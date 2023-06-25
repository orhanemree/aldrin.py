from aldrin import Aldrin

width  = 160
height = 90
pixels = [0] * (width*height)
aldrin = Aldrin(pixels, width, height)


def main():
    aldrin.fill(0xff00ff)
    aldrin.save_ppm("hello-world.ppm")


if __name__ == "__main__":
    main()
