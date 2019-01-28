#!/bin/bash

python main.py
convert -units PixelsPerInch preprocessed_img/test.png -density 300 preprocessed_img/test_dpi300.png
clang++ -o test main_tesseract.cpp -llept -ltesseract -std=c++11
./test