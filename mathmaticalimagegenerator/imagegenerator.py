from PIL import Image
# import math
from math import log, pi
import random

from mathmaticalimagegenerator.config import Config
from .palettes import rgb_palettes


width = 500
height = 500

class ImageGenerator:

    __slots__ = ("_config",)
    _config: Config

    def __init__(self):
        self._config = Config()

    def make_image(self):
        im: Image.Image = Image.new(mode="RGB", size=(self._config.get_width(), self._config.get_height()))
        palette = rgb_palettes.get(self._config.get_palette_name())
        if palette is None:
            print("ERROR: Palette not found!")
            return
        for x in range(self._config.get_width()):
            for y in range(self._config.get_height()):
                im.putpixel((x, y), palette[self.color_function(x, y, len(palette))])
        im.save("picture.png")

    def color_function(self, x: int , y: int, scale: int) -> int:
        """Any function which takes two integer arguments x & y, and returns an integer in range [0,scale)."""

        return int(((x**2)+(y**2))*pi) % scale

        # Other function options: #
        #return ((x**2) - (y**2)) % scale
        #return (x**((x*y)%5)) % scale
        #return min(x%max(y,1),y%max(x,1)) % scale
        #return int(round(((x**math.pi) + (y**math.e // (x+1))), 0)) % scale
        #return x*y % scale
