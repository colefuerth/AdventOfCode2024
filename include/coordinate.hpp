#pragma once
#include <iostream>

class coordinate2d {
    public:
        int x;
        int y;
        coordinate2d(int x_val, int y_val) : x(x_val), y(y_val) {}
};

// Operator declarations
coordinate2d operator+(const coordinate2d& a, const coordinate2d& b);
coordinate2d operator-(const coordinate2d& a, const coordinate2d& b);
bool operator==(const coordinate2d& a, const coordinate2d& b);
bool operator!=(const coordinate2d& a, const coordinate2d& b);
coordinate2d operator*(const coordinate2d& a, int s);
coordinate2d& operator+=(coordinate2d& a, const coordinate2d& b);
coordinate2d& operator-=(coordinate2d& a, const coordinate2d& b);
std::ostream& operator<<(std::ostream& os, const coordinate2d& c);
std::istream& operator>>(std::istream& is, coordinate2d& c);
size_t hash_value(const coordinate2d& c);

namespace std {
    template <>
    struct hash<coordinate2d> {
        size_t operator()(const coordinate2d& c) const {
            return hash_value(c);
        }
    };
}
