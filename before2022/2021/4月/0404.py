# from @鹤翔万里
# video address: https://www.bilibili.com/video/av95502154

from manimlib.imports import *


class LinearBezierCurve(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }

    def construct(self):
        P0 = Dot(np.array([-1.5, 1.5, 0]))
        P1 = Dot(np.array([1.5, -1.5, 0]))
        P = VGroup(P0, P1).set_color(GRAY)

        P0_P1 = Line(P0, P1).set_color(GRAY)

        t = ValueTracker(0)

        B = Dot(color=RED).add_updater(
            lambda m: m.move_to((P1.get_center() - P0.get_center()) * t.get_value() + P0.get_center()))

        path = TracedPath(B.get_center, stroke_width=7, stroke_color=RED)

        label = Text("线性贝塞尔曲线", font="Source Han Serif CN").scale(1.8).set_color(BLACK).shift(DOWN * 3)
        self.add(label)
        self.add(P, P0_P1, B, path)
        self.wait()
        self.play(t.increment_value, 1, run_time=7, rate_func=linear)
        self.wait()


class QuadraticBezierCurve(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }

    def construct(self):
        P0 = Dot(np.array([-3, -1.5, 0]))
        P1 = Dot(np.array([0, 1.5, 0]))
        P2 = Dot(np.array([1.5, -1.5, 0]))
        P = VGroup(P0, P1, P2).set_color(GRAY)

        P0_P1 = Line(P0, P1)
        P1_P2 = Line(P1, P2)
        P_lines = VGroup(P0_P1, P1_P2).set_color(GRAY)

        t = ValueTracker(0)

        Q0 = Dot(color=BLUE).add_updater(
            lambda m: m.move_to((P1.get_center() - P0.get_center()) * t.get_value() + P0.get_center()))
        Q1 = Dot(color=BLUE).add_updater(
            lambda m: m.move_to((P2.get_center() - P1.get_center()) * t.get_value() + P1.get_center()))
        Q = VGroup(Q0, Q1)

        Q0_Q1 = Line().add_updater(lambda m: m.put_start_and_end_on(Q0.get_center(), Q1.get_center())).set_color(YELLOW)

        B = Dot(color=RED).add_updater(
            lambda m: m.move_to((Q1.get_center() - Q0.get_center()) * t.get_value() + Q0.get_center()))

        path = TracedPath(B.get_center, stroke_width=7, stroke_color=RED)

        label = Text("二次贝塞尔曲线", font="Source Han Serif CN").scale(1.8).set_color(BLACK).shift(DOWN * 3)
        self.add(label)
        self.add(P, P_lines)
        self.add(Q, Q0_Q1)
        self.add(B, path)
        self.wait()
        self.play(t.increment_value, 1, run_time=7, rate_func=linear)
        self.wait()


