#!/usr/bin/env python  
# encoding: utf-8  
import urllib2
import urllib
import re
import os
import sys
import time
import threading
import random
from PIL import Image

from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

reload(sys)
sys.setdefaultencoding("utf-8")

IMG_ORIGIN_PATH = "data"
IMG_SIZE = 300


class DownloadImage:
    def __init__(self, query_file_name):
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
        self.headers = {'User-Agent': self.user_agent}

        #setting proxy for google engine
        proxy_handler = urllib2.ProxyHandler({u'socks': '127.0.0.1', 'socks': '127.0.0.1'})
        opener = urllib2.build_opener(proxy_handler)
        urllib2.install_opener(opener)

        # read <chinese, english> pair from name_list.txt file
        self.query_dict = {}  # 读取<中文，英文>对保存至词典
        with open(query_file_name) as query_file:
            for line_str in query_file:
                ch_en = line_str.strip().decode('utf-8').split('=')
                self.query_dict[ch_en[0]] = ch_en[1].strip()

        # 不同搜索引擎的图片url提取的正则表达式不一样
        self.img_regx = {
            'google': r'\\"ou\\":\\"(.*?)\\"',
            'bing': 'src="(.*?)"',
            'sogou': '"pic_url":"(.*?)"',
            'baidu': '"objURL":"(.*?)"',
            '360': '"img":"(.*?)"'
        }

    def get_engine_url(self, engine, query, bat_num):
        if engine == 'google':
            url = 'https://www.google.com/search'
            params = {
                'hl': 'en',
                'yv': 2,
                'tbm': 'isch',
                'q': query,
                'ijn': bat_num,
                'start': bat_num * 100,
                'asearch': 'ichunk',
                'async': '_id:rg_s,_pms:s'
            }
        elif engine == 'sogou':
            url = 'http://pic.sogou.com/pics'
            params = {
                'query': query,
                'mode': 1,
                'start': bat_num * 48,
                'reqType': 'ajax',
                'reqFrom': 'result',
                'tn': 0
            }
        elif engine == 'baidu':  # 注意百度的搜索词不需要进行编码
            url = "http://image.baidu.com/search/avatarjson"
            params = {
                'tn': 'resultjsonavatarnew',
                'ie': 'utf-8',
                'word': query,
                'rn': 60,
                'pn': bat_num * 60
            }
        elif engine == 'bing':
            url = 'http://www.bing.com/images/async'
            params = {
                'q': query,
                'first': bat_num * 36,
                'count': 35,
                'relp': 35,
                'lostate': 'r',
                'mmasync': 1
            }
        elif engine == '360':
            url = 'http://image.so.com/j'
            params = {
                'q': query,
                'src': 'srp',
                'correct': query,
                'sn': bat_num * 60,
                'pn': 60
            }
        else:
            print("Sorry, we don't know the engine")
            exit(0)
        return url + "?" + urllib.urlencode(params)

    def download_img(self, engine, query, batch):
        for bat_num in range(0, batch):
            # 生成文件夹（如果不存在的话）
            path = os.path.join(IMG_ORIGIN_PATH, self.query_dict[query])
            if not os.path.exists(path):
                os.makedirs(path)
            try:
                url = self.get_engine_url(engine, query, bat_num)
                print(url)
                req = urllib2.Request(url, headers=self.headers)
                res = urllib2.urlopen(req)
                page = res.read()
                # print(page)
                # 因为JSON的原因，在浏览器页面按F12看到的，和你打印出来的页面内容是不一样的，所以匹配的是objURL这个东西，对比一下页面里别的某某URL，那个能访问就用那个
                img_srcs = re.findall(self.img_regx[engine], page, re.S)
                print query, len(img_srcs)
            except IOError as e:
                # 如果访问失败，就跳到下一个继续执行代码，而不终止程序
                print query, " error:", e
                continue

            cur_img_id = 0
            # 访问上述得到的图片路径，保存到本地
            for src in img_srcs:
                src = src.replace('\\', '')
                print(src)
                with open(os.path.join(path, self.query_dict[query] + str(int(time.time())) +
                        str(int(random.random() * 1000)) + '.jpg'), 'wb') as img_file:
                    try:
                        print query + " downloading No.%d" % (cur_img_id + bat_num * len(img_srcs))
                        # 设置一个urlopen的超时，如果3秒访问不到，就跳到下一个地址，防止程序卡在一个地方。
                        img = urllib2.urlopen(src, timeout=3)
                        img_file.write(img.read())
                    except:
                        print query + "No.%d error:" % (cur_img_id + bat_num * len(img_srcs))
                        continue
                cur_img_id += 1

    def img_preprocess(self, query):
        print("start resize image " + query)
        file_names = os.listdir(os.path.join(IMG_ORIGIN_PATH, self.query_dict[query]))

        output_path = os.path.join(IMG_ORIGIN_PATH, self.query_dict[query])
        if not os.path.exists(output_path):
            os.mkdir(output_path)

        idx = 0
        for name in file_names:
            if ".jpg" in name:
                file_path = os.path.join(IMG_ORIGIN_PATH, self.query_dict[query], name)
                img_data = Image.open(file_path).convert('RGB')
                if img_data is not None:
                    out_path = os.path.join(output_path, self.query_dict[query] + '-%05d' % idx + ".jpg")
                    # print(file_path, out_path)
                    img_data.save(out_path)
                    idx += 1
                else:
                    print(file_path)
                os.remove(file_path)
        print("finished resize image")


class DownloadThread(threading.Thread):
    def __init__(self, engine, query_list, batch):
        threading.Thread.__init__(self)
        self.engine = engine
        self.query_list = query_list
        self.batch = batch

    def run(self):
        print('starting download from engine:%s, batch=%d\n' % (self.engine, self.batch))
        for query in self.query_list:
            print('start downloading images from engine:%s, query:%s\n' % (self.engine, query))
            # 以下是对已下载的图片进行resize操作
            # print('start resizing dir:%s' % query)
            # img_download.img_preprocess(query)
            img_download.download_img(self.engine, query, self.batch)
        print('finished download batch %d from engine:%s\n' % (self.batch, self.engine))


# 主程序，读txt文件开始爬
if __name__ == '__main__':
    query_file = "name_list.txt"
    img_download = DownloadImage(query_file)
    threads = []

    for engine in ['google', 'bing', 'baidu', 'sogou', '360']:
        if engine == 'bing':
            batch = 20
        else:
            batch = 50
            # 读取查询的关键词
        download_thread = DownloadThread(engine, img_download.query_dict.keys(), batch)
        download_thread.start()
        threads.append(download_thread)

    for t in threads:  # join all threads for terminate
        t.join()
    print('all download, bye')
