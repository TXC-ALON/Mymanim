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

class test_3d_bezier_3(ThreeDScene):
    def setup(self):
        axes = ThreeDAxes(x_range=np.array([-5.0, 5.0, 1.0]),
                          y_range=np.array([-5.0, 5.0, 1.0]),
                          z_range=np.array([-4.0, 4.0, 1.0])
                          )
        self.add(axes)
        frame = self.camera.frame
        frame.set_euler_angles(theta=45 * DEGREES, phi=60 * DEGREES, units=RADIANS)
        Dot_x = Dot3d(np.array([-3,0,0])).set_color(ORANGE)
        self.add(Dot_x)
        P0 = Dot3d(np.array([-3, 0, 1])).set_color(GREEN)
        P1 = Dot3d(np.array([0, 0, 2])).set_color(PURPLE)
        P2 = Dot3d(np.array([3, 0, 0.5])).set_color(RED_A)
        P = VGroup(P0, P1, P2)

        P0_P1 = Line(P0, P1)
        P1_P2 = Line(P1, P2)
        P_lines = VGroup(P0_P1, P1_P2).set_color(ORANGE)

        t = ValueTracker(0)

        Q0 = Dot3d(color=BLUE).add_updater(
            lambda m: m.move_to((P1.get_center() - P0.get_center()) * t.get_value() + P0.get_center()))
        Q1 = Dot3d(color=BLUE).add_updater(
            lambda m: m.move_to((P2.get_center() - P1.get_center()) * t.get_value() + P1.get_center()))
        Q = VGroup(Q0, Q1)

        Q0_Q1 = Line().add_updater(lambda m: m.put_start_and_end_on(Q0.get_center(), Q1.get_center())).set_color(YELLOW)

        B = Dot3d(color=RED).add_updater(
            lambda m: m.move_to((Q1.get_center() - Q0.get_center()) * t.get_value() + Q0.get_center()))

        path = TracedPath(B.get_center, stroke_width=7, stroke_color=RED)
        label = Text("二次贝塞尔曲线", font="方正清刻本悦宋简体 常规").scale(1.8).set_color(BLACK).shift(DOWN * 3)
        self.add(label)
        self.add(P, P_lines)
        self.add(Q, Q0_Q1)
        self.add(B, path)
        self.wait()
        self.play(t.increment_value, 1, run_time=7, rate_func=linear)
        self.wait()

