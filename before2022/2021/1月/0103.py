from manimlib.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class AudioTest(Scene):
    def construct(self):
        group_dots = VGroup(*[Dot() for _ in range(3)])
        group_dots.arrange_submobjects(RIGHT)
        for dot in group_dots:
            self.add_sound("click", gain=-10)
            self.add(dot)
            self.wait()
        self.wait()


# todo 出现一些问题
class SVGTest(Scene):
    def construct(self):
        svg = SVGMobject("finger")
        # svg = SVGMobject("camera")
        self.play(DrawBorderThenFill(svg, rate_func=linear))
        self.wait()


# 书写svg
class ImageTest(Scene):
    def construct(self):
        image = ImageMobject("note")
        self.play(FadeIn(image))
        self.wait()


# 贴图
class CheckSVG(Scene):
    CONFIG = {
        "camera_config": {"background_color": WHITE},
        "svg_type": "svg",
        "file": "",
        "svg_scale": 0.9,
        "angle": 0,
        "flip_svg": False,
        "fill_opacity": 1,
        "remove": [],
        "stroke_color": BLACK,
        "fill_color": BLACK,
        "stroke_width": 3,
        "numbers_scale": 0.5,
        "show_numbers": False,
        "animation": False,
        "direction_numbers": UP,
        "color_numbers": RED,
        "space_between_numbers": 0,
        "show_elements": [],
        "color_element": BLUE,
        "set_size": "width",
        "remove_stroke": [],
        "show_stroke": [],
        "stroke_": 1
    }

    def construct(self):
        if self.set_size == "width":
            width_size = FRAME_WIDTH
            height_size = None
        else:
            width_size = None
            height_size = FRAME_HEIGHT

        if self.svg_type == "svg":
            self.imagen = SVGMobject(
                "%s" % self.file,
                # fill_opacity = 1,
                stroke_width=self.stroke_width,
                stroke_color=self.stroke_color,
                width=width_size,
                height=height_size
            ).rotate(self.angle).set_fill(self.fill_color, self.fill_opacity).scale(self.svg_scale)
        else:
            self.imagen = self.import_text().set_fill(self.fill_color, self.fill_opacity).rotate(self.angle).set_stroke(
                self.stroke_color, self.stroke_width)
            if self.set_size == "width":
                self.imagen.set_width(FRAME_WIDTH)
            else:
                self.imagen.set_height(FRAME_HEIGHT)
            self.imagen.scale(self.svg_scale)
        self.personalize_image()
        if self.flip_svg == True:
            self.imagen.flip()
        if self.show_numbers == True:
            self.print_formula(self.imagen,
                               self.numbers_scale,
                               self.direction_numbers,
                               self.remove,
                               self.space_between_numbers,
                               self.color_numbers)

        self.return_elements(self.imagen, self.show_elements)
        for st in self.remove_stroke:
            self.imagen[st].set_stroke(None, 0)
        for st in self.show_stroke:
            self.imagen[st].set_stroke(None, self.stroke_)
        if self.animation == True:
            self.play(DrawBorderThenFill(self.imagen))
        else:
            self.add(self.imagen)
        self.wait()

    def import_text(self):
        return TexMobject("")

    def personalize_image(self):
        pass

    def print_formula(self, text, inverse_scale, direction, exception, buff, color):
        text.set_color(RED)
        self.add(text)
        c = 0
        for j in range(len(text)):
            permission_print = True
            for w in exception:
                if j == w:
                    permission_print = False
            if permission_print:
                self.add(text[j].set_color(self.stroke_color))
        c = c + 1

        c = 0
        for j in range(len(text)):
            permission_print = True
            element = TexMobject("%d" % c, color=color)
            element.scale(inverse_scale)
            element.next_to(text[j], direction, buff=buff)
            for w in exception:
                if j == w:
                    permission_print = False
            if permission_print:
                self.add(element)
            c = c + 1

    def return_elements(self, formula, adds):
        for i in adds:
            self.add_foreground_mobjects(formula[i].set_color(self.color_element),
                                         TexMobject("%d" % i, color=self.color_element,
                                                    background_stroke_width=0).scale(self.numbers_scale).next_to(
                                             formula[i], self.direction_numbers, buff=self.space_between_numbers))


# 貌似是一堆函数，没搞起来


