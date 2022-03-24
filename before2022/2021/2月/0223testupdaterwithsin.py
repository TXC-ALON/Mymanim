from manimlib.imports import *
from manim_sandbox.utils.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class updaterwithsin(Scene):

    def construct(self):
        # object
        circle = Circle(color=GREEN, stroke_width=8).scale(2)
        dot_o = Dot(ORIGIN, color=GRAY)
        dot_p = Dot(np.sqrt(3) * RIGHT + UP, color=BLUE).set_height(0.2)
        arrow = Line(dot_o, dot_p, color=RED_D, stroke_width=5)
        line_2 = Line(ORIGIN, [dot_p.get_center()[0], 0, 0], color=YELLOW_D, stroke_width=3)
        line_3 = Line([dot_p.get_center()[0], 0, 0], dot_p.get_center(), color=YELLOW_D, stroke_width=3)
        group = VGroup(circle, arrow, line_2, line_3, dot_o, dot_p)

        # position
        def anim(obj, alpha):
            obj[-1].become(Dot(color=BLUE).set_height(0.2)).move_to(circle.point_from_proportion(alpha + 1 / 12))
            obj[1].become(Line(ORIGIN, dot_p, color=RED_D, stroke_width=5))
            obj[2].become(Line(ORIGIN, [dot_p.get_center()[0], 0, 0], color=YELLOW_D, stroke_width=3))
            obj[3].become(Line([dot_p.get_center()[0], 0, 0], dot_p.get_center(), color=YELLOW_D, stroke_width=3))

        # show
        self.add(group)
        self.wait()
        path = TracedPath(dot_p.get_center, stroke_width=6,
                          stroke_color=YELLOW)
        path.add_updater(lambda a: a.shift(RIGHT * 0.04))
        self.add(path)
        self.play(UpdateFromAlphaFunc(group, anim),
                  run_time=6, rate_func=linear)
        self.wait(2)


class updaterwithsin2(DarkScene):
    def construct(self):
        t = ValueTracker(0)
        cir = Circle(radius=1)
        dot_p = Dot().add_updater(lambda a: a.move_to(
            np.array([2 * np.cos(t.get_value()), 2 * np.sin(t.get_value()), 0]))).set_color(YELLOW)
        arrow = Line(cir.get_center(), dot_p, color=RED_D, stroke_width=5).add_updater(
            lambda a: a.become(Line(cir.get_center(), dot_p, color=RED_D, stroke_width=5)))
        line1 = Line(cir.get_center(), [dot_p.get_center()[0], 0, 0], color=YELLOW_D, stroke_width=3).add_updater(
            lambda a: a.become(Line(cir.get_center(), [dot_p.get_center()[0], 0, 0], color=YELLOW_D, stroke_width=3)))
        line2 = Line([dot_p.get_center()[0], 0, 0], dot_p.get_center(), color=YELLOW_D, stroke_width=3).add_updater(
            lambda a: a.become(Line([dot_p.get_center()[0], 0, 0], dot_p.get_center(), color=YELLOW_D, stroke_width=3)))
        dot_q = Dot().add_updater(lambda a: a.move_to(
            np.array([2, 2 * np.sin(t.get_value()), 0])))
        l_pq = DashedLine().add_updater(lambda a: a.put_start_and_end_on(dot_p.get_center(), dot_q.get_center()))
        dot_m = Dot().add_updater(lambda a: a.move_to(
            np.array([2 * np.cos(t.get_value()), -2, 0])))
        l_pm = DashedLine().add_updater(lambda a: a.put_start_and_end_on(
            dot_p.get_center(), dot_m.get_center()))
        path = TracedPath(dot_q.get_center, stroke_width=6,
                          stroke_color=YELLOW)
        path.add_updater(lambda a: a.shift(RIGHT * 0.04))
        path2 = TracedPath(dot_m.get_center, stroke_width=6,
                           stroke_color=BLUE)
        path2.add_updater(lambda a: a.shift(RIGHT * 0.04))
        self.add(cir, dot_p, dot_q, dot_m, l_pq, l_pm, path, path2)
        self.add(arrow, line1, line2)
        self.play(t.set_value, 2 * TAU, run_time=8, rate_func=linear)


