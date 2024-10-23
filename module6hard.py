from math import pi, sqrt

class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = color
        self.__sides = sides
        self.filled = bool
        self.set_sides(*sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 < r <= 255 and 0 < g <= 255 and 0 < b <= 255:
            return r, g, b
        else:
            return self.__color

    def set_color(self, r, g, b):
        self.__color = list(self.__is_valid_color(r, g, b))
        return self.__color


    def __is_valid_sides(self, *sides):
        if len(sides) == self.sides_count:
            for i in sides:
                if i > 0 and isinstance(i, int):
                    return True
        else:
            return False

    def get_sides(self):
        return list(self.__sides)

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        self.new_sides = new_sides
        if len(self.new_sides) != self.sides_count:
            pass
        else:
            self.__sides = list(self.new_sides)



class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self._Figure__sides[0] / (2 * pi)

    def get_square(self):
        s = (self.__radius ** 2) * pi
        return s

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides, )


    def get_volume(self):
        V = self._Figure__sides[0] ** 3
        return V


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.sides = sides
        p = (self._Figure__sides[0] + self._Figure__sides[1] + self._Figure__sides[2]) / 2
        self.__height = 2 * (sqrt(p * (p - self._Figure__sides[0]) * (p - self._Figure__sides[1])
        * (p - self._Figure__sides[2]))) / self._Figure__sides[0]


    def get_square(self):
        St = (self.__height * self.sides[0]) / 2
        return St

circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())