class CubicBezierCurve(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }

    def construct(self):
        P0 = Dot(np.array([-3, -1.5, 0]))
        P1 = Dot(np.array([-3.6, 1.5, 0]))
        P2 = Dot(np.array([0, 1.5, 0]))
        P3 = Dot(np.array([3, -1.5, 0]))
        P = VGroup(P0, P1, P2, P3).set_color(GRAY)

        P0_P1 = Line(P0, P1)
        P1_P2 = Line(P1, P2)
        P2_P3 = Line(P2, P3)
        P_lines = VGroup(P0_P1, P1_P2, P2_P3).set_color(GRAY)

        t = ValueTracker(0)

        Q0 = Dot(color=BLUE).add_updater(
            lambda m: m.move_to((P1.get_center() - P0.get_center()) * t.get_value() + P0.get_center()))
        Q1 = Dot(color=BLUE).add_updater(
            lambda m: m.move_to((P2.get_center() - P1.get_center()) * t.get_value() + P1.get_center()))
        Q2 = Dot(color=BLUE).add_updater(
            lambda m: m.move_to((P3.get_center() - P2.get_center()) * t.get_value() + P2.get_center()))
        Q = VGroup(Q0, Q1, Q2)

        Q0_Q1 = Line().add_updater(lambda m: m.put_start_and_end_on(Q0.get_center(), Q1.get_center()))
        Q1_Q2 = Line().add_updater(lambda m: m.put_start_and_end_on(Q1.get_center(), Q2.get_center()))
        Q_lines = VGroup(Q0_Q1, Q1_Q2).set_color(YELLOW)

        R0 = Dot(color=GREEN).add_updater(
            lambda m: m.move_to((Q1.get_center() - Q0.get_center()) * t.get_value() + Q0.get_center()))
        R1 = Dot(color=GREEN).add_updater(
            lambda m: m.move_to((Q2.get_center() - Q1.get_center()) * t.get_value() + Q1.get_center()))
        R = VGroup(R0, R1)

        R0_R1 = Line().add_updater(lambda m: m.put_start_and_end_on(R0.get_center(), R1.get_center())).set_color(PURPLE)

        B = Dot(color=RED).add_updater(
            lambda m: m.move_to((R1.get_center() - R0.get_center()) * t.get_value() + R0.get_center()))

        path = TracedPath(B.get_center, stroke_width=7, stroke_color=RED)

        label = Text("三次贝塞尔曲线", font="Source Han Serif CN").scale(1.8).set_color(BLACK).shift(DOWN * 3)
        self.add(label)
        self.add(P, P_lines)
        self.add(Q, Q_lines)
        self.add(R, R0_R1)
        self.add(B, path)
        self.wait()
        self.play(t.increment_value, 1, run_time=7, rate_func=linear)
        self.wait()


class FourthOrderBezierCurve(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }

    def construct(self):
        P0 = Dot(np.array([-3.6, -1.5, 0]))
        P1 = Dot(np.array([-4.2, 1.5, 0]))
        P2 = Dot(np.array([0, 1.5, 0]))
        P3 = Dot(np.array([2, -1.5, 0]))
        P4 = Dot(np.array([3, 0.5, 0]))
        P = VGroup(P0, P1, P2, P3, P4).set_color(GRAY)

        P0_P1 = Line(P0, P1)
        P1_P2 = Line(P1, P2)
        P2_P3 = Line(P2, P3)
        P3_P4 = Line(P3, P4)
        P_lines = VGroup(P0_P1, P1_P2, P2_P3, P3_P4).set_color(GRAY)

        t = ValueTracker(0)

        Q0 = Dot(color=BLUE).add_updater(
            lambda m: m.move_to((P1.get_center() - P0.get_center()) * t.get_value() + P0.get_center()))
        Q1 = Dot(color=BLUE).add_updater(
            lambda m: m.move_to((P2.get_center() - P1.get_center()) * t.get_value() + P1.get_center()))
        Q2 = Dot(color=BLUE).add_updater(
            lambda m: m.move_to((P3.get_center() - P2.get_center()) * t.get_value() + P2.get_center()))
        Q3 = Dot(color=BLUE).add_updater(
            lambda m: m.move_to((P4.get_center() - P3.get_center()) * t.get_value() + P3.get_center()))
        Q = VGroup(Q0, Q1, Q2, Q3)

        Q0_Q1 = Line().add_updater(lambda m: m.put_start_and_end_on(Q0.get_center(), Q1.get_center()))
        Q1_Q2 = Line().add_updater(lambda m: m.put_start_and_end_on(Q1.get_center(), Q2.get_center()))
        Q2_Q3 = Line().add_updater(lambda m: m.put_start_and_end_on(Q2.get_center(), Q3.get_center()))
        Q_lines = VGroup(Q0_Q1, Q1_Q2, Q2_Q3).set_color(YELLOW)

        R0 = Dot(color=GREEN).add_updater(
            lambda m: m.move_to((Q1.get_center() - Q0.get_center()) * t.get_value() + Q0.get_center()))
        R1 = Dot(color=GREEN).add_updater(
            lambda m: m.move_to((Q2.get_center() - Q1.get_center()) * t.get_value() + Q1.get_center()))
        R2 = Dot(color=GREEN).add_updater(
            lambda m: m.move_to((Q3.get_center() - Q2.get_center()) * t.get_value() + Q2.get_center()))
        R = VGroup(R0, R1, R2)

        R0_R1 = Line().add_updater(lambda m: m.put_start_and_end_on(R0.get_center(), R1.get_center())).set_color(PURPLE)
        R1_R2 = Line().add_updater(lambda m: m.put_start_and_end_on(R1.get_center(), R2.get_center())).set_color(PURPLE)
        R_lines = VGroup(R0_R1, R1_R2)

        S0 = Dot(color=ORANGE).add_updater(
            lambda m: m.move_to((R1.get_center() - R0.get_center()) * t.get_value() + R0.get_center()))
        S1 = Dot(color=ORANGE).add_updater(
            lambda m: m.move_to((R2.get_center() - R1.get_center()) * t.get_value() + R1.get_center()))
        S = VGroup(S0, S1)

        S0_S1 = Line().add_updater(lambda m: m.put_start_and_end_on(S0.get_center(), S1.get_center())).set_color(GOLD)

        B = Dot(color=RED).add_updater(
            lambda m: m.move_to((S1.get_center() - S0.get_center()) * t.get_value() + S0.get_center()))

        path = TracedPath(B.get_center, stroke_width=7, stroke_color=RED)

        label = Text("四次贝塞尔曲线", font="Source Han Serif CN").scale(1.8).set_color(BLACK).shift(DOWN * 3)
        self.add(label)
        self.add(P, P_lines)
        self.add(Q, Q_lines)
        self.add(R, R_lines)
        self.add(S, S0_S1)
        self.add(B, path)
        self.wait()
        self.play(t.increment_value, 1, run_time=7, rate_func=linear)
        self.wait()


