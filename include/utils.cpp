#include "utils.hpp"
#include <fstream>

std::vector<std::string> readFile(const std::string& filename) {
    std::ifstream file(filename);
    std::vector<std::string> lines;
    std::string line;
    while (getline(file, line)) {
        lines.push_back(line);
    }
    return lines;
}
