# equivalent: https://github.com/orhanemree/aldrin/blob/master/examples/rectangles.c

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


def main():
    aldrin.draw_rectangle(100, 100, 200, 105, 0x0000ff, 2)
    aldrin.fill_rectangle(0, 0, 50, 90, 0xff0000)

    aldrin.fill_square(100, 100, 50, 0x00ff00)
    aldrin.draw_square(250, 250, 50, 0xffffff, 2)
    
    aldrin.save_ppm("output/rectangles.ppm")


if __name__ == "__main__":
    main()
