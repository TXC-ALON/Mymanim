from manimlib.imports import *
from manim_sandbox.utils.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class rotateing(Scene):

    def construct(self):
# object
        sq1 = Square().set_color(BLUE)
        sq2 = Square().set_color(PINK)
        dot0 = Dot(sq1.get_vertices()[0], color=RED).scale(2)
        dot1 = Dot(sq2.get_vertices()[0], color=GREEN).scale(2)
        vg1 = VGroup(sq1, dot0)
        vg2 = VGroup(sq2, dot1)
# position
        #sq1.move_to(LEFT*2)
        #sq2.move_to(RIGHT * 2)
# show
        self.add(vg1,vg2)
        self.wait()
        self.play(
                Rotating(vg1, about_point = ORIGIN,radians=TAU),
                MRotating(vg2,about_point = ORIGIN, angle=TAU),run_time=5
        )
        self.wait()
        #self.play(MRotating(sq2, radians=TAU),run_time=4)