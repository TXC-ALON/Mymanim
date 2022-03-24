from manimlib.imports import *
from manim_sandbox.utils.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class complex1(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": average_color("#1f252A",WHITE)
        },
    }

    def construct(self):
        axis_config = {
            "stroke_color": BLACK,
            "stroke_width": 2,
            "include_ticks": False,
            "include_tip": False,
            "line_to_number_buff": SMALL_BUFF,
            "label_direction": DR,
            "number_scale_val": 0.5,
            'decimal_number_config': {'color': BLACK},
        }

        cp_scale = 2
        cp = ComplexPlane(axis_config=axis_config).scale(cp_scale)
        cp.add_coordinates(0, 1, 2, 3, 4, -1, -2, -3, -4)
        cp.add_coordinates(1j, 2j, 3j, -1j, -2j, -3j)

        self.add(cp)

        c_num = 100
        c_list = [BLUE_D, BLUE, GREEN, ORANGE, RED_D]
        colors = color_gradient(c_list, c_num) #返回长度为length_of_output的颜色梯度数组
        color_bar = Line(cp.n2p(-2.), cp.n2p(2.), stroke_width=24).to_corner(UP * 1.75).set_color(c_list[:])
        c_line = Line(cp.n2p(-2.), cp.n2p(2.), stroke_width=4.5, stroke_color=BLACK).next_to(color_bar, DOWN * 0.5)
        self.add(c_line,color_bar)
        w_tick = VGroup()
        for i in range(5):
            tick = Line(ORIGIN, UP * 0.12, color=BLACK, stroke_width=2.5).next_to(c_line, UP * 0.01).shift((i-2)*cp.n2p(1.))
            w_tick.add(tick)
        w_label_01 = TexMobject('-10', color=BLACK).scale(0.6).next_to(w_tick[0], DOWN * 0.4)
        w_label_02 = TexMobject('-1', color=BLACK).scale(0.6).next_to(w_tick[1], DOWN * 0.4)
        w_label_03 = TexMobject('0', color=BLACK).scale(0.6).next_to(w_tick[2], DOWN * 0.4)
        w_label_04 = TexMobject('1', color=BLACK).scale(0.6).next_to(w_tick[3], DOWN * 0.4)
        w_label_05 = TexMobject('10', color=BLACK).scale(0.6).next_to(w_tick[4], DOWN * 0.4)
        w_label = VGroup(w_label_01, w_label_02, w_label_03, w_label_04, w_label_05)
        w_axes = VGroup(w_tick, w_label)
        self.add(w_axes)
        w_color = RED
        omega_text = TexMobject('\\omega', '=', color=BLACK, background_stroke_color=BLACK,
                                background_stroke_width=2.5).scale(1.2).next_to(color_bar, RIGHT * 0.5)
        omega_text[0].set_color(w_color).set_background_stroke(color=w_color)
        omega_value = DecimalNumber(1.0, num_decimal_places=2, color=w_color).next_to(omega_text, RIGHT * 0.5).shift(
            UP * 0.025)
        omega_tracker = Triangle(color=RED, stroke_color=w_color, fill_color=w_color,
                                 fill_opacity=1).set_background_stroke(color=w_color).scale(0.2).rotate(PI).next_to(
            w_tick[3], UP * 0.5)

        omega_value.add_updater(lambda v: v.set_value(np.sign(cp.p2n(omega_tracker.get_center()).real - 0) * 10 ** (
                    abs(cp.p2n(omega_tracker.get_center()).real) - 1)))
        omega_tracker.add_updater(
            lambda t: t.set_color(colors[int((cp.p2n(t.get_center()).real + 2) / 4 * (c_num - 1))]))
        d_theta = 2.5 * DEGREES
        arrow = Arrow(cp.n2p(0), cp.n2p(1), buff=0, color=RED)
        arrow.add_updater(lambda a, dt: a.rotate(d_theta * omega_value.get_value(), about_point=ORIGIN))
        dot = Dot(color=RED).scale(1.5).add_updater(lambda d: d.move_to(arrow.get_end()))
        circle = Circle(radius=cp.n2p(1)[0], color=YELLOW, stroke_width=8)

        color_dict = {'e': GREEN, 'i': PINK, 't': BLUE, '\\omega': RED, '=': BLACK, 'z': YELLOW}
        formula_01 = TexMobject('\\mathbf{z', '=', 'e^{', 'i', '\\omega', 't}}',
                                background_stroke_color=WHITE).set_color_by_tex_to_color_map(color_dict).set_height(0.9)
        formula_01.move_to(cp.n2p(2 + 0.5j))

        self.add(omega_text,omega_value,omega_tracker)
        self.add(arrow,dot,circle,formula_01)
        angle_z = Angle(cp.n2p(1), cp.n2p(0), cp.n2p(0.9+0.6j), radius=0.6, color=BLUE,).scale(10)
        self.add(angle_z)
        debugPoints(self,angle_z[1])

class Angle(VGroup):

    CONFIG = {
        'radius': 1,
        'color': RED,
        'opacity': 0.4,
        'stroke_width': 10,
        # 'below_180': True,
    }

    def __init__(self, A, O, B, **kwargs):

        VMobject.__init__(self, **kwargs)
        OA, OB = A-O, B-O
        theta = np.angle(complex(*OA[:2])/complex(*OB[:2])) # angle of OB to OA
        point_O =Dot().move_to(O)
        line_OA = Line(O, A)
        line_OB = Line(O, B)
        Arc_small = Arc(start_angle=Line(O, B).get_angle(), angle=theta, radius=self.radius,
                     stroke_width=self.stroke_width, color=self.color)
        Arc_large = Arc(start_angle=Line(O, B).get_angle(), angle=theta, radius=self.radius,
                     stroke_width=self.stroke_width, color=self.color)
        Arc_group = VGroup(point_O,line_OA,line_OB,Arc_small,Arc_large)
        self.add(Arc_group)

