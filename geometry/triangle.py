from geometry.shape import Shape
import math


class Triangle(Shape):

    def __init__(self, a: float, b: float, c: float):
        if not self._is_valid_triangle(a, b, c):
            raise ValueError("Invalid triangle sides")
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_angled(self) -> bool:
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2)

    @staticmethod
    def _is_valid_triangle(a, b, c) -> bool:
        return a + b > c and a + c > b and b + c > a
