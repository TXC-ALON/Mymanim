from manimlib.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L
def debugTeX(self, texm):
    for i, j in enumerate(texm):
        tex_id = Text(str(i), font="Euclid").scale(0.5).set_color(RED)
        tex_id.move_to(j)
        self.add(tex_id)


class testLatex(Scene):
    def construct(self):
        tex = TexMobject("\\int_{b}^{a} \\sin x\\cos x\\frac{\\mathrm{d} y}{\\mathrm{d} x}")
        tex.scale(3)
        self.play(ShowCreation(tex))
        self.add(tex)
        debugTeX(self, tex[0])
        # 妈的自己试了半天结果就是一个【0】！！！cao
        self.wait(3)


def Range(in_val, end_val, step=1):
    return list(np.arange(in_val, end_val + step, step))


class Plot(GraphScene):
    CONFIG = {
        "y_max": 50,
        "y_min": 0,
        "x_max": 7,
        "x_min": 0,
        "y_tick_frequency": 10,
        "x_tick_frequency": 0.5,
        "axes_color": BLUE,
    }

    def construct(self):
        self.setup_axes()
        graph = self.get_graph(lambda x: x ** 2, color=GREEN)

        self.play(
            ShowCreation(graph),
            run_time=2
        )
        self.wait()

    def setup_axes(self):
        GraphScene.setup_axes(self)
        self.x_axis.label_direction = UP
        # Additional parametters
        init_val_x = 0
        step_x = 0.5
        end_val_x = 7
        # Position of labels
        values_decimal_x = Range(init_val_x, end_val_x, step_x)
        # List of labels
        list_x = [*["%.1f" % i for i in values_decimal_x]]
        # List touples of (posición,etiqueta)
        values_x = [
            (i, j)
            for i, j in zip(values_decimal_x, list_x)
        ]
        self.x_axis_labels = VGroup()
        for x_val, x_tex in values_x:
            tex = TexMobject(x_tex)
            tex.scale(0.7)
            tex.next_to(self.coords_to_point(x_val, 0), DOWN)
            self.x_axis_labels.add(tex)
        self.play(
            Write(self.x_axis_labels),
            Write(self.x_axis),
            Write(self.y_axis)
        )


class CameraPosition5(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle = Circle()
        self.set_camera_orientation(phi=80 * DEGREES, theta=45 * DEGREES, distance=6, gamma=120 * DEGREES)
        self.play(ShowCreation(circle), ShowCreation(axes))
        self.wait()


class MoveCamera2(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle = Circle()
        self.play(ShowCreation(circle), ShowCreation(axes))
        self.move_camera(phi=80 * DEGREES, theta=45 * DEGREES, distance=3, run_time=3)
        self.move_camera(phi=-80 * DEGREES, theta=-45 * DEGREES, distance=3, gamma=120 * DEGREES, run_time=3)
        self.wait()


class ParametricCurve2(ThreeDScene):
    def construct(self):
        curve1 = ParametricFunction(
            lambda u: np.array([
                1.2 * np.cos(u),
                1.2 * np.sin(u),
                u / 2
            ]), t_min=-TAU, t_max=TAU,
        )
        curve1.set_stroke(RED, 50)
        curve2 = ParametricFunction(
            lambda u: np.array([
                1.2 * np.cos(u),
                1.2 * np.sin(u),
                u
            ]), color=RED, t_min=-TAU, t_max=TAU,
        )
        curve2.set_stroke(BLUE, 5)
        curve1.set_shade_in_3d(True)
        curve2.set_shade_in_3d(True)

        axes = ThreeDAxes()

        self.add(axes)

        self.set_camera_orientation(phi=80 * DEGREES, theta=-60 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.play(ShowCreation(curve1))
        self.wait()
        self.play(Transform(curve1, curve2), rate_func=there_and_back, run_time=3)
        self.wait()


class Text3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        dot = Dot([1.0, 1.0, 0.0]).set_stroke(RED, 5)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        text3d = TextMobject("This is a 3D text").scale(2).set_shade_in_3d(True)
        text3d.rotate(PI / 2, axis=[1, 1, 0])
        self.add(axes, dot, text3d)
        self.move_camera(phi=0 * DEGREES, theta=0 * DEGREES, distance=3, run_time=3)
        self.wait()


class Text3D3(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        text3d = TextMobject("This is a 3D text")

        self.add_fixed_in_frame_mobjects(text3d)  # <----- Add this
        text3d.to_corner(UL)

        self.add(axes)
        self.begin_ambient_camera_rotation()
        self.play(Write(text3d))

        self.wait(2)

def HSL(hue,saturation=1,lightness=0.5):
    return Color(hsl=(hue,saturation,lightness))


# This function is come and go, but linear
def double_linear(t):
    if t < 0.5:
        return linear(t*2)
    else:
        return linear(1-(t-0.5)*2)

class ValueTrackerWithColor(Scene):
    def construct(self):
        gradient_rectangle = Rectangle(
            width=FRAME_WIDTH - 1,
            height=1,
            fill_opacity=1,
            # Gradient direction
            sheen_direction=RIGHT,
            stroke_width=0
        )
        square = Square(fill_opacity=1)
        square.to_edge(UP, buff=1)
        gradient_rectangle.to_edge(DOWN, buff=1)

        gradient_rectangle.set_color(color=self.get_hsl_set_colors())

        color_tracker = ValueTracker(0)

        color_label = Integer(color_tracker.get_value(), unit="^\\circ")
        # 整数
        color_label.add_updater(lambda v: v.set_value(color_tracker.get_value()).next_to(square, UP))

        square.add_updater(lambda s: s.set_color(HSL(color_tracker.get_value() / 360)))

        line_color = Line(
            gradient_rectangle.get_corner(UL),
            gradient_rectangle.get_corner(UR)
        )
        arrow = Arrow(LEFT, RIGHT)
        arrow.add_updater(lambda a: a.put_start_and_end_on(square.get_bottom() + DOWN * 0.3,
                                                           line_color.point_from_proportion(
                                                               color_tracker.get_value() / 360)))
        # put_start_and_end_on 把直线的首尾放在 start, end 上 point_from_proportion(alpha)在整条路径上占比为alpha处的点
        self.add(gradient_rectangle, square, color_label, arrow)
        self.wait(3)
        self.play(
            color_tracker.set_value, 360,
            rate_func=double_linear,
            run_time=20,
        )
        self.wait(3)

    def get_hsl_set_colors(self, saturation=1, lightness=0.5):
        return [*[HSL(i / 360, saturation, lightness) for i in range(360)]]