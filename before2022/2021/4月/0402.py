from manim_sandbox.utils.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class MIcircle(Scene):
    CONFIG = {
        "step_size":0.00001
    }
    def construct(self):
        axes = NumberPlane()
        self.add(axes)
        func1 = FunctionGraph(lambda x: pow(1 + x ** 3, 1 / 3), color=GOLD,x_min = -3,x_max = 3)
        func2 = FunctionGraph(lambda x: pow(1 - x ** 3, 1 / 3), color=RED,x_min = -3,x_max = 3)
        func3 = FunctionGraph(lambda x: -pow(1 + x ** 3, 1 / 3), color=BLUE,x_min = -3,x_max = 3)
        func4 = FunctionGraph(lambda x: -pow(1 - x ** 3, 1 / 3), color=GREEN,x_min = -3,x_max = 3)
        func = VGroup(func1,func2,func3,func4)
        self.play(ShowCreation(func), run_time=5)
class MIcircle2(Scene):

    def construct(self):
        axes = Axes()

        dot = Dot().set_color(YELLOW).move_to(ORIGIN)
        arrow1 = Arrow(ORIGIN,UP)
        self.add(axes,dot,arrow1)
        arrow2 = arrow1.copy()
        arrow2.rotate(PI / 2, about_point = ORIGIN).set_color(RED)
        func1 = FunctionGraph(lambda x: pow(1 + x ** 3, 1 / 3), color=GOLD,x_min = -3,x_max = 3)
        func0 = func1.copy().rotate(PI / 2, ORIGIN).set_color(RED)
        func2 = func1.copy().rotate(PI/2,about_point = ORIGIN).set_color(RED)
        func3 = func1.copy().rotate(2*PI/2,about_point = ORIGIN).set_color(BLUE)
        func4 = func1.copy().rotate(3*PI / 2,about_point = ORIGIN).set_color(GREEN)
        func = VGroup(func1,func2,func3,func4)
        self.play(ShowCreation(func), run_time=2)
        self.play(ReplacementTransform(func1,func0), run_time=2)
        self.play(ReplacementTransform(arrow1, arrow2), run_time=2)
        self.wait(2)

class MIcircle3(Scene):
    def construct(self):
        h = (2 ** (8 / 3) - 4) / 3
        border = VMobject().set_points(np.array([
            [0, 1, 0], [h, 1, 0], [1, h, 0], [1, 0, 0],
            [1, 0, 0], [1, -h, 0], [h, -1, 0], [0, -1, 0],
            [0, -1, 0], [-h, -1, 0], [-1, -h, 0], [-1, 0, 0],
            [-1, 0, 0], [-1, h, 0], [-h, 1, 0], [0, 1, 0]
        ]))
        self.play(ShowCreation(border))
        self.wait()

class TestCubicBezierMI2(Scene):
    def construct(self):
        n = ValueTracker(2)
        h = ValueTracker((2 ** (3 - 1 / n.get_value()) - 4) / 3)
        h.add_updater(lambda a: a.set_value((2 ** (3 - 1 / n.get_value()) - 4) / 3))
        border = VMobject().add_updater(lambda a: a.set_points(2 * np.array([
            [0, 1, 0], [h.get_value(), 1, 0], [1, h.get_value(), 0], [1, 0, 0],
            [1, 0, 0], [1, -h.get_value(), 0], [h.get_value(), -1, 0], [0, -1, 0],
            [0, -1, 0], [-h.get_value(), -1, 0], [-1, -h.get_value(), 0], [-1, 0, 0],
            [-1, 0, 0], [-1, h.get_value(), 0], [-h.get_value(), 1, 0], [0, 1, 0]
        ])))##.set_fill(color=ORANGE, opacity=1,).set_stroke(color=None, width=0.01, opacity=None,
              ##     background=False, family=True)
        text = VGroup(
            TexMobject("n="),
            DecimalNumber(0.)
        ).arrange(RIGHT).to_corner(DR)
        text[1].add_updater(lambda a: a.set_value(n.get_value()))
        self.add(text, h, n)
        self.play(ShowCreation(border))
        self.wait()
        axe = Axes()
        cir = Circle().set_color(GREEN).scale(2)
        self.add(axe,cir)
        self.play(n.set_value, 10, run_time=15, rate_func=linear)
        self.wait()
