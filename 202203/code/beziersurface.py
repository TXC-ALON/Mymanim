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

#test the camera and analysis the basic direction
class create_3D_scene_basic(ThreeDScene):
    def construct(self):
        CONFIG = {
            "camera_class": ThreeDCamera
        }
        dot1 = Dot3d(color=BLUE, size=0.15).move_to([1, 0, 0])
        dot2 = Dot3d(color=PINK, size=0.15).move_to([0, 1, 0])
        dot3 = Dot3d(color=ORANGE, size=0.15).move_to([0, 0, 1])
        dot4 = Dot3d(color=PURPLE, size=0.15).move_to([1, 2, 3])
        Dot_group_basic= VGroup(dot1, dot2, dot3, dot4)
        axes = ThreeDAxes(x_range=np.array([-5.0, 5.0, 1.0]),
                          y_range=np.array([-5.0, 5.0, 1.0]),
                          z_range=np.array([-4.0, 4.0, 1.0])
                          )
        self.play(ShowCreation(axes))
        self.wait(1)
        self.play(ShowCreation(Dot_group_basic))
        #他就是吧xoy坐标系简单加个y，，，我说呢
        #self.move_camera(phi=0 * DEGREES, theta=0 * DEGREES, gamma=90 * DEGREES, run_time=1)
        circle = Circle()

        frame = self.camera.frame
        frame.set_euler_angles(theta=0, phi=0, units=RADIANS)
        self.wait(1)
        self.play(ShowCreation(circle))
        self.wait(1)
        self.play(
            # 在过渡期间移动相机帧
            frame.increment_phi, 60 * DEGREES,
            frame.increment_theta, 45 * DEGREES,
            run_time=3
        )


class addthesquare(ThreeDScene):
    def construct(self):
        CONFIG = {
            "camera_class": ThreeDCamera,
        }
        dot1 = Dot3d(color=YELLOW, size=0.15).move_to([1, 0, 0])
        dot2 = Dot3d(color=PINK, size=0.15).move_to([0, 1, 0])
        dot3 = Dot3d(color=ORANGE, size=0.15).move_to([0, 0, 1])
        dot4 = Dot3d(color=PURPLE, size=0.15).move_to([1, 2, 3])
        Dot_group_basic = VGroup(dot1, dot2, dot3, dot4)
        axes = ThreeDAxes(x_range=np.array([-5.0, 5.0, 1.0]),
                          y_range=np.array([-5.0, 5.0, 1.0]),
                          z_range=np.array([-4.0, 4.0, 1.0])
                          )
        self.add(axes,Dot_group_basic)

        dot5 = Dot3d(color=BLUE, size=0.15).move_to([-2, 2, 0])
        dot6 = Dot3d(color=BLUE, size=0.15).move_to([-2, -2, 0])
        dot7 = Dot3d(color=BLUE, size=0.15).move_to([2, 2, 0])
        dot8 = Dot3d(color=BLUE, size=0.15).move_to([2, -2, 0])
        Dot_group1 = VGroup(dot5,dot6,dot7,dot8).set_color(RED_B)
        back_square = Square3D(fill_opacity=1,side_length = 4).set_color('#66CCFF')
        self.play(ShowCreation(back_square))
        frame = self.camera.frame
        frame.set_euler_angles(theta=0, phi=0, units=RADIANS)
        self.play(
            # 在过渡期间移动相机帧
            frame.increment_phi, 60 * DEGREES,
            frame.increment_theta, 45 * DEGREES,
            run_time=3
        )
        self.wait(1)
        self.play(ShowCreation(Dot_group1))
        self.wait(2)



class begining2(ThreeDScene):
    def construct(self):
        CONFIG = {
            "camera_class": ThreeDCamera,
        }
        axes = ThreeDAxes(x_range=np.array([-5.0, 5.0, 1.0]),
                          y_range=np.array([-5.0, 5.0, 1.0]),
                          z_range=np.array([-4.0, 4.0, 1.0])
                          )
        self.add(axes)

        back_square = Square(fill_opacity=0, side_length=6,color = GREY,stroke_width = 0.5)
        #self.play(ShowCreation(back_square))
        #self.wait()
        dot1 = Dot3d(color=BLUE, size=0.15).move_to([1, 1, 0])
        dot2 = Dot3d(color=BLUE, size=0.15).move_to([-1, 1, 0])
        dot3 = Dot3d(color=BLUE, size=0.15).move_to([-1, -1, 0])
        dot4 = Dot3d(color=BLUE, size=0.15).move_to([1, -1, 0])
        dot5 = Dot3d(color=BLUE, size=0.15).move_to([3, 3, 0])
        dot6 = Dot3d(color=BLUE, size=0.15).move_to([-3,3, 0])
        dot7 = Dot3d(color=BLUE, size=0.15).move_to([-3,-3, 0])
        dot8 = Dot3d(color=BLUE, size=0.15).move_to([3,-3, 0])

        dot9 = Dot3d(color=BLUE, size=0.15).move_to([3,1, 0])
        dot10 = Dot3d(color=BLUE, size=0.15).move_to([1,3, 0])
        dot11 = Dot3d(color=BLUE, size=0.15).move_to([-1,3, 0])
        dot12 = Dot3d(color=BLUE, size=0.15).move_to([-3,1, 0])
        dot13 = Dot3d(color=BLUE, size=0.15).move_to([-3,-1, 0])
        dot14 = Dot3d(color=BLUE, size=0.15).move_to([-1,-3, 0])
        dot15 = Dot3d(color=BLUE, size=0.15).move_to([1,-3, 0])
        dot16 = Dot3d(color=BLUE, size=0.15).move_to([3,-1, 0])

        dashline1 = DashedLine(dot5,dot6,stroke_width = 2)
        dashline2 = DashedLine(dot12, dot9,stroke_width = 2)
        dashline3 = DashedLine(dot16, dot13,stroke_width = 2)
        dashline4 = DashedLine(dot8, dot7,stroke_width = 2)
        dashline_group1 = VGroup(dashline1,dashline2,dashline3,dashline4).set_color(ORANGE)
        dashline5 = DashedLine(dot5, dot8,stroke_width = 1.5)
        dashline6 = DashedLine(dot10, dot15,stroke_width = 1.5)
        dashline7 = DashedLine(dot11, dot14,stroke_width = 1.5)
        dashline8 = DashedLine(dot6, dot7,stroke_width = 1.5)
        dashline_group2 = VGroup(dashline5, dashline6, dashline7, dashline8).set_color(GREY)

        Dot_group1 = VGroup(dot1, dot2, dot3, dot4,
                            dot5, dot6, dot7, dot8,
                            dot9, dot10, dot11, dot12,
                            dot13, dot14, dot15, dot16
                            )
        self.play(ShowCreation(Dot_group1),run_time = 0.01)
        self.wait()
        self.play(ShowCreation(dashline_group1))
        self.wait()
        self.play(ShowCreation(dashline_group2))
        frame = self.camera.frame
        frame.set_euler_angles(theta=0, phi=0, units=RADIANS)
        self.play(
            # 在过渡期间移动相机帧
            frame.increment_phi, 60 * DEGREES,
            frame.increment_theta, 45 * DEGREES,
            run_time=3
        )
        self.wait(1)

