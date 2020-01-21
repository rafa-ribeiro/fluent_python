from math import hypot


class Vector:

	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def __repr__(self):
		return f"Vector({self.x}, {self.y})"

	def __abs__(self):
		return hypot(self.x, self.y)

	def __bool__(self):
		return bool(self.x or self.y)

	def __add__(self, other):
		x = self.x + other.x
		y = self.y + other.y
		return Vector(x=x, y=y)

	def __mul__(self, scalar):
		x = self.x * scalar
		y = self.y * scalar
		return Vector(x=x, y=y)