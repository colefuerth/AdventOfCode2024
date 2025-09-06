CXX = g++
CXXFLAGS = -std=c++23 -Wall -Wextra -O2 -I../include
LDFLAGS = -ltbb
TARGET = aoc
SOURCE = aoc.cpp
INCLUDE_LIB = ../include/libutils.a

.PHONY: build run test clean

build: $(TARGET)

$(INCLUDE_LIB):
	$(MAKE) -C ../include

$(TARGET): $(SOURCE) $(INCLUDE_LIB)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(SOURCE) $(INCLUDE_LIB) $(LDFLAGS)

run: $(TARGET)
	./$(TARGET) input.txt

test: $(TARGET)
	./$(TARGET) small.txt

clean:
	rm -f $(TARGET)