class FunctionTracker(Scene):
    def construct(self):
        # f(x) = x**2
        fx = lambda x: x.get_value() ** 2
        # ValueTrackers definition
        x_value = ValueTracker(0)
        fx_value = ValueTracker(fx(x_value))
        # DecimalNumber definition
        x_tex = DecimalNumber(x_value.get_value()).add_updater(lambda v: v.set_value(x_value.get_value()))
        fx_tex = DecimalNumber(fx_value.get_value()).add_updater(lambda v: v.set_value(fx(x_value)))
        # TeX labels definition
        x_label = TexMobject("x = ")
        fx_label = TexMobject("x^2 = ")
        # Grouping of labels and numbers
        group = VGroup(x_tex, fx_tex, x_label, fx_label).scale(2.6)
        VGroup(x_tex, fx_tex).arrange_submobjects(DOWN, buff=3)
        # Align labels and numbers
        x_label.next_to(x_tex, LEFT, buff=0.7, aligned_edge=x_label.get_bottom())
        fx_label.next_to(fx_tex, LEFT, buff=0.7, aligned_edge=fx_label.get_bottom())

        self.add(group.move_to(ORIGIN))
        self.wait(3)
        self.play(
            x_value.set_value, 30,
            rate_func=linear,
            run_time=10
        )
        self.wait()
        self.play(
            x_value.set_value, 0,
            rate_func=linear,
            run_time=10
        )
        self.wait(3)


class FunctionTrackerWithNumberLine(Scene):
    def construct(self):
        # f(x) = x**2
        fx = lambda x: x.get_value() ** 2
        # ValueTrackers definition
        x_value = ValueTracker(0)
        fx_value = ValueTracker(fx(x_value))
        # DecimalNumber definition
        x_tex = DecimalNumber(x_value.get_value()).add_updater(lambda v: v.set_value(x_value.get_value()))
        fx_tex = DecimalNumber(fx_value.get_value()).add_updater(lambda v: v.set_value(fx(x_value)))
        # TeX labels definition
        x_label = TexMobject("x = ")
        fx_label = TexMobject("x^2 = ")
        # Grouping of labels and numbers
        group = VGroup(x_tex, fx_tex, x_label, fx_label).scale(2)
        # Set the labels position
        x_label.next_to(x_tex, LEFT, buff=0.7, aligned_edge=x_label.get_bottom())
        fx_label.next_to(fx_tex, LEFT, buff=0.7, aligned_edge=fx_label.get_bottom())
        # Grouping numbers and labels
        x_group = VGroup(x_label, x_tex)
        fx_group = VGroup(fx_label, fx_tex)
        # Align labels and numbers
        VGroup(x_group, fx_group).arrange_submobjects(RIGHT, buff=2, aligned_edge=DOWN).to_edge(UP)
        # Get NumberLine,Arrow and label from x
        # def get_number_line_group(self,label,x_max,unit_size,v_tracker,step_label=1,**number_line_config):
        x_number_line_group = self.get_number_line_group(
            "x", 30, 0.2, step_label=10, v_tracker=x_value, tick_frequency=2
        )
        x_number_line_group.to_edge(LEFT, buff=1)
        # Get NumberLine,Arrow and label from f(x)
        fx_number_line_group = self.get_number_line_group(
            "x^2", 900, 0.012, step_label=100, v_tracker=fx_tex,
            tick_frequency=50
        )
        fx_number_line_group.next_to(x_number_line_group, DOWN, buff=1).to_edge(LEFT, buff=1)

        self.add(
            x_number_line_group,
            fx_number_line_group,
            group
        )
        self.wait()
        self.play(
            x_value.set_value, 30,
            rate_func=linear,
            run_time=10
        )
        self.wait()
        self.play(
            x_value.set_value, 0,
            rate_func=linear,
            run_time=10
        )
        self.wait(3)

    def get_numer_labels_to_numberline(self, number_line, x_max=None, x_min=0, buff=0.2, step_label=1, **tex_kwargs):
        # This method return the labels of the NumberLine
        labels = VGroup()
        x_max = number_line.x_max
        for x in range(x_min, x_max + 1, step_label):
            x_label = TexMobject(f"{x}", **tex_kwargs)
            # 这里不是很理解，首先这个fx为什么显示是x，然后后面进来的参数是什么
            # Format strings contain “replacement fields” surrounded by curly braces {}. Anything that is not contained in braces is considered literal text, which is copied unchanged to the output. If you need to include a brace character in the literal text, it can be escaped by doubling: {{ and }}.
            # See manimlib/mobject/number_line.py CONFIG dictionary
            x_label.next_to(number_line.number_to_point(x), DOWN, buff=buff)
            labels.add(x_label)
        return labels

    def get_number_line_group(self, label, x_max, unit_size, v_tracker, step_label=1, **number_line_config):
        # Set the Label (x,or x**2)
        number_label = TexMobject(label)
        # Set the arrow
        arrow = Arrow(UP, DOWN, buff=0).set_height(0.5)
        # Set the number_line
        number_line = NumberLine(
            x_min=0,
            x_max=x_max,
            unit_size=unit_size,
            numbers_with_elongated_ticks=[],
            **number_line_config
        )
        # Get the labels from number_line
        labels = self.get_numer_labels_to_numberline(number_line, step_label=step_label, height=0.2)
        # Set the arrow position
        arrow.next_to(number_line.number_to_point(0), UP, buff=0)
        # Grouping arrow and number_label
        label = VGroup(arrow, number_label)
        # Set the position of number_label
        number_label.next_to(arrow, UP, buff=0.1)
        # Grouping all elements
        numer_group = VGroup(label, number_line, labels)
        # Set the updater to the arrow and number_label
        label.add_updater(lambda mob: mob.next_to(number_line.number_to_point(v_tracker.get_value()), UP, buff=0))

        return numer_group


