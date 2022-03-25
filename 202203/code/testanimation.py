from manimlib import *
import numpy as np

class Dot3d(VGroup):
    def __init__(self, loc=ORIGIN, size=0.2, color=WHITE, **kwargs):
        VGroup.__init__(self, **kwargs)
        dot_01 = Dot(loc, color=color).set_height(size)
        self.add(dot_01)
        num = 8
        for i in range(1, num):
            dot_i = dot_01.copy().rotate(PI * i / num, axis=UP)
            self.add(dot_i)
        for i in range(1, num):
            dot_i = dot_01.copy().rotate(PI * i / num, axis=RIGHT)
            self.add(dot_i)

class Square(Scene):
    def setup(self):
        square = Rectangle(fill_opacity=1,length = 3,width = 4,color = RED,stroke_color = BLUE,opacity = 0.5)#.set_color(RED)
        self.play(DrawBorderThenFill(square))
        self.remove(square)
        self.play(ShowCreation(square))
class Dashline(Scene):
    def setup(self):
        dot0 = Dot(color = RED,size = 0.1).move_to([0,0,0])
        dot4 = Dot(color=BLUE, size=0.15).move_to([-1, -1, 0])
        dot5 = Dot(color=BLUE, size=0.15).move_to([3, 1, 0])
        dot = VGroup(dot0,dot5,dot4)
        #line = DashedLine(np.array([-1,-2,0]),np.array([3,4,0]))
        line = DashedLine(dot5,dot4)
        self.play(ShowCreation(dot))
        self.wait()
        self.play(ShowCreation(line))

class dotmovement_3D(ThreeDScene):
    def setup(self):
        dot0 = Dot3d(color=RED, size=0.1).move_to([0, 0, 0])
        dot1 = Dot3d(color=BLUE, size=0.15).move_to([1, 0, 0])
        dot2 = Dot3d(color=YELLOW, size=0.15).move_to([0, 1, 3])
        dot = VGroup(dot0,dot1)
        axes = ThreeDAxes(x_range=np.array([-5.0, 5.0, 1.0]),
                          y_range=np.array([-5.0, 5.0, 1.0]),
                          z_range=np.array([-4.0, 4.0, 1.0])
                          )
        frame = self.camera.frame
        frame.set_euler_angles(theta=45 * DEGREES, phi=60 * DEGREES, units=RADIANS)
        self.add(axes)
        self.wait()
        self.play(ShowCreation(dot))
        self.wait()
        self.play(Transform(dot1,dot2))
        self.wait()


