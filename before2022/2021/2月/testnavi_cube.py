from manimlib.imports import *
from manim_sandbox.utils.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class testnavicube(ThreeDScene):

    def construct(self):
# object
        self.move_camera(phi=75 * DEGREES, theta=-60 * DEGREES, distance=10)
        axes = ThreeDAxes()
        self.add(axes)
        navi_cube = Cube(stroke_color=ORANGE, stroke_width=0.6, fill_color=ORANGE, fill_opacity=0.2).scale(0.1)
        l_cube = navi_cube.get_height()
        navi_cube.shift(l_cube / 2)
        l_x = Line(ORIGIN, l_cube * UP * 4, color=GREEN)
        l_y = Line(ORIGIN, l_cube * OUT * 4, color=PINK)
        l_t = Line(ORIGIN, l_cube * RIGHT * 4, color=ORANGE)
        tex_x = TexMobject('x', background_stroke_color=WHITE, color=GREEN).rotate(PI / 2, RIGHT).next_to(l_x, UP * 1.25)
        tex_y = TexMobject('y', background_stroke_color=WHITE, color=PINK).rotate(PI / 2, RIGHT).next_to(l_y, OUT * 0.5)
        tex_t = TexMobject('t', background_stroke_color=WHITE, color=ORANGE).rotate(PI / 2, RIGHT).next_to(l_t, RIGHT * 0.5)
        navi_group = VGroup(l_x, l_y, l_t, tex_x, tex_y, tex_t, navi_cube).move_to(l_x.points[0])
# position

# show
        self.add(navi_group)
