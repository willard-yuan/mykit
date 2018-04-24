
#include "siftsIndex.hpp"

using namespace std;
using namespace hnswlib;

typedef std::function<bool(std::pair<std::string, int>, std::pair<std::string, int>)> Comparator;
Comparator compFunctor = [](std::pair<std::string, int> elem1 ,std::pair<std::string, int> elem2)
{
    return elem1.second > elem2.second;
};


int main(int argc, char** argv) {

    int vecdim = 128;
    int numSifts = 5;
    int rank = 5;
    const std::string geoInfoPath = "../data/sifts_125402_geoInfo.bin";
    const std::string indexInfoPath = "../data/sifts_125402m_ef_80_M_32_ip.bin";
    
    siftsIDX *siftIdx = new siftsIDX(geoInfoPath, indexInfoPath);
    
    float *massb = new float[vecdim];
    
    std::map<string, int> relateID;
    
    cv::Ptr<cv::Feature2D> detector = cv::xfeatures2d::SIFT::create(128);
    cv::Mat im = cv::imread("../data/201505310117china2.jpg", 1);
    if (im.empty()) return 0;
    
    std::vector<cv::KeyPoint> keypoints;
    cv::Mat img_descs;
    detector->detect(im, keypoints);
    detector->compute(im, keypoints, img_descs);
    
    if (keypoints.size() < 5) {
        std::cout << "too few feature points: " << std::endl;
        return 0;
    }
    
    siftIdx->rootSift(img_descs);
    
    std::vector<rankInfo> rankRet;
    
    rankInfo tmp;
    for(int i = 0; i < img_descs.rows; i++) {
        
        for(int j = 0; j < vecdim; j++) {
            massb[j] = img_descs.at<float>(i, j);
        }
        std::priority_queue<std::pair<float, labeltype >> candidates = siftIdx->appr_alg->searchKnn((void *)massb, numSifts);
        
        // 剔除不满足要求的SIFT点
        for(int k = 0; k < numSifts; k++) {
            if(abs(candidates.top().first) < 0.1 && abs(keypoints.at(i).angle - siftIdx->geosInfo.at(candidates.top().second).Pt.angle) < 10){
                //cout << siftIdx->geosInfo.at(candidates.top().second).fileBaseName << ", angle diff: " << abs(keypoints.at(i).angle - siftIdx->geosInfo.at(candidates.top().second).Pt.angle) << ", dist: " << candidates.top().first << endl;
                tmp.numMatched[siftIdx->geosInfo.at(candidates.top().second).fileBaseName] += 1;
                tmp.matchedPair[siftIdx->geosInfo.at(candidates.top().second).fileBaseName].push_back(std::make_pair(i, k));
            }
            candidates.pop();
        }
        //cout << "*******************" << endl;
    }
    
    std::set<std::pair<std::string, int>, Comparator> sortRank(tmp.numMatched.begin(), tmp.numMatched.end(), compFunctor);
    
    // 几何重排
    int recount = 0;
    for (std::pair<std::string, int> element : sortRank){
        if(recount < rank){
            std::cout << "top@" << recount+1 << ": " <<element.first << ": " << element.second << std::endl;
            ++recount;
            
        }
    }
    
    delete [] massb;
    
    return 0;
}
