# equivalent: https://github.com/orhanemree/aldrin/blob/master/examples/ellipses.c

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
    aldrin.fill_ellipse(0, 0, 10, 50, 0x00ff00)
    aldrin.fill_ellipse(100, 100, 110, 50, 0xff0000)
    aldrin.draw_ellipse(0, 190, 90, 50, 0x0000ff)

    r = 20
    aldrin.fill_circle(100-r, 100-r, r, 0xffffff)
    
    aldrin.save_ppm("output/ellipses.ppm")


if __name__ == "__main__":
    main()
