import os
import glob

from shutil import copyfile

text_list = glob.glob('/home/willard/data/gt_files/*.txt')
oxford_building_images = '/home/willard/data/oxbuild_images_backup/'
dst = '/home/willard/data/oxford_queries/'

queries_list = []

for tmp_text in text_list:
    head, tail = os.path.split(tmp_text)
    if(tail[-9:-4] == 'query'):
        queries_list.append(os.path.join(head, tail))

queries_image_name = []
for tmp_query_txt in queries_list:
    lines = [line.rstrip('\n').split()[0] + '.jpg' for line in open(tmp_query_txt)]
    queries_image_name.append(os.path.join(oxford_building_images, lines[0][5:]))
    copyfile(os.path.join(oxford_building_images, lines[0][5:]), os.path.join(dst,lines[0][5:]))

print queries_image_name
