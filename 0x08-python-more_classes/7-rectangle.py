#!/usr/bin/python3

"""Rectangle class """


class Rectangle:
    """ Rectangle class """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ init """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >=0")
        else:
            self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=0")
        else:
            self.__height = value

    def area(self):
        """ area method """
        return self._width * self._height

    def perimeter(self):
        """ perimeter method """
        if self._width == 0 or self._height == 0:
            return 0
        else:
            return (self._width * 2) + (self._height * 2)

    def __str__(self):
        """ str method """
        if self._width == 0 or self._height == 0:
            return ""
        else:
            return ((str(self.print_symbol) * self.__width + "\n") *
                    self.__height)[:-1]

    def __repr__(self):
        """ repr method """
        return "Rectangle({}, {})".format(self._width, self._height)

    def __del__(self):
        """ del method """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
