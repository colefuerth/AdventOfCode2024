#include <iostream>
#include <string>
#include <vector>
#include <array>

#include "../include/utils.hpp"
#include "../include/coordinate.hpp"

using namespace std;

int search_from(array<coordinate2d, 2> cd, const vector<string>& lines, const string& target) {
    coordinate2d c = cd[0];
    coordinate2d d = cd[1];
    size_t rows = lines.size();
    size_t cols = lines[0].size();
    size_t len = target.size();
    coordinate2d end = c + (d * (int)(len - 1));
    if (end.x < 0 || end.x >= (int)cols || end.y < 0 || end.y >= (int)rows) {
        return 0;
    }
    for (size_t i = 0; i < len; i++) {
        if (lines[c.y][c.x] != target[i]) {
            return 0;
        }
        c += d;
    }
    return 1;
}

const vector<coordinate2d> directions = {
    {1, 0},   // right
    {0, 1},   // down
    {-1, 0},  // left
    {0, -1},  // up
    {1, 1},   // down-right
    {-1, 1},  // down-left
    {1, -1},  // up-right
    {-1, -1}  // up-left
};

int main(int argc, char* argv[]) {
    if (argc != 2) {
        cerr << "Usage: " << argv[0] << " <input_file>" << endl;
        return 1;
    }
    vector<string> lines = readFile(argv[1]);
    vector<array<coordinate2d, 2>> inputs;
    inputs.reserve(lines.size() * lines[0].length() * directions.size());
    for (size_t y = 0; y < lines.size(); y++) {
        for (size_t x = 0; x < lines[0].length(); x++) {
            for (const auto& d : directions) {
                inputs.push_back({coordinate2d((int)x, (int)y), d});
            }
        }
    }
    const string target = "XMAS";
    vector<int> results = map_reduce<array<coordinate2d, 2>, int>(inputs, search_from, lines, target);
    int total = 0;
    for (const auto& r : results) {
        total += r;
    }
    cout << "Total occurrences of '" << target << "': " << total << endl;
    return 0;
}
