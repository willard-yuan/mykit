//
//  utils.cpp
//  bag-of-words
//
//  Created by willard on 8/18/15.
//  Copyright (c) 2015 wilard. All rights reserved.
//


#include "utils.h"
using namespace std;

namespace func {
    vector<string> ReadAllLinesFromFile(const string& filename){
        ifstream file(filename);
        vector<string> fileNames;
        string temp;
        while(std::getline(file, temp)) {
            cout << temp << endl;
            const size_t found = temp.find_last_of("/\\");
            auto fileImg  = temp.substr(0,found) + "/" + temp.substr(found+1);
            fileNames.push_back(fileImg);
        }
        file.close();
        return fileNames;
    }
}