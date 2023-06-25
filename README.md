<p align="center">
    <img src="img/lily_aldrin.png">
</p>

# 👩‍🦰 Aldrin.py
Python wrapper for [Aldrin](https://github.com/orhanemree/aldrin) 2D Computer Graphics Library in C.

Visit [Aldrin](https://github.com/orhanemree/aldrin) to C source code repository.

Visit [Playground](https://orhanemree.github.io/aldrin.js/playground.html) to try online.

## Quick Start
* Clone the repo.
```bash
$ git clone https://github.com/orhanemree/aldrin.py.git
$ cd aldrin.py
```
* Import `Aldrin` class from `aldrin.py` module in your code.
```python
from aldrin import Aldrin # that's it!
```

## `Hello, World!` of Pixels
```python
from aldrin import Aldrin

width  = 160
height = 90
pixels = [0] * (width*height)
aldrin = Aldrin(pixels, width, height)


def main():
    aldrin.fill(0xff00ff)
    aldrin.save_ppm("img/hello_world.ppm")


if __name__ == "__main__":
    main()
```
Output should look something like this:

<img src="img/hello_world.png">

Note that: `aldrin.save_ppm()` function generates `.ppm` output (see [`/img/hello_world.ppm`](img/hello_world.ppm)). The output converted to `.png` format to be displayed here.

## Build
* This repo and Quick Start is up to date and ready to use. But if you want to build shared library yourself go source code repo, download `src/aldrin.c` and run:
```bash
# for Unix-like
$ gcc -shared -o bin/aldrin.so src/aldrin.c
# for Windows
$ gcc -shared -o bin/aldrin.dll src/aldrin.c
```

## Examples
* See [`/examples`](examples).

## Running Tests
```bash
$ cd test
$ python main.py
```
* Get more info:
```bash
$ python main.py help
```

## Documentation
* See [`Documentation`](https://orhanemree.github.io/aldrin.js/reference.html) to read docs and run examples live.
* Important: Documentation is for C actually. But since this Python version uses Aldrin with class structure function names are slightly different. For example: `aldrin_fill()` in C is `aldrin.fill()` in Python wrapper. You can understand better if you compare examples in this repo and in the source code repo. The equivalent of each example is mentiones in the first line of the example.

## License
* Licensed under the [MIT License](LICENSE).