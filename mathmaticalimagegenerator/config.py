from json import load, JSONDecodeError

config_file = "config.json"

class Config:
    # Static Values
    default_height = 100
    default_width = 100
    default_mode = "rgb"
    default_palette = "black_white"

    # Attributes
    __slots__ = ("_width", "_height", "_mode", "_palette_name")
    _width: int
    _height: int
    _mode: str
    _palette_name: str

    def __init__(self):
        self._initialize_default_values()
        self._load_config()

    def _load_config(self):
        try:
            with open(config_file, 'r') as file:
                data = load(file)
                self._height = data.get('height', Config.default_height)
                self._width = data.get('width', Config.default_height)
                self._mode = data.get('color_mode', Config.default_height)
                self._palette_name = data.get('palette', Config.default_height)
        except FileNotFoundError:
            print(f"Error: {config_file} not found")
        except JSONDecodeError as e:
            print(f"Error decoding {config_file}: {e}")

    def _initialize_default_values(self):
        self._width = Config.default_width
        self._height = Config.default_height
        self._mode = Config.default_mode
        self._palette_name = Config.default_palette

    def get_height(self):
        return self._height

    def get_width(self):
        return self._width

    def get_palette_name(self):
        return self._palette_name

    def get_color_mode(self):
        return self._mode