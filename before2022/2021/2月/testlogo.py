from manimlib.imports import *
from manim_sandbox.utils.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class testlogo(Scene):

    def construct(self):
# object
        input_triangle_p1 = RegularPolygon(n=3, start_angle=TAU / 4).move_to(UP)
        output_triangle_p1 = RegularPolygon(n=3, start_angle=0).move_to(DOWN)
# position

# show
        self.add(input_triangle_p1,output_triangle_p1)
