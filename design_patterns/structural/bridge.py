# pylint: skip-file


class Color:

    def fill_color(self):
        pass


class Shape:
    def __init__(self, color):
        self.color = color

    def color_it(self):
        pass


class Rectangle(Shape):
    def __init__(self, color):
        super(Rectangle, self).__init__(color)

    def color_it(self):
        print("Rectangle filled with ", end="")
        self.color.fill_color()


class Circle(Shape):
    def __init__(self, color):
        super(Circle, self).__init__(color)

    def color_it(self):
        print("Circle filled with ", end="")
        self.color.fill_color()


class RedColor(Color):
    def fill_color(self):
        print("red color")


class BlueColor(Color):
    def fill_color(self):
        print("blue color")


if __name__ == '__main__':
    s1 = Rectangle(RedColor())
    s1.color_it()

    s2 = Circle(BlueColor())
    s2.color_it()
