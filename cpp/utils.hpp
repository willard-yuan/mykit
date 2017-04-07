/***************************
 * My useful functions
 * Author: yuanyong.name
 ***************************/

#ifndef utils_hpp
#define utils_hpp

#include <stdio.h>
#include <glob.h>
#include <math.h>
#include <string>
#include <sstream>
#include <vector>
#include <numeric>
#include <algorithm>

/***************************
 * File processing functions
 ***************************/

std::vector<std::string> split(const std::string &s, char delim);
std::vector<std::string> glob_vector(const std::string& pattern);
std::string base_name(std::string const & path, std::string const & delims = "/\\");
std::string remove_extension(std::string const & filename);


/***************************
 * Math processing functions
 ***************************/

float cosine_similarity(std::vector<float> v1, std::vector<float> v2);

#endif /* utils_hpp */