class ValueTrackerScene3(DarkScene):
    def construct(self):
        t = ValueTracker(0)
        cir = Circle(radius=1)
        dot_o = Dot().move_to(cir.get_center())
        dot_p = Dot().add_updater(lambda a: a.move_to(
            np.array([np.cos(t.get_value()), np.sin(t.get_value()), 0]))).set_color(PINK)
        dot_q = Dot().add_updater(lambda a: a.move_to(
            np.array([0, np.sin(t.get_value()), 0]))).set_color(YELLOW)
        l_pq = DashedLine().add_updater(lambda a: a.put_start_and_end_on(
            dot_p.get_center(), dot_q.get_center()))

        line1 = Line().add_updater(lambda a: a.put_start_and_end_on(
            dot_o.get_center(), dot_p.get_center())).set_color(ORANGE)
        line2 = Line().add_updater(lambda a: a.put_start_and_end_on(
            dot_o.get_center(), np.array([np.cos(t.get_value()), 0, 0]))).set_color(ORANGE)
        line3 = Line().add_updater(lambda a: a.put_start_and_end_on(
            np.array([1.0000001 * np.cos(t.get_value()), 0, 0]), dot_p.get_center())).set_color(ORANGE)

        dot_m = Dot().add_updater(lambda a: a.move_to(
            np.array([1.0000001 * np.cos(t.get_value()), 0, 0]))).set_color(BLUE_E)
        l_pm = DashedLine().add_updater(lambda a: a.put_start_and_end_on(
            dot_p.get_center(), dot_m.get_center()))
        path = TracedPath(dot_q.get_center, stroke_width=6,
                          stroke_color=YELLOW)
        path.add_updater(lambda a: a.shift(RIGHT * 0.04))
        path2 = TracedPath(dot_m.get_center, stroke_width=6,
                           stroke_color=BLUE)
        path2.add_updater(lambda a: a.shift(UP * 0.04))
        self.add(cir, dot_o, dot_p, dot_q, dot_m, l_pq, l_pm, line1, line2, line3, path, path2)
        self.play(t.set_value, 2 * TAU, run_time=8, rate_func=linear)


class testrotating(DarkScene):
    def construct(self):
        t = ValueTracker(0)
        cir = Circle(radius=1)
        dot_o = Dot().move_to(cir.get_center())
        dot_p_on_cir = Dot().add_updater(lambda a: a.move_to(
            np.array([np.cos(t.get_value()), np.sin(t.get_value()), 0]))).set_color(PINK)
        dot_sin = Dot().add_updater(lambda a: a.move_to(
            np.array([0, np.sin(t.get_value()), 0]))).set_color(YELLOW)

        line1 = Line().add_updater(lambda a: a.put_start_and_end_on(
            dot_o.get_center(), dot_p_on_cir.get_center())).set_color(ORANGE)
        line2 = Line().add_updater(lambda a: a.put_start_and_end_on(
            dot_o.get_center(), np.array([np.cos(t.get_value()), 0, 0]))).set_color(ORANGE)
        line3 = Line().add_updater(lambda a: a.put_start_and_end_on(
            np.array([1.0000001 * np.cos(t.get_value()), 0, 0]), dot_p_on_cir.get_center())).set_color(ORANGE)

        dot_cos = Dot().add_updater(lambda a: a.move_to(
            np.array([1 * np.cos(t.get_value()), 0, 0]))).set_color(BLUE_E)
        l_pm = DashedLine().add_updater(lambda a: a.put_start_and_end_on(
            dot_p_on_cir.get_center(), dot_cos.get_center()))
        path = TracedPath(dot_sin.get_center, stroke_width=6,
                          stroke_color=YELLOW)
        path.add_updater(lambda a: a.shift(RIGHT * 0.04))
        path2 = TracedPath(dot_cos.get_center, stroke_width=6,
                           stroke_color=BLUE)
        path2.add_updater(lambda a: a.shift(UP * 0.04))
        self.add(cir, dot_o, dot_p_on_cir, dot_sin, dot_cos, l_pm, line1, line2, line3, path, path2)
        self.play(t.set_value, 2 * TAU, run_time=8, rate_func=linear)
