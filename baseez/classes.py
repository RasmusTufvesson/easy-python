class _Vector2Base:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def get(self):#, instance, owner):
        return self.x, self.y
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return Vector2(self.x * other.x, self.y * other.y)
    def __truediv__(self, other):
        return Vector2(self.x // other.x, self.y // other.y)
    def __div__(self, other):
        return Vector2(self.x / other.x, self.y / other.y)
    def __lt__(self, other):
        return self.x < other.x and self.y < other.y
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)
    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(other)
    def __ne__(self, other):
        return not self.__eq__(other)
    def __iadd__(self, other):
        self = Vector2(self.x + other.x, self.y + other.y)
    def __isub__(self, other):
        self = Vector2(self.x - other.x, self.y - other.y)
    def __imul__(self, other):
        self = Vector2(self.x * other.x, self.y * other.y)
    def __itruediv__(self, other):
        self = Vector2(self.x // other.x, self.y // other.y)
    def __idiv__(self, other):
        self = Vector2(self.x / other.x, self.y / other.y)

class Vector2(_Vector2Base):
    ZERO = _Vector2Base(0, 0)
    RIGHT = _Vector2Base(1, 0)
    LEFT = _Vector2Base(-1, 0)
    UP = _Vector2Base(0, -1)
    DOWN = _Vector2Base(0, 1)

class _ColorBase:
    def __init__(self, rgb: tuple):
        self.rgb = self._correct_color(rgb)
    
    def get(self):#, instancem, owner):
        return self.rgb

    def _correct_color(self, val):
        for v in range(len(val)):
            if val[v]>255:
                val[v] = 255
            elif val[v]<0:
                val[v] = 0
        return val

class Color(_ColorBase):
    BLACK = _ColorBase((0,0,0))
    WHITE = _ColorBase((255,255,255))
    RED = _ColorBase((255,0,0))
    GREEN = _ColorBase((0,255,0))
    BLUE = _ColorBase((0,0,255))