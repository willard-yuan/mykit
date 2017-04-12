
/***************************
 * My useful functions
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
void SplitString(const std::string& s, std::vector<std::string>& v, const std::string& c);


/***************************
 * Math processing functions
 ***************************/

float cosine_similarity(std::vector<float> &v1, std::vector<float> &v2);
std::vector<float> nomalize_vecotor(std::vector<float> &v);

#endif /* utils_hpp */
