CXX = g++
CXXFLAGS = -std=c++23 -Wall -Wextra -O2 -fPIC
TARGET = libutils.a
SOURCES = $(wildcard *.cpp)
OBJECTS = $(SOURCES:.cpp=.o)

.PHONY: all clean

all: $(TARGET)

$(TARGET): $(OBJECTS)
	ar rcs $(TARGET) $(OBJECTS)

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -f $(TARGET) $(OBJECTS)