# HSL color, see https://pypi.org/project/colour/
def HSL(hue, saturation=1, lightness=0.5):


# 色度，饱和度，亮度
    return Color(hsl=(hue, saturation, lightness))


# This function is come and go, but linear
def double_linear(t):
    if t < 0.5:
        return linear(t * 2)
    else:
        return linear(1 - (t - 0.5) * 2)


# 来去函数变得线性
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
        circle1 = Circle(radius = 2.5)
        gradient_rectangle.to_edge(DOWN, buff=1)

        gradient_rectangle.set_color(color=self.get_hsl_set_colors())

        color_tracker = ValueTracker(0)

        color_label = Integer(color_tracker.get_value(), unit="^\\circ")
        # 整数
        color_label.add_updater(lambda v: v.set_value(color_tracker.get_value()).next_to(square, UP))

        square.add_updater(lambda s: s.set_color(HSL(color_tracker.get_value() / 360)))


        arrow = Arrow(LEFT, RIGHT)
        arrow.add_updater(lambda a: a.put_start_and_end_on(ORIGIN,circle1.point_from_proportion(
                                                               color_tracker.get_value() / 360)))
        # put_start_and_end_on 把直线的首尾放在 start, end 上 point_from_proportion(alpha)在整条路径上占比为alpha处的点
        self.add(square, color_label, arrow)
        self.wait(3)
        self.play(
            color_tracker.set_value, 360,
            rate_func=double_linear,
            run_time=20,
        )
        self.wait(3)

    def get_hsl_set_colors(self, saturation=1, lightness=0.5):
        return [*[HSL(i / 360, saturation, lightness) for i in range(360)]]


class MmodNTracker(Scene):
    CONFIG = {
        "number_of_lines": 400,
        "gradient_colors": [RED, YELLOW, GREEN, BLUE, PINK],
        "end_value": 100,
        "total_time": 360,
    }

    def construct(self):
        circle = Circle().set_height(FRAME_HEIGHT * 0.9)
        mod_tracker = ValueTracker(0)
        lines = self.get_m_mod_n_objects(circle, mod_tracker.get_value())
        lines.add_updater(
            lambda mob: mob.become(
                self.get_m_mod_n_objects(circle, mod_tracker.get_value())
            )
        )
        self.add(circle, lines)
        self.wait(3)
        self.play(
            mod_tracker.set_value, self.end_value,
            rate_func=linear,
            run_time=self.total_time
        )
        self.wait(3)

    def get_m_mod_n_objects(self, circle, x, y=None):
        if y == None:
            y = self.number_of_lines
        lines = VGroup()
        for i in range(y):

        lines.set_color_by_gradient(*self.gradient_colors)
        return lines
