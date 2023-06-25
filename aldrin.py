from os import path
import platform
import ctypes

# relative path to source
curr_path = path.abspath(__file__)
parent_path = path.dirname(curr_path)

# decide source path according to operation system
op_system = platform.system()

source_path = path.join(parent_path, "bin/aldrin.so")
if op_system == "Windows":
    source_path = path.join(parent_path, "bin/aldrin.dll")

lib = ctypes.CDLL(source_path);


# Aldrin_Canvas
class Aldrin_Canvas(ctypes.Structure):
    _fields_ = [
        ("pixels", ctypes.POINTER(ctypes.c_uint32)),
        ("width", ctypes.c_uint32),
        ("height", ctypes.c_uint32)
    ]


# aldrin_put_pixel()
lib.aldrin_put_pixel.argtypes = [Aldrin_Canvas, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32]
lib.aldrin_put_pixel.restype = None


# aldrin_fill()
lib.aldrin_fill.argtypes = [Aldrin_Canvas, ctypes.c_uint32]
lib.aldrin_fill.restype = None


# aldrin_draw_line()
lib.aldrin_draw_line.argtypes = [Aldrin_Canvas, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, 
                                 ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32]
lib.aldrin_draw_line.restype = None


# aldrin_draw_triangle()
lib.aldrin_draw_triangle.argtypes = [Aldrin_Canvas, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32,
                                     ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32,
                                     ctypes.c_uint32]
lib.aldrin_draw_triangle.restype = None


# aldrin_fill_triangle()
lib.aldrin_fill_triangle.argtypes = [Aldrin_Canvas, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32,
                                     ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32]
lib.aldrin_fill_triangle.restype = None


# aldrin_draw_ellipse()
lib.aldrin_draw_ellipse.argtypes = [Aldrin_Canvas, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32,
                                    ctypes.c_uint32, ctypes.c_uint32]
lib.aldrin_draw_ellipse.restype = None


# aldrin_fill_ellipse()
lib.aldrin_fill_ellipse.argtypes = [Aldrin_Canvas, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32,
                                    ctypes.c_uint32, ctypes.c_uint32]
lib.aldrin_fill_ellipse.restype = None


# aldrin_draw_circle()
lib.aldrin_draw_circle.argtypes = [Aldrin_Canvas, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32,
                                    ctypes.c_uint32]
lib.aldrin_draw_circle.restype = None


# aldrin_fill_circle()
lib.aldrin_fill_circle.argtypes = [Aldrin_Canvas, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32,
                                    ctypes.c_uint32]
lib.aldrin_fill_circle.restype = None


# aldrin_draw_rectangle()
lib.aldrin_draw_rectangle.argtypes = [Aldrin_Canvas, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32,
                                    ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32]
lib.aldrin_draw_rectangle.restype = None


# aldrin_fill_rectangle()
lib.aldrin_fill_rectangle.argtypes = [Aldrin_Canvas, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32,
                                    ctypes.c_uint32, ctypes.c_uint32]
lib.aldrin_fill_rectangle.restype = None


# aldrin_draw_square()
lib.aldrin_draw_square.argtypes = [Aldrin_Canvas, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32,
                                    ctypes.c_uint32, ctypes.c_uint32]
lib.aldrin_draw_square.restype = None


# aldrin_fill_square()
lib.aldrin_fill_square.argtypes = [Aldrin_Canvas, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32,
                                    ctypes.c_uint32]
lib.aldrin_fill_square.restype = None


# aldrin_text()
lib.aldrin_text.argtypes = [Aldrin_Canvas, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_char_p, 
                            ctypes.c_uint32, ctypes.c_uint32]
lib.aldrin_text.restype = None


# aldrin_get_pixels()
# note: same as list(ctypes.cast(ac.pixels, ctypes.POINTER(ctypes.c_uint32*(ac.width*ac.height))).contents)
lib.aldrin_get_pixels.argtypes = [Aldrin_Canvas]
lib.aldrin_get_pixels.restype = ctypes.POINTER(ctypes.c_uint32)


