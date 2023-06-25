# equivalent: https://github.com/orhanemree/aldrin/blob/master/examples/text.c

from os import path
import sys

# change path to paretn to load aldrin.py
parent_dir = path.dirname(path.dirname(path.abspath(__file__)))
sys.path.append(parent_dir)

from aldrin import Aldrin

width  = 200
height = 200
pixels = [0] * (width*height)
aldrin = Aldrin(pixels, width, height)


# this definitions are default values in C
AC_GLYPHS_WIDTH  = 3
AC_GLYPHS_HEIGHT = 5
AC_TEXT_SPACING  = 1

def main():
    aldrin.text(0, 0, "abcdefghijklmnopqrstuvwxyz", 0xffffff, 1);
    aldrin.text(0, AC_GLYPHS_HEIGHT, "ABCDEFGHIJKLMNOPQRSTUVWXYZ", 0xff0000, 2)
    aldrin.text(20, 4*AC_GLYPHS_HEIGHT, "01234 56789", 0x00ff00, 3)

    """
    multiply them to center text horizontally to canvas:
        7: text length
        AC_GLYPHS_WIDTH: 3 pixels by default in the library
        AC_TEXT_SPACING: 1 pixel by default in the library
        5: font size specified as function param
    """
    
    x = 7*(AC_GLYPHS_WIDTH+AC_TEXT_SPACING)*5;
    
    aldrin.text((width-x)//2, 100, "+-*/\\.,", 0x0000ff, 5)
    aldrin.text((width-x)//2, 150, "_?!'\":;", 0x0000ff, 5)
    
    aldrin.save_ppm("output/text.ppm")


if __name__ == "__main__":
    main()
