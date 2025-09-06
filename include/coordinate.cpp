#include "coordinate.hpp"
#include <iostream>

coordinate2d operator+(const coordinate2d& a, const coordinate2d& b) {
    return coordinate2d(a.x + b.x, a.y + b.y);
}
coordinate2d operator-(const coordinate2d& a, const coordinate2d& b) {
    return coordinate2d(a.x - b.x, a.y - b.y);
}
bool operator==(const coordinate2d& a, const coordinate2d& b) {
    return a.x == b.x && a.y == b.y;
}
bool operator!=(const coordinate2d& a, const coordinate2d& b) {
    return !(a == b);
}
coordinate2d operator*(const coordinate2d& a, int s) {
    return coordinate2d(a.x * s, a.y * s);
}
coordinate2d& operator+=(coordinate2d& a, const coordinate2d& b) {
    a.x += b.x;
    a.y += b.y;
    return a;
}
coordinate2d& operator-=(coordinate2d& a, const coordinate2d& b) {
    a.x -= b.x;
    a.y -= b.y;
    return a;
}
std::ostream& operator<<(std::ostream& os, const coordinate2d& c) {
    os << "(" << c.x << ", " << c.y << ")";
    return os;
}
std::istream& operator>>(std::istream& is, coordinate2d& c) {
    char ch1, ch2, ch3;
    is >> ch1 >> c.x >> ch2 >> c.y >> ch3;
    if (ch1 != '(' || ch2 != ',' || ch3 != ')') {
        is.setstate(std::ios::failbit);
    }
    return is;
}
size_t hash_value(const coordinate2d& c) {
    return std::hash<int>()(c.x) ^ (std::hash<int>()(c.y) << 1);
}