# aldrin_get_width()
lib.aldrin_get_width.argtypes = [Aldrin_Canvas]
lib.aldrin_get_width.restype = ctypes.c_uint32


# aldrin_get_height()
lib.aldrin_get_height.argtypes = [Aldrin_Canvas]
lib.aldrin_get_height.restype = ctypes.c_uint32

# aldrin_save_ppm()
lib.aldrin_save_ppm.argtypes = [Aldrin_Canvas, ctypes.c_char_p]
lib.aldrin_save_ppm.restype = None


# implement library object oriented

class Aldrin:
    
    def __init__(self, pixels: list[int], width: int, height: int):
        self.width = width
        self.height = height
        self.ac = Aldrin_Canvas((ctypes.c_uint32 * len(pixels))(*pixels), width, height)
        
    
    def put_pixel(self, x: int, y: int, color: int):
        lib.aldrin_put_pixel(self.ac, x, y, color)
        
        
    def fill(self, fill_color: int):
        lib.aldrin_fill(self.ac, fill_color)
    

    def draw_line(self, x1: int, y1: int, x2: int, y2: int, line_color: int, thickness: int):
        lib.aldrin_draw_line(self.ac, x1, y1, x2, y2, line_color, thickness)
        
    
    def draw_triangle(self, x1: int, y1: int, x2: int, y2: int, x3: int, y3: int, line_color: int, thickness: int):
        lib.aldrin_draw_triangle(self.ac, x1, y1, x2, y2, x3, y3, line_color, thickness)
        
    
    def fill_triangle(self, x1: int, y1: int, x2: int, y2: int, x3: int, y3: int, fill_color: int):
        lib.aldrin_fill_triangle(self.ac, x1, y1, x2, y2, x3, y3, fill_color)
        
    
    def draw_ellipse(self, x: int, y: int, rx: int, ry: int, line_color: int):
        lib.aldrin_draw_ellipse(self.ac, x, y, rx, ry, line_color)
        
    
    def fill_ellipse(self, x: int, y: int, rx: int, ry: int, fill_color: int):
        lib.aldrin_fill_ellipse(self.ac, x, y, rx, ry, fill_color)
        
    
    def draw_circle(self, x: int, y: int, r: int, line_color: int):
        lib.aldrin_draw_circle(self.ac, x, y, r, line_color)
        
    
    def fill_circle(self, x: int, y: int, r: int, fill_color: int):
        lib.aldrin_fill_circle(self.ac, x, y, r, fill_color)
        
    
    def draw_rectangle(self, x: int, y: int, w: int, h: int, line_color: int, thickness: int):
        lib.aldrin_draw_rectangle(self.ac, x, y, w, h, line_color, thickness)
        
    
    def fill_rectangle(self, x: int, y: int, w: int, h: int, fill_color: int):
        lib.aldrin_fill_rectangle(self.ac, x, y, w, h, fill_color)
        
    
    def draw_square(self, x: int, y: int, l: int, line_color: int, thickness: int):
        lib.aldrin_draw_square(self.ac, x, y, l, line_color, thickness)
        
    
    def fill_square(self, x: int, y: int, l: int, fill_color: int):
        lib.aldrin_fill_square(self.ac, x, y, l, fill_color)
        
    
    def text(self, x: int, y: int, text: str, text_color: int, text_size: int):
        lib.aldrin_text(self.ac, x, y, text.encode(), text_color, text_size)
        
        
    def get_pixels(self) -> list[int]:
        # retursn pixels' ptr in C
        ptr = lib.aldrin_get_pixels(self.ac)
        pixels_len = self.width*self.height
        # get pixels as array from ptr from C 
        pixels = ctypes.cast(ptr, ctypes.POINTER(ctypes.c_uint32*pixels_len)).contents
        # convert to python list and return
        return list(pixels)
    
        
    def get_width(self) -> int:
        return lib.aldrin_get_width(self.ac)
    
    
    def get_height(self) -> int:
        return lib.aldrin_get_width(self.ac)
    
    
    def save_ppm(self, filename: str):
        lib.aldrin_save_ppm(self.ac, filename.encode());