class FifthOrderBezierCurve(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }

    def construct(self):
        P0 = Dot(np.array([-3, -2, 0]))
        P1 = Dot(np.array([-1.5, 2.5, 0]))
        P2 = Dot(np.array([0, -0.5, 0]))
        P3 = Dot(np.array([1.5, 2, 0]))
        P4 = Dot(np.array([3, 0, 0]))
        P5 = Dot(np.array([1.5, -2, 0]))
        P = VGroup(P0, P1, P2, P3, P4, P5).set_color(GRAY)

        P0_P1 = Line(P0, P1)
        P1_P2 = Line(P1, P2)
        P2_P3 = Line(P2, P3)
        P3_P4 = Line(P3, P4)
        P4_P5 = Line(P4, P5)
        P_lines = VGroup(P0_P1, P1_P2, P2_P3, P3_P4, P4_P5).set_color(GRAY)

        t = ValueTracker(0)

        Q0 = Dot(color=BLUE).add_updater(
            lambda m: m.move_to((P1.get_center() - P0.get_center()) * t.get_value() + P0.get_center()))
        Q1 = Dot(color=BLUE).add_updater(
            lambda m: m.move_to((P2.get_center() - P1.get_center()) * t.get_value() + P1.get_center()))
        Q2 = Dot(color=BLUE).add_updater(
            lambda m: m.move_to((P3.get_center() - P2.get_center()) * t.get_value() + P2.get_center()))
        Q3 = Dot(color=BLUE).add_updater(
            lambda m: m.move_to((P4.get_center() - P3.get_center()) * t.get_value() + P3.get_center()))
        Q4 = Dot(color=BLUE).add_updater(
            lambda m: m.move_to((P5.get_center() - P4.get_center()) * t.get_value() + P4.get_center()))
        Q = VGroup(Q0, Q1, Q2, Q3, Q4)

        Q0_Q1 = Line().add_updater(lambda m: m.put_start_and_end_on(Q0.get_center(), Q1.get_center()))
        Q1_Q2 = Line().add_updater(lambda m: m.put_start_and_end_on(Q1.get_center(), Q2.get_center()))
        Q2_Q3 = Line().add_updater(lambda m: m.put_start_and_end_on(Q2.get_center(), Q3.get_center()))
        Q3_Q4 = Line().add_updater(lambda m: m.put_start_and_end_on(Q3.get_center(), Q4.get_center()))
        Q_lines = VGroup(Q0_Q1, Q1_Q2, Q2_Q3, Q3_Q4).set_color(YELLOW)

        R0 = Dot(color=GREEN).add_updater(
            lambda m: m.move_to((Q1.get_center() - Q0.get_center()) * t.get_value() + Q0.get_center()))
        R1 = Dot(color=GREEN).add_updater(
            lambda m: m.move_to((Q2.get_center() - Q1.get_center()) * t.get_value() + Q1.get_center()))
        R2 = Dot(color=GREEN).add_updater(
            lambda m: m.move_to((Q3.get_center() - Q2.get_center()) * t.get_value() + Q2.get_center()))
        R3 = Dot(color=GREEN).add_updater(
            lambda m: m.move_to((Q4.get_center() - Q3.get_center()) * t.get_value() + Q3.get_center()))
        R = VGroup(R0, R1, R2, R3)

        R0_R1 = Line().add_updater(lambda m: m.put_start_and_end_on(R0.get_center(), R1.get_center()))
        R1_R2 = Line().add_updater(lambda m: m.put_start_and_end_on(R1.get_center(), R2.get_center()))
        R2_R3 = Line().add_updater(lambda m: m.put_start_and_end_on(R2.get_center(), R3.get_center()))
        R_lines = VGroup(R0_R1, R1_R2, R2_R3).set_color(PURPLE)

        S0 = Dot(color=ORANGE).add_updater(
            lambda m: m.move_to((R1.get_center() - R0.get_center()) * t.get_value() + R0.get_center()))
        S1 = Dot(color=ORANGE).add_updater(
            lambda m: m.move_to((R2.get_center() - R1.get_center()) * t.get_value() + R1.get_center()))
        S2 = Dot(color=ORANGE).add_updater(
            lambda m: m.move_to((R3.get_center() - R2.get_center()) * t.get_value() + R2.get_center()))
        S = VGroup(S0, S1, S2)

        S0_S1 = Line().add_updater(lambda m: m.put_start_and_end_on(S0.get_center(), S1.get_center()))
        S1_S2 = Line().add_updater(lambda m: m.put_start_and_end_on(S1.get_center(), S2.get_center()))
        S_lines = VGroup(S0_S1, S1_S2).set_color(GOLD)

        T0 = Dot(color=PINK).add_updater(
            lambda m: m.move_to((S1.get_center() - S0.get_center()) * t.get_value() + S0.get_center()))
        T1 = Dot(color=PINK).add_updater(
            lambda m: m.move_to((S2.get_center() - S1.get_center()) * t.get_value() + S1.get_center()))
        T = VGroup(T0, T1)

        T0_T1 = Line().add_updater(lambda m: m.put_start_and_end_on(T0.get_center(), T1.get_center())).set_color(PINK)

        B = Dot(color=RED).add_updater(
            lambda m: m.move_to((T1.get_center() - T0.get_center()) * t.get_value() + T0.get_center()))

        path = TracedPath(B.get_center, stroke_width=7, stroke_color=RED)

        label = Text("五次贝塞尔曲线", font="Source Han Serif CN").scale(1.8).set_color(BLACK).shift(DOWN * 3)
        self.add(label)
        self.add(P, P_lines)
        self.add(Q, Q_lines)
        self.add(R, R_lines)
        self.add(S, S_lines)
        self.add(T, T0_T1)
        self.add(B, path)
        self.wait()
        self.play(t.increment_value, 1, run_time=7, rate_func=linear)
        self.wait()


