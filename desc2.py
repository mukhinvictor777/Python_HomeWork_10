"""
Создать не менее двух дескрипторов для атрибутов классов, которые вы создали ранее в ДЗ
"""


class Road:

    thickness = 5
    weight = 25

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        try:
            int(value)
        except ValueError:
            raise ValueError("Ширина дорожного полотна должна быть числом не меньше 10")
        if value < 10:
            raise ValueError("Ширина дорожного полотна должна быть числом не меньше 10")
        self.__width = value

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        try:
            int(value)
        except ValueError:
            raise ValueError("Длина дорожного полотна должна быть числом не меньше 100")
        if value < 100:
            raise ValueError("Длина дорожного полотна должна быть числом не меньше 100")
        self.__length = value

    def asphalt_weight(self, length, width):
        if not length:
            length = self.__length
        if not width:
            width = self.__width
        asphalt_weight = int(length) * int(width) * self.weight * self.thickness
        print(f'\nМасса асфальта для покрытия дорожного полотна длиной {length} метров и шириной {width} метров ' 
              f'равна {asphalt_weight//1000} т')


example_road = Road('5000', '20')
print(example_road.width)
print(example_road.length)
print()
example_road.width = -11
example_road.length = 95
print(example_road.width)
print(example_road.length)
print()
example_road.asphalt_weight('', '')
example_road.asphalt_weight(10000, 50)
