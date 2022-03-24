from manimlib.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class testsquare(Scene):

    def construct(self):
        # object
        square = Square(side_length=6, color="BlUE")
        self.add(square)
        for point in square.get_points():
            self.add(Dot(point, color="YELLOW"))
        self.wait()


class testCircle(Scene):

    def construct(self):
        # object
        circle = Circle(radius=3, color=BLUE)
        self.add(circle)
        for point in circle.get_points():
            self.add(Dot(point, color="YELLOW"))
        self.wait()
# position

# show
