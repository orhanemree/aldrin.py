# equivalent: https://github.com/orhanemree/aldrin/blob/master/examples/triangles.c

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
    aldrin.fill_triangle(5, 10, 5, 100, 120, 10, 0xff0000)
    aldrin.fill_triangle(80, 80, 50, 130, 130, 90, 0x00ff00)
    aldrin.fill_triangle(width-10, 20, 90, 190, 210, 150, 0x0000ff)
    
    aldrin.save_ppm("output/triangles.ppm")


if __name__ == "__main__":
    main()
