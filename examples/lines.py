# equivalent: https://github.com/orhanemree/aldrin/blob/master/examples/lines.c

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
    aldrin.draw_line(width+5, height+5, width//2-1, 1, 0xff0000, 3)
    aldrin.draw_line(width//2-1, height-1, 1, 1, 0x00ff00, 1)
    aldrin.draw_line(0, 0, width-1, 0, 0x0000ff, 1)
    aldrin.draw_line(0, 0, 0, height+100, 0x0000ff, 1)
    
    aldrin.save_ppm("output/lines.ppm")


if __name__ == "__main__":
    main()
