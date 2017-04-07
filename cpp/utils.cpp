
#include "utils.hpp"

/***************************
 * File processing functions
 ***************************/

// Split string by special char, such as by space
// Usage: split("hello world", ' ')
std::vector<std::string> split(const std::string &s, char delim) {
    std::vector<std::string> elems;
    std::stringstream ss(s);
    std::string item;
    while (getline(ss, item, delim)) {
        elems.push_back(item);
    }
    return elems;
}

// Get the files full paths from directory
std::vector<std::string> glob_vector(const std::string& pattern){
    glob_t glob_result;
    glob(pattern.c_str(), GLOB_TILDE, NULL, &glob_result);
    std::vector<std::string> files;
    for(unsigned int i=0;i<glob_result.gl_pathc;++i){
        auto tmp = std::string(glob_result.gl_pathv[i]);
        files.push_back(tmp);
    }
    std::sort(files.begin(), files.end());
    globfree(&glob_result);
    return files;
}

// Get base name from a full path
// Usage: base_name("/xxx/xxx/123.jpg")
// Output: 123.jpg
std::string base_name(std::string const & path, std::string const & delims){
    return path.substr(path.find_last_of(delims) + 1);
}

// Remove extension from a base name
// Usage: remove_extension("123.jpg")
// Output: 123
std::string remove_extension(std::string const & filename){
    typename std::string::size_type const p(filename.find_last_of('.'));
    return p > 0 && p != std::string::npos ? filename.substr(0, p) : filename;
}


/***************************
 * Math processing functions
 ***************************/

// Compute cosine similarity between two vectors
float cosine_similarity(std::vector<float> v1, std::vector<float> v2){
    float dot = 0.0, denom_a = 0.0, denom_b = 0.0 ;
    dot = std::inner_product( v1.begin(), v1.end(), v2.begin(), 0.0 );
    denom_a = std::inner_product( v1.begin(), v1.end(), v1.begin(), 0.0 );
    denom_b = std::inner_product( v2.begin(), v2.end(), v2.begin(), 0.0 );
    return dot / (sqrt(denom_a) * sqrt(denom_b));
}