class test_3d_bezier_4(ThreeDScene):
    def setup(self):
        axes = ThreeDAxes(x_range=np.array([-5.0, 5.0, 1.0]),
                          y_range=np.array([-5.0, 5.0, 1.0]),
                          z_range=np.array([-4.0, 4.0, 1.0])
                          )
        self.add(axes)
        frame = self.camera.frame
        frame.set_euler_angles(theta=45 * DEGREES, phi=60 * DEGREES, units=RADIANS)
        Dot_x = Dot3d(np.array([-3,0,0])).set_color(ORANGE)
        self.add(Dot_x)
        P0 = Dot3d(np.array([-4.0, 0.0, -1.5]))
        P1 = Dot3d(np.array([-2.5, 0.0, 3.0]))
        P2 = Dot3d(np.array([0.0, 0.0, -2.0]))
        P3 = Dot3d(np.array([3.0, 0.0, 1.5]))
        P = VGroup(P0, P1, P2, P3).set_color(PINK)

        P0_P1 = Line(P0, P1)
        P1_P2 = Line(P1, P2)
        P2_P3 = Line(P2, P3)
        P_lines = VGroup(P0_P1, P1_P2, P2_P3).set_color(PINK)

        t = ValueTracker(0)

        Q0 = Dot3d(color=BLUE).add_updater(
            lambda m: m.move_to((P1.get_center() - P0.get_center()) * t.get_value() + P0.get_center()))
        Q1 = Dot3d(color=BLUE).add_updater(
            lambda m: m.move_to((P2.get_center() - P1.get_center()) * t.get_value() + P1.get_center()))
        Q2 = Dot3d(color=BLUE).add_updater(
            lambda m: m.move_to((P3.get_center() - P2.get_center()) * t.get_value() + P2.get_center()))
        Q = VGroup(Q0, Q1, Q2)

        Q0_Q1 = Line().add_updater(lambda m: m.put_start_and_end_on(Q0.get_center(), Q1.get_center()))
        Q1_Q2 = Line().add_updater(lambda m: m.put_start_and_end_on(Q1.get_center(), Q2.get_center()))
        Q_lines = VGroup(Q0_Q1, Q1_Q2).set_color(YELLOW)

        R0 = Dot3d(color=GREEN).add_updater(
            lambda m: m.move_to((Q1.get_center() - Q0.get_center()) * t.get_value() + Q0.get_center()))
        R1 = Dot3d(color=GREEN).add_updater(
            lambda m: m.move_to((Q2.get_center() - Q1.get_center()) * t.get_value() + Q1.get_center()))
        R = VGroup(R0, R1)

        R0_R1 = Line().add_updater(lambda m: m.put_start_and_end_on(R0.get_center(), R1.get_center())).set_color(PURPLE)

        B = Dot3d(color=RED).add_updater(
            lambda m: m.move_to((R1.get_center() - R0.get_center()) * t.get_value() + R0.get_center()))

        path = TracedPath(B.get_center, stroke_width=4, stroke_color=RED)

        label = Text("三次贝塞尔曲线", font="Source Han Serif CN").scale(1.8).set_color(BLACK).shift(DOWN * 3)
        self.add(label)
        self.add(P, P_lines)
        self.add(Q, Q_lines)
        self.add(R, R0_R1)
        self.add(B, path)
        self.wait()
        self.play(t.increment_value, 1, run_time=7, rate_func=linear)
        self.wait()
        self.play(
            # 在过渡期间移动相机帧
            frame.increment_theta, 360 * DEGREES,
            run_time=5
        )
        self.wait(1)

