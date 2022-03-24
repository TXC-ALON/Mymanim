from manim_sandbox.utils.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class MIcircle3(Scene):
    def construct(self):
        dot_list = [np.array([3., 0., 0.]), np.array([2.42705098, 1.76335576, 0.]),
                    np.array([0.92705098, 2.85316955, 0.]), np.array([0.92705098, 2.85316955, 0.]),
                    np.array([-0.92705098, 2.85316955, 0.]), np.array([-2.42705098, 1.76335576, 0.]),
                    np.array([-3.0000000e+00, 3.6739404e-16, 0.0000000e+00]),
                    np.array([-3.0000000e+00, 3.6739404e-16, 0.0000000e+00]), np.array([-2.42705098, -1.76335576, 0.]),
                    np.array([-0.92705098, -2.85316955, 0.]), np.array([0.92705098, -2.85316955, 0.]),
                    np.array([0.92705098, -2.85316955, 0.]), np.array([2.42705098, -1.76335576, 0.])]
        listlen = len(dot_list)
        dotgroup = VGroup()  # dot group
        line_inner = VGroup()
        line_group_vertical = VGroup()
        line_group_horizontal = VGroup()
        for i in range(listlen):
            dotgroup.add(Dot(dot_list[i], color=YELLOW_E).scale(0.5))
            line_inner.add(DashedLine(ORIGIN, Dot(dot_list[i], color=YELLOW_E)).set_stroke(width=0.8))
            line_group_vertical.add(
                Line(np.array([dot_list[i][0], 4, 0]), np.array([dot_list[i][0], -4, 0]), color=BLUE).set_stroke(
                    width=0.7))
            line_group_vertical.add(
                Line(np.array([-4, dot_list[i][1], 0]), np.array([4, dot_list[i][1], 0]), color=PINK).set_stroke(
                    width=0.7))
        cir = Circle().scale(3).set_color(GREEN)
        self.add(cir)
        self.play(ShowCreation(dotgroup))
        self.play(ShowCreation(line_inner))
        self.wait()
        self.play(ShowCreation(line_group_vertical))
        self.wait()
        self.play(ShowCreation(line_group_horizontal))
        self.wait()
class MIcircle_nequal2p5(DarkScene):
    def construct(self):
        a = 1
        b = 1
        m = 2.5
        n = 2.5
        t = ValueTracker(0)
        dot = Dot(color=YELLOW, background_stroke_color=WHITE, background_stroke_width=2, radius=0.05)
        dot.add_updater(lambda dot: dot.move_to(
            2*np.array([
                pow(abs(np.cos(t.get_value())),2/m)*a*np.sign(np.cos(t.get_value())),
                pow(abs(np.sin(t.get_value())),2/n)*b*np.sign(np.sin(t.get_value())),
                0])))
        path = TracedPath(dot.get_center, stroke_color=RED, stroke_width=4)
        self.add(path)
        self.play(Write(dot))
        self.wait()
        self.play(t.set_value, 2 * PI, run_time=5, rate_func=linear)
        self.wait(3)