class eigthOrderBezierCurve(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }

    def construct(self):
        P0 = Dot(np.array([-3, -2, 0]))
        P1 = Dot(np.array([-2.5, 2.5, 0]))
        P2 = Dot(np.array([-1, -1, 0]))
        P3 = Dot(np.array([0.5, 2.5, 0]))
        P4 = Dot(np.array([1, -1, 0]))
        P5 = Dot(np.array([1.5, -2, 0]))
        P6 = Dot(np.array([2.5, -2, 0]))
        P7 = Dot(np.array([3, -1, 0]))
        P8 = Dot(np.array([4, 3, 0]))
        P = VGroup(P0, P1, P2, P3, P4, P5, P6, P7, P8).set_color(GRAY)

        P0_P1 = Line(P0, P1)
        P1_P2 = Line(P1, P2)
        P2_P3 = Line(P2, P3)
        P3_P4 = Line(P3, P4)
        P4_P5 = Line(P4, P5)
        P5_P6 = Line(P5, P6)
        P6_P7 = Line(P6, P7)
        P7_P8 = Line(P7, P8)
        P_lines = VGroup(P0_P1, P1_P2, P2_P3, P3_P4, P4_P5, P5_P6, P6_P7, P7_P8).set_color(GRAY)

        t = ValueTracker(0)

        Q0 = Dot(color=BLUE).add_updater(
            lambda m: m.move_to((P1.get_center() - P0.get_center()) * t.get_value() + P0.get_center()))
        Q1 = Dot(color=BLUE).add_updater(
            lambda m: m.move_to((P2.get_center() - P1.get_center()) * t.get_value() + P1.get_center()))
        Q2 = Dot(color=BLUE).add_updater(
            lambda m: m.move_to((P3.get_center() - P2.get_center()) * t.get_value() + P2.get_center()))
        Q3 = Dot(color=BLUE).add_updater(
            lambda m: m.move_to((P4.get_center() - P3.get_center()) * t.get_value() + P3.get_center()))
        Q4 = Dot(color=BLUE).add_updater(
            lambda m: m.move_to((P5.get_center() - P4.get_center()) * t.get_value() + P4.get_center()))
        Q5 = Dot(color=BLUE).add_updater(
            lambda m: m.move_to((P6.get_center() - P5.get_center()) * t.get_value() + P5.get_center()))
        Q6 = Dot(color=BLUE).add_updater(
            lambda m: m.move_to((P7.get_center() - P6.get_center()) * t.get_value() + P6.get_center()))
        Q7 = Dot(color=BLUE).add_updater(
            lambda m: m.move_to((P8.get_center() - P7.get_center()) * t.get_value() + P7.get_center()))
        Q = VGroup(Q0, Q1, Q2, Q3, Q4, Q5, Q6, Q7)

        Q0_Q1 = Line().add_updater(lambda m: m.put_start_and_end_on(Q0.get_center(), Q1.get_center()))
        Q1_Q2 = Line().add_updater(lambda m: m.put_start_and_end_on(Q1.get_center(), Q2.get_center()))
        Q2_Q3 = Line().add_updater(lambda m: m.put_start_and_end_on(Q2.get_center(), Q3.get_center()))
        Q3_Q4 = Line().add_updater(lambda m: m.put_start_and_end_on(Q3.get_center(), Q4.get_center()))
        Q4_Q5 = Line().add_updater(lambda m: m.put_start_and_end_on(Q4.get_center(), Q5.get_center()))
        Q5_Q6 = Line().add_updater(lambda m: m.put_start_and_end_on(Q5.get_center(), Q6.get_center()))
        Q6_Q7 = Line().add_updater(lambda m: m.put_start_and_end_on(Q6.get_center(), Q7.get_center()))
        Q_lines = VGroup(Q0_Q1, Q1_Q2, Q2_Q3, Q3_Q4, Q4_Q5, Q5_Q6, Q6_Q7).set_color(YELLOW)

        R0 = Dot(color=GREEN).add_updater(
            lambda m: m.move_to((Q1.get_center() - Q0.get_center()) * t.get_value() + Q0.get_center()))
        R1 = Dot(color=GREEN).add_updater(
            lambda m: m.move_to((Q2.get_center() - Q1.get_center()) * t.get_value() + Q1.get_center()))
        R2 = Dot(color=GREEN).add_updater(
            lambda m: m.move_to((Q3.get_center() - Q2.get_center()) * t.get_value() + Q2.get_center()))
        R3 = Dot(color=GREEN).add_updater(
            lambda m: m.move_to((Q4.get_center() - Q3.get_center()) * t.get_value() + Q3.get_center()))
        R4 = Dot(color=GREEN).add_updater(
            lambda m: m.move_to((Q5.get_center() - Q4.get_center()) * t.get_value() + Q4.get_center()))
        R5 = Dot(color=GREEN).add_updater(
            lambda m: m.move_to((Q6.get_center() - Q5.get_center()) * t.get_value() + Q5.get_center()))
        R6 = Dot(color=GREEN).add_updater(
            lambda m: m.move_to((Q7.get_center() - Q6.get_center()) * t.get_value() + Q6.get_center()))
        R = VGroup(R0, R1, R2, R3, R4, R5, R6)

        R0_R1 = Line().add_updater(lambda m: m.put_start_and_end_on(R0.get_center(), R1.get_center()))
        R1_R2 = Line().add_updater(lambda m: m.put_start_and_end_on(R1.get_center(), R2.get_center()))
        R2_R3 = Line().add_updater(lambda m: m.put_start_and_end_on(R2.get_center(), R3.get_center()))
        R3_R4 = Line().add_updater(lambda m: m.put_start_and_end_on(R3.get_center(), R4.get_center()))
        R4_R5 = Line().add_updater(lambda m: m.put_start_and_end_on(R4.get_center(), R5.get_center()))
        R5_R6 = Line().add_updater(lambda m: m.put_start_and_end_on(R5.get_center(), R6.get_center()))
        R_lines = VGroup(R0_R1, R1_R2, R2_R3, R3_R4, R4_R5, R5_R6).set_color(PURPLE)

        S0 = Dot(color=ORANGE).add_updater(
            lambda m: m.move_to((R1.get_center() - R0.get_center()) * t.get_value() + R0.get_center()))
        S1 = Dot(color=ORANGE).add_updater(
            lambda m: m.move_to((R2.get_center() - R1.get_center()) * t.get_value() + R1.get_center()))
        S2 = Dot(color=ORANGE).add_updater(
            lambda m: m.move_to((R3.get_center() - R2.get_center()) * t.get_value() + R2.get_center()))
        S3 = Dot(color=ORANGE).add_updater(
            lambda m: m.move_to((R4.get_center() - R3.get_center()) * t.get_value() + R3.get_center()))
        S4 = Dot(color=ORANGE).add_updater(
            lambda m: m.move_to((R5.get_center() - R4.get_center()) * t.get_value() + R4.get_center()))
        S5 = Dot(color=ORANGE).add_updater(
            lambda m: m.move_to((R6.get_center() - R5.get_center()) * t.get_value() + R5.get_center()))
        S = VGroup(S0, S1, S2, S3, S4, S5)

        S0_S1 = Line().add_updater(lambda m: m.put_start_and_end_on(S0.get_center(), S1.get_center()))
        S1_S2 = Line().add_updater(lambda m: m.put_start_and_end_on(S1.get_center(), S2.get_center()))
        S2_S3 = Line().add_updater(lambda m: m.put_start_and_end_on(S2.get_center(), S3.get_center()))
        S3_S4 = Line().add_updater(lambda m: m.put_start_and_end_on(S3.get_center(), S4.get_center()))
        S4_S5 = Line().add_updater(lambda m: m.put_start_and_end_on(S4.get_center(), S5.get_center()))
        S_lines = VGroup(S0_S1, S1_S2, S2_S3, S3_S4, S4_S5).set_color(GOLD)

        T0 = Dot(color=PINK).add_updater(
            lambda m: m.move_to((S1.get_center() - S0.get_center()) * t.get_value() + S0.get_center()))
        T1 = Dot(color=PINK).add_updater(
            lambda m: m.move_to((S2.get_center() - S1.get_center()) * t.get_value() + S1.get_center()))
        T2 = Dot(color=PINK).add_updater(
            lambda m: m.move_to((S3.get_center() - S2.get_center()) * t.get_value() + S2.get_center()))
        T3 = Dot(color=PINK).add_updater(
            lambda m: m.move_to((S4.get_center() - S3.get_center()) * t.get_value() + S3.get_center()))
        T4 = Dot(color=PINK).add_updater(
            lambda m: m.move_to((S5.get_center() - S4.get_center()) * t.get_value() + S4.get_center()))
        T = VGroup(T0, T1, T2, T3, T4)

        T0_T1 = Line().add_updater(lambda m: m.put_start_and_end_on(T0.get_center(), T1.get_center())).set_color(PINK)
        T1_T2 = Line().add_updater(lambda m: m.put_start_and_end_on(T1.get_center(), T2.get_center())).set_color(PINK)
        T2_T3 = Line().add_updater(lambda m: m.put_start_and_end_on(T2.get_center(), T3.get_center())).set_color(PINK)
        T3_T4 = Line().add_updater(lambda m: m.put_start_and_end_on(T3.get_center(), T4.get_center())).set_color(PINK)
        T_lines = VGroup(T0_T1, T1_T2, T2_T3, T3_T4).set_color(MAROON_A)

        B0 = Dot(color=RED).add_updater(
            lambda m: m.move_to((T1.get_center() - T0.get_center()) * t.get_value() + T0.get_center()))
        B1 = Dot(color=RED).add_updater(
            lambda m: m.move_to((T2.get_center() - T1.get_center()) * t.get_value() + T1.get_center()))
        B2 = Dot(color=RED).add_updater(
            lambda m: m.move_to((T3.get_center() - T2.get_center()) * t.get_value() + T2.get_center()))
        B3 = Dot(color=RED).add_updater(
            lambda m: m.move_to((T4.get_center() - T3.get_center()) * t.get_value() + T3.get_center()))
        B = VGroup(B0, B1, B2, B3)

        B0_B1 = Line().add_updater(lambda m: m.put_start_and_end_on(B0.get_center(), B1.get_center())).set_color(RED)
        B1_B2 = Line().add_updater(lambda m: m.put_start_and_end_on(B1.get_center(), B2.get_center())).set_color(RED)
        B2_B3 = Line().add_updater(lambda m: m.put_start_and_end_on(B2.get_center(), B3.get_center())).set_color(RED)
        B_lines = VGroup(B0_B1,B1_B2,B2_B3).set_color(DARK_GREY)

        M0 = Dot(color=YELLOW_B).add_updater(
            lambda m: m.move_to((B1.get_center() - B0.get_center()) * t.get_value() + B0.get_center()))
        M1 = Dot(color=YELLOW_B).add_updater(
            lambda m: m.move_to((B2.get_center() - B1.get_center()) * t.get_value() + B1.get_center()))
        M2 = Dot(color=YELLOW_B).add_updater(
            lambda m: m.move_to((B3.get_center() - B2.get_center()) * t.get_value() + B2.get_center()))
        M = VGroup(M0,M1,M2)

        M0_M1 = Line().add_updater(lambda m: m.put_start_and_end_on(M0.get_center(), M1.get_center())).set_color(BLUE_B)
        M1_M2 = Line().add_updater(lambda m: m.put_start_and_end_on(M1.get_center(), M2.get_center())).set_color(BLUE_B)
        M_lines = VGroup(M0_M1,M1_M2).set_color(TEAL_B)

        l0 = Dot(color=PURPLE_B).add_updater(
            lambda m: m.move_to((M1.get_center() - M0.get_center()) * t.get_value() + M0.get_center()))
        l1 = Dot(color=PURPLE_B).add_updater(
            lambda m: m.move_to((M2.get_center() - M1.get_center()) * t.get_value() + M1.get_center()))
        l = VGroup(l0,l1)

        l0_l1 = Line().add_updater(lambda m: m.put_start_and_end_on(l0.get_center(), l1.get_center())).set_color(LIGHT_GREY)

        final = Dot(color=RED).add_updater(
            lambda m: m.move_to((l1.get_center() - l0.get_center()) * t.get_value() + l0.get_center()))
        path = TracedPath(final.get_center, stroke_width=7, stroke_color=RED_E)

        label = Text("八次贝塞尔曲线", font="Source Han Serif CN").scale(1.8).set_color(BLACK).shift(DOWN * 3)
        self.add(label)
        self.add(P, P_lines)
        self.add(Q, Q_lines)
        self.add(R, R_lines)
        self.add(S, S_lines)
        self.add(T, T_lines)
        self.add(B, B_lines)
        self.add(M,M_lines)
        self.add(l,l0_l1)
        self.add(final,path)
        self.wait()
        self.play(t.increment_value, 1, run_time=7, rate_func=linear)
        self.wait()
