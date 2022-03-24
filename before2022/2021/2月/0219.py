# from big_ol_pile_of_manim_imports import*
from manimlib.imports import *
# from manimlib.debug import *
import numpy as np


class triangle(GraphScene):
    CONFIG = {
        "start_x": 0.5,
        "big_x": 5,
        "dx": 0.001,
        "x_min": -3,
        "x_max": 9,
        "y_min": -3,
        "y_tick_frequency": 1,
        "y_max": 6,
        "x_labeled_nums": list(range(-1, 1, 1)),
        "y_labeled_nums": list(range(-1, 1, 1)),
        "graph_origin": 1 * DOWN + 2 * LEFT,  # 设置调整坐标轴的选项
    }

    def construct(self):
        self.draw_graph()
        # self.show_move()
        # self.emphmax()

    def draw_graph(self):
        func = lambda x: np.log(2 * x) - 1 / 2 * x + 5
        self.setup_axes(animate=True)
        graph = self.get_graph(func, x_min=0.01, color=RED, step_size=0.001)

        func_label = TexMobject(r"f(x)=\ln (2x)-\frac12 x+5").scale(0.5)
        func_label.next_to(graph, direction=LEFT, buff=LARGE_BUFF)

        self.graph = graph
        self.func = func

        dotA = Dot(self.coords_to_point(1, 0), color=BLUE)
        dotB = Dot(self.coords_to_point(5, 0), color=BLUE)
        dotC = Dot(point=self.coords_to_point(self.start_x, func(self.start_x)), color=BLUE)

        self.dotA = dotA.set_plot_depth(1)
        self.dotB = dotB.set_plot_depth(1)
        self.dotC = dotC.set_plot_depth(1)
        c_controller = ValueTracker(self.start_x)
        self.dotC.add_updater(lambda d: d.move_to(self.coords_to_point(c_controller.get_value(), func(c_controller.get_value()))))
        triangle = self.get_triangle().add_updater(lambda tri: [
            self.dotC.move_to(self.coords_to_point(c_controller.get_value(), func(c_controller.get_value()))),
            tri.become(self.get_triangle())])
        labelgroup = self.get_point_label().add_updater(
            lambda l, dt: l[2].next_to(self.dotC, direction=RIGHT, buff=SMALL_BUFF))

        self.play(
            ShowCreation(graph),
            Write(func_label),
            rate_func=smooth
        )
        self.play(
            FadeInFromDown(dotA),
            FadeInFromDown(dotB),
            FadeInFromDown(dotC),
            rate_func=smooth
        )
        self.wait()

        self.play(Write(labelgroup))
        self.wait()
        self.play(ShowCreation(triangle))
        self.wait()
        self.play(c_controller.set_value, 8, rate_func=there_and_back, run_time=8)
        self.wait()

    def get_point_label(self):
        labelgroup = VGroup()

        labelA = TextMobject("A").scale(0.5)
        labelA.next_to(self.dotA, direction=UL * 0.75, buff=SMALL_BUFF)

        labelB = TextMobject("B").scale(0.5)
        labelB.next_to(self.dotB, direction=UP, buff=SMALL_BUFF)

        labelC = TextMobject("C").scale(0.5)
        labelC.next_to(self.dotC, direction=RIGHT, buff=SMALL_BUFF)

        labelgroup.add(labelA, labelB, labelC)

        return labelgroup

    def get_triangle(self):
        triangle = Polygon(self.dotA.get_center(), self.dotB.get_center(), self.dotC.get_center(),
                           stroke_width=2, stroke_color=WHITE, fill_opacity=0.6, fill_color=PINK)

        return triangle

from manimlib.imports import *
from manim_sandbox.utils.imports import *


class _2020To2021(Scene):
    def construct(self):
        color_list = [RED, GOLD, GREEN, BLUE]
        text = TextMobject("2020").scale(12).set_color_by_gradient(color_list)
        ind = AllPointsIndex(text, scale_factor=0.4, color=WHITE)
        ind.add_updater(lambda a: a.become(
            AllPointsIndex(text, scale_factor=0.4, color=WHITE)
        ))
        self.add(text, ind)
        self.wait(2)
        self.play(text.become,
                  TextMobject("2021").scale(12).set_color_by_gradient(color_list))
        self.wait(2)

        current = {"time": 2020,
                   "diligence": 998244353,
                   "caption": Text("2020")
                   }
        dt = 1

        def future(day):
            day.time += dt
            day.diligence += dt * 100
            day.caption.become(
                Text("2021")
            )

        self.play(UpdateFromFunc(current, future))

#         code_str = """past=Text("2020")
# def anim(obj, alpha):
#     obj.become(Text("2021"))
# self.play(UpdateFromAlphaFunc(past, anim))"""
#         code = CodeLine(code_str)
#         self.add(code)

from manimlib.imports import *
from manim_sandbox.utils.imports import *


class fraction(NewGraphScene):

    def construct(self):
        # graph_origin=np.array([-4, -2.5, 0])
        self.y_max = 5
        self.y_min = -1
        self.y_axis_height = 6
        self.x_min = -1
        self.x_max = 9
        self.x_axis_width = 10
        self.setup_axes(animate=True)

        def func(z, ita):
            f = 2
            for i in range(int(ita)-1, 1, -1):
                f = 2+(z-1)/f
            return 1+(z-1)/f

        sqrt_graph = ParametricFunction(lambda t: [t-4, np.sqrt(t)-2.5, 0], t_min=0, t_max=9, color=WHITE,
                                        stroke_width=18, stroke_opacity=0.3).set_plot_depth(-1)
        graph = ParametricFunction(
            lambda t: [t-4, func(t, 2)-2.5, 0], t_min=0, t_max=9, color=BLUE)
        self.play(ShowCreation(graph), ShowCreation(sqrt_graph))
        formula_01 = TexMobject(r"y=1+{x-1\over 2}").to_corner(UR)
        self.play(Write(formula_01))
        self.wait()
        formula = [
            r"y=1+\displaystyle{x-1\over {2+\displaystyle{x-1\over 2}}}",
            r"y=1+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over 2}}}}}",
            r"y=1+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over 2}}}}}}}}",
            r"y=1+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over 2}}}}}}}}}}",
            r"y=1+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over 2}}}}}}}}}}}}",
            r"y=1+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\ddots}}}}}}}}}}}}}",
        ]
        formula_group = VGroup(*[
            TexMobject(tex).to_corner(UR) for tex in formula
        ])
        graph_group = VGroup(*[
            ParametricFunction(
                lambda t: [t - 4, func(t, i) - 2.5, 0], t_min=0, t_max=9, color=BLUE)
            for i in range(3, 11)
        ]
        )
        for i in range(5):
            self.play(Transform(graph, graph_group[i]),
                      Transform(formula_01, formula_group[i]))
            self.wait()
        self.play(ReplacementTransform(graph, graph_group[-1]),
                  ReplacementTransform(formula_01, formula_group[-1]))
        self.wait()
        sq_y = TexMobject(r"\sqrt{x}").move_to(
            formula_group[-1][0][0].get_center()+LEFT*0.2+UP*0.1)
        self.play(ReplacementTransform(formula_group[-1][0][0], sq_y))
        self.wait()

class BGPic(Scene):
    def construct(self):
        rect = Rectangle(width=50, height=FRAME_HEIGHT/2, fill_opacity=1)
        rect.set_color([RED, ORANGE, YELLOW, TEAL, BLUE, "#0000ff"])
        rect.set_sheen_direction(DOWN)
        self.add(rect)