class test_3d_bezier_4minus4(ThreeDScene):
    def setup(self):
        axes = ThreeDAxes(x_range=np.array([-5.0, 5.0, 1.0]),
                          y_range=np.array([-5.0, 5.0, 1.0]),
                          z_range=np.array([-4.0, 4.0, 1.0])
                          )
        self.add(axes)
        frame = self.camera.frame
        frame.set_euler_angles(theta=45 * DEGREES, phi=60 * DEGREES, units=RADIANS)
        Dot_x = Dot3d(np.array([-3,0,0])).set_color(ORANGE)
        self.add(Dot_x)
        P0 = Dot3d(np.array([-3.0, -3.0, -1.5]))
        P1 = Dot3d(np.array([-1.5, -3.0, 2.0]))
        P2 = Dot3d(np.array([1.0, -3.0, -4.0]))
        P3 = Dot3d(np.array([3.0, -3.0, 1.5]))
        P_0 = VGroup(P0, P1, P2, P3).set_color(PINK)

        P01 = Dot3d(np.array([-3.0, -1.0, -1.5]))
        P11 = Dot3d(np.array([-1.0, -1.0, 1.5]))
        P21 = Dot3d(np.array([1.0, -1.0, 0.0]))
        P31 = Dot3d(np.array([3.0, -1.0, -2.5]))
        P_1 = VGroup(P01, P11, P21, P31).set_color(PINK)

        P02 = Dot3d(np.array([-3.0, 1.0, -1.5]))
        P12 = Dot3d(np.array([-1.0, 1.0, 1.0]))
        P22 = Dot3d(np.array([1.0, 1.0, -2.0]))
        P32 = Dot3d(np.array([3.0, 1.0, -1.5]))
        P_2 = VGroup(P02, P12, P22, P32).set_color(PINK)

        P03 = Dot3d(np.array([-3.0, 3.0, -1.5]))
        P13 = Dot3d(np.array([-1.0, 3.0, -1.0]))
        P23 = Dot3d(np.array([1.0, 3.0, 1.0]))
        P33 = Dot3d(np.array([3.0, 3.0, 2]))
        P_3 = VGroup(P03, P13, P23, P33).set_color(PINK)

        P0_P1 = Line(P0, P1)
        P1_P2 = Line(P1, P2)
        P2_P3 = Line(P2, P3)
        P_0_lines = VGroup(P0_P1, P1_P2, P2_P3).set_color(PINK)

        P01_P11 = Line(P01, P11)
        P11_P21 = Line(P11, P21)
        P21_P31 = Line(P21, P31)
        P_1_lines = VGroup(P01_P11, P11_P21, P21_P31).set_color(PINK)

        P02_P12 = Line(P02, P12)
        P12_P22 = Line(P12, P22)
        P22_P32 = Line(P22, P32)
        P_2_lines = VGroup(P02_P12, P12_P22, P22_P32).set_color(PINK)

        P03_P13 = Line(P03, P13)
        P13_P23 = Line(P13, P23)
        P23_P33 = Line(P23, P33)
        P_3_lines = VGroup(P03_P13, P13_P23, P23_P33).set_color(PINK)
        t = ValueTracker(0)

        Q0 = Dot3d(color=BLUE).add_updater(
            lambda m: m.move_to((P1.get_center() - P0.get_center()) * t.get_value() + P0.get_center()))
        Q1 = Dot3d(color=BLUE).add_updater(
            lambda m: m.move_to((P2.get_center() - P1.get_center()) * t.get_value() + P1.get_center()))
        Q2 = Dot3d(color=BLUE).add_updater(
            lambda m: m.move_to((P3.get_center() - P2.get_center()) * t.get_value() + P2.get_center()))
        Q_0 = VGroup(Q0, Q1, Q2)

        Q01 = Dot3d(color=BLUE).add_updater(
            lambda m: m.move_to((P11.get_center() - P01.get_center()) * t.get_value() + P01.get_center()))
        Q11 = Dot3d(color=BLUE).add_updater(
            lambda m: m.move_to((P21.get_center() - P11.get_center()) * t.get_value() + P11.get_center()))
        Q21 = Dot3d(color=BLUE).add_updater(
            lambda m: m.move_to((P31.get_center() - P21.get_center()) * t.get_value() + P21.get_center()))
        Q_1 = VGroup(Q01, Q11, Q21)

        Q02 = Dot3d(color=BLUE).add_updater(
            lambda m: m.move_to((P12.get_center() - P02.get_center()) * t.get_value() + P02.get_center()))
        Q12 = Dot3d(color=BLUE).add_updater(
            lambda m: m.move_to((P22.get_center() - P12.get_center()) * t.get_value() + P12.get_center()))
        Q22 = Dot3d(color=BLUE).add_updater(
            lambda m: m.move_to((P32.get_center() - P22.get_center()) * t.get_value() + P22.get_center()))
        Q_2 = VGroup(Q02, Q12, Q22)

        Q03 = Dot3d(color=BLUE).add_updater(
            lambda m: m.move_to((P13.get_center() - P03.get_center()) * t.get_value() + P03.get_center()))
        Q13 = Dot3d(color=BLUE).add_updater(
            lambda m: m.move_to((P23.get_center() - P13.get_center()) * t.get_value() + P13.get_center()))
        Q23 = Dot3d(color=BLUE).add_updater(
            lambda m: m.move_to((P33.get_center() - P23.get_center()) * t.get_value() + P23.get_center()))
        Q_3 = VGroup(Q03, Q13, Q23)

        Q0_Q1 = Line().add_updater(lambda m: m.put_start_and_end_on(Q0.get_center(), Q1.get_center()))
        Q1_Q2 = Line().add_updater(lambda m: m.put_start_and_end_on(Q1.get_center(), Q2.get_center()))
        Q_lines = VGroup(Q0_Q1, Q1_Q2).set_color(YELLOW)

        Q01_Q11 = Line().add_updater(lambda m: m.put_start_and_end_on(Q01.get_center(), Q11.get_center()))
        Q11_Q21 = Line().add_updater(lambda m: m.put_start_and_end_on(Q11.get_center(), Q21.get_center()))
        Q_1_lines = VGroup(Q01_Q11, Q11_Q21).set_color(YELLOW)

        Q02_Q12 = Line().add_updater(lambda m: m.put_start_and_end_on(Q02.get_center(), Q12.get_center()))
        Q12_Q22 = Line().add_updater(lambda m: m.put_start_and_end_on(Q12.get_center(), Q22.get_center()))
        Q_2_lines = VGroup(Q02_Q12, Q12_Q22).set_color(YELLOW)

        Q03_Q13 = Line().add_updater(lambda m: m.put_start_and_end_on(Q03.get_center(), Q13.get_center()))
        Q13_Q23 = Line().add_updater(lambda m: m.put_start_and_end_on(Q13.get_center(), Q23.get_center()))
        Q_3_lines = VGroup(Q03_Q13, Q13_Q23).set_color(YELLOW)

        R0 = Dot3d(color=GREEN).add_updater(
            lambda m: m.move_to((Q1.get_center() - Q0.get_center()) * t.get_value() + Q0.get_center()))
        R1 = Dot3d(color=GREEN).add_updater(
            lambda m: m.move_to((Q2.get_center() - Q1.get_center()) * t.get_value() + Q1.get_center()))
        R = VGroup(R0, R1)

        R01 = Dot3d(color=GREEN).add_updater(
            lambda m: m.move_to((Q11.get_center() - Q01.get_center()) * t.get_value() + Q01.get_center()))
        R11 = Dot3d(color=GREEN).add_updater(
            lambda m: m.move_to((Q21.get_center() - Q11.get_center()) * t.get_value() + Q11.get_center()))
        R_1 = VGroup(R01, R11)

        R02 = Dot3d(color=GREEN).add_updater(
            lambda m: m.move_to((Q12.get_center() - Q02.get_center()) * t.get_value() + Q02.get_center()))
        R12 = Dot3d(color=GREEN).add_updater(
            lambda m: m.move_to((Q22.get_center() - Q12.get_center()) * t.get_value() + Q12.get_center()))
        R_2 = VGroup(R02, R12)

        R03 = Dot3d(color=GREEN).add_updater(
            lambda m: m.move_to((Q13.get_center() - Q03.get_center()) * t.get_value() + Q03.get_center()))
        R13 = Dot3d(color=GREEN).add_updater(
            lambda m: m.move_to((Q23.get_center() - Q13.get_center()) * t.get_value() + Q13.get_center()))
        R_3 = VGroup(R03, R13)


        R0_R1 = Line().add_updater(lambda m: m.put_start_and_end_on(R0.get_center(), R1.get_center())).set_color(PURPLE)
        R0_R1_1 = Line().add_updater(lambda m: m.put_start_and_end_on(R01.get_center(), R11.get_center())).set_color(PURPLE)
        R0_R1_2 = Line().add_updater(lambda m: m.put_start_and_end_on(R02.get_center(), R12.get_center())).set_color(PURPLE)
        R0_R1_3 = Line().add_updater(lambda m: m.put_start_and_end_on(R03.get_center(), R13.get_center())).set_color(PURPLE)

        B = Dot3d(color=RED).add_updater(
            lambda m: m.move_to((R1.get_center() - R0.get_center()) * t.get_value() + R0.get_center()))
        B_1 = Dot3d(color=RED).add_updater(
            lambda m: m.move_to((R11.get_center() - R01.get_center()) * t.get_value() + R01.get_center()))
        B_2 = Dot3d(color=RED).add_updater(
            lambda m: m.move_to((R12.get_center() - R02.get_center()) * t.get_value() + R02.get_center()))
        B_3 = Dot3d(color=RED).add_updater(
            lambda m: m.move_to((R13.get_center() - R03.get_center()) * t.get_value() + R03.get_center()))
        B_group = VGroup(B,B_1,B_2,B_3)
        self.add(B_group)
        P0_P1E = Line(B, B_1)
        P1_P2E = Line(B_1, B_2)
        P2_P3E = Line(B_2, B_3)
        P_Elines = VGroup(P0_P1E, P1_P2E, P2_P3E).set_color(PINK)

        Q0E = Dot3d(color=BLUE).add_updater(lambda m: m.move_to((B_1.get_center() - B.get_center()) * t.get_value() + B.get_center()))
        Q1E = Dot3d(color=BLUE).add_updater(lambda m: m.move_to((B_2.get_center() - B_1.get_center()) * t.get_value() + B_1.get_center()))
        Q2E = Dot3d(color=BLUE).add_updater(lambda m: m.move_to((B_3.get_center() - B_2.get_center()) * t.get_value() + B_2.get_center()))
        QE = VGroup(Q0E, Q1E, Q2E)

        Q0_Q1E = Line().add_updater(lambda m: m.put_start_and_end_on(Q0E.get_center(), Q1E.get_center()))
        Q1_Q2E = Line().add_updater(lambda m: m.put_start_and_end_on(Q1E.get_center(), Q2E.get_center()))
        Q_linesE = VGroup(Q0_Q1E, Q1_Q2E).set_color(YELLOW)

        R0E = Dot3d(color=GREEN).add_updater(lambda m: m.move_to((Q1E.get_center() - Q0E.get_center()) * t.get_value() + Q0E.get_center()))
        R1E = Dot3d(color=GREEN).add_updater(lambda m: m.move_to((Q2E.get_center() - Q1E.get_center()) * t.get_value() + Q1E.get_center()))
        RE = VGroup(R0E, R1E)

        R0_R1E = Line().add_updater(lambda m: m.put_start_and_end_on(R0E.get_center(), R1E.get_center())).set_color(PURPLE)

        BE = Dot3d(color=RED).add_updater(lambda m: m.move_to((R1E.get_center() - R0E.get_center()) * t.get_value() + R0E.get_center()))

        pathE = TracedPath(BE.get_center, stroke_width=7, stroke_color=GOLD)

        path = TracedPath(B.get_center, stroke_width=4, stroke_color=RED)
        path_1 = TracedPath(B_1.get_center, stroke_width=4, stroke_color=RED)
        path_2 = TracedPath(B_2.get_center, stroke_width=4, stroke_color=RED)
        path_3 = TracedPath(B_3.get_center, stroke_width=4, stroke_color=RED)

        label = Text("三次贝塞尔曲线", font="Source Han Serif CN").scale(1.8).set_color(BLACK).shift(DOWN * 3)
        self.add(label)
        self.add(P_0, P_0_lines)
        self.add(Q_0, Q_lines)
        self.add(R, R0_R1)
        self.add(B, path)

        self.add(P_1, P_1_lines)
        self.add(Q_1, Q_1_lines)
        self.add(R_1, R0_R1_1)
        self.add(B_1, path_1)

        self.add(P_2, P_2_lines)
        self.add(Q_2, Q_2_lines)
        self.add(R_2, R0_R1_2)
        self.add(B_2, path_2)

        self.add(P_3, P_3_lines)
        self.add(Q_3, Q_3_lines)
        self.add(R_3, R0_R1_3)
        self.add(B_3, path_3)

        self.add(B, P_Elines)
        self.add(QE, Q_linesE)
        self.add(RE, R0_R1E)
        self.add(BE, pathE)

        self.wait()
        self.play(t.increment_value, 1, run_time=7, rate_func=linear)
        self.wait()
        self.play(
            # 在过渡期间移动相机帧
            frame.increment_theta, 360 * DEGREES,
            run_time=5
        )
        self.wait(1)

