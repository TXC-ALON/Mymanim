from manimlib.imports import *
from manim_sandbox.utils.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class testcammera(ThreeDScene):

    def construct(self):
# object
        axes = ThreeDAxes()
        dot = Dot([1.0, 2.0, 0.0]).set_stroke(RED, 5)
        self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES)
        x = TextMobject("x").set_color(BLUE).scale(2).move_to([4.0, 0.0, 0.0])
        y = TextMobject("y").set_color(RED).scale(2).move_to([0.0, 4.0, 0.0])
        z = TextMobject("z").set_color(PINK).scale(2).move_to([0.0, 0.0, 4.0])
        labels = VGroup(x,y,z)
        text3d = TextMobject("This is a 3D text").scale(2).set_shade_in_3d(True)
        text3d.rotate(PI / 2, axis=[1, 1, 0])
        self.add(axes, dot, text3d,labels)
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, distance=10, run_time=3)
        self.wait()
        self.move_camera(phi=-90 * DEGREES, theta=-90 * DEGREES, distance=10, run_time=3)
        self.wait()
# position

# show

