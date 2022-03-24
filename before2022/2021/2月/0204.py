from manimlib.imports import *
from manim_sandbox.utils.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class Test_mytext(Scene):

    def construct(self):

        color_dict = {'R': PINK, 'd': YELLOW, 'r': ORANGE, '\\theta': BLUE, '\\over': WHITE,
              't': BLUE, 'e': GREEN, 'i': RED, '\\sin': WHITE, '\\cos': WHITE}

        font_list = ['Comic Sans MS', '庞门正道标题体', 'Consolas', 'SWGothe', 'Rough___Dusty_Chalk',
                     'SWScrps', '新蒂小丸子体']

        origin_formula = TexMobject('f', '(', 't', ')', '=', 'x', '(', 't', ')', '+', 'y', '(', 't', ')', 'i', '=',
                             '(', 'R', '-', 'r', ')', 'e^{', 'i', 't}', '+', 'd', 'e^{', '-', 'i', '{R', '-',
                             'r', '\\over', 'r}', 't}').scale(1)\
                        .set_color_by_tex_to_color_map(color_dict).to_corner(LEFT * 2 + UP * 1.5)
        formulas = VGroup(origin_formula)

        for i in range(len(font_list)):
            formula_i = MyText('f', '(', 't', ')', '=', 'x', '(', 't', ')', '+', 'y', '(', 't', ')', 'i', '=',
                             '(', 'R', '-', 'r', ')', 'e^{', 'i', 't}', '+', 'd', 'e^{', '-', 'i', '{R', '-',
                             'r', '\\over', 'r}', 't}', default_font=font_list[i], tex_scale_factor=0.75)
            formula_i.set_color_by_tex_to_color_map(color_dict)
            replace_dict = {'e^{': 'e', 't}': 't', '{R': 'R', 'r}': 'r', '\\over': '-'}
            new_formula = formula_i.get_new_font_texs(replace_dict)
            new_formula.to_corner(LEFT * 2 + UP * 1.5).shift(DOWN * 0.8 * (i+1))
            formulas.add(new_formula)

        self.add(formulas)

        self.wait(5)

class update(Scene):
    def construct(self):
        sq = Square(side_length = 1).move_to(LEFT*5)

        dot0 = Dot().add_updater(lambda a: a.move_to(
            sq.get_vertices()[0])).scale(1.5).set_color(PINK)
        path = Line(LEFT*5, RIGHT*5)
        path2 = TracedPath(dot0.get_center, stroke_width=6, stroke_color=YELLOW)
        dt = 1/60
        def anim(sq, dt):
            sq.rotate(3*dt*PI)
            sq.shift(2.5*RIGHT*dt)
        sq.add_updater(anim)
        self.add(sq,path,dot0,path2)
        self.wait(5)

from manimlib.imports import *
from manim_sandbox.utils.imports import *


class TestDanma(Scene):
    def construct(self):
        color_map = [RED_A, RED_B, RED_C,
                     GOLD_D, GOLD_C, GOLD_B, GOLD_A,
                     YELLOW_E, YELLOW_D, YELLOW_C, YELLOW_B,
                     GREEN_A, GREEN_B, GREEN_C,
                     TEAL_A, TEAL_B, TEAL_C, TEAL_D,
                     BLUE_C, BLUE_D,
                     PURPLE_A, PURPLE_B, PURPLE_C, PURPLE_D,
                     ]

        def mysum(frame, time, a):
            count = 0
            for i in range(frame-time+1):
                count += i*a
            return count
        f = 5
        a = PI/180*0.1
        v = 0.5

        def func(v, time, frame, a):
            t = math.floor(time)
            return np.array([v*t*np.cos(mysum(frame, t, a))*0.05,
                             v*t*np.sin(mysum(frame, t, a))*0.05, 0])

        dotg_0 = VGroup()
        for t in range(min(f, 200)):
            dot_i = Dot(func(v, t, f, a), color=RED).scale(0.5)
            dotg_0.add(dot_i)
        self.add(dotg_0)
        for f in range(300):
            dotg_i = VGroup()
            for t in range(min(f, 180)):
                dot_j = Dot(func(v, t, f, a)).scale(0.5).set_color(
                    color_map[math.floor(t/20) % len(color_map)])
                dotg_i.add(dot_j)
            self.play(Transform(dotg_0, dotg_i), run_time=1/200)
            vg_rm = VGroup()
            for obj in self.mobjects:
                if get_line_long(obj.get_center(), ORIGIN) >= 10:
                    vg_rm.add(obj)
            self.remove(vg_rm)


class Test2(Scene):
    def construct(self):
        color_map = [RED_A, RED_B, RED_C,
                     GOLD_D, GOLD_C, GOLD_B, GOLD_A,
                     YELLOW_E, YELLOW_D, YELLOW_C, YELLOW_B,
                     GREEN_A, GREEN_B, GREEN_C,
                     TEAL_A, TEAL_B, TEAL_C, TEAL_D,
                     BLUE_C, BLUE_D,
                     PURPLE_A, PURPLE_B, PURPLE_C, PURPLE_D,
                     ]

        def mysum(time, frame, cont):
            count = 0
            for i in range(frame-time+1):
                count += i*cont
            return count

        def myfunc(v, t, f, a):
            t_ = math.floor(t)
            return np.array([
                v*t_*np.cos(mysum(t_, f, a)),
                v*t_*np.sin(mysum(t_, f, a)), 0
            ])
        f = 1
        a = 3*0.05
        v = 0.015

        dot_0 = Dot(myfunc(v, 1, f, a), color=RED).scale(0.7)
        self.add(dot_0)
        for f in range(0, 1100, 100):
            dot_i_group = VGroup()
            for t in range(min(f, 490)):
                dot_i = Dot(myfunc(v, t, f, a)).scale(0.7).set_color(
                    color_map[math.floor(t/20) % len(color_map)])
                dot_i_group.add(dot_i)
            self.play(Transform(dot_0, dot_i_group), run_time=1/60)
            vg_rm = VGroup()
            for obj in self.mobjects:
                if get_line_long(obj.get_center(), ORIGIN) >= 14:
                    vg_rm.add(obj)
            self.remove(vg_rm)

class Envelop(Scene):

    def construct(self):
        num=360
        lines=VGroup()
        t=ValueTracker(0.)
        dec_num=DecimalNumber(0,number_decimal_places=2).to_corner(DR, buff=0.5)
        text=TexMobject("n=").next_to(dec_num,LEFT,buff=0.18)

        def func(lines, dt):
            lines_=VGroup()
            for i in range(num):
                distance=get_norm(np.array([np.cos(i*TAU/num),np.sin(i*TAU/num),0])\
                              -np.array([np.cos(t.get_value()*i*TAU/num),np.sin(t.get_value()*i*TAU/num),0]))
                if distance > 0:
                    line_i=Line(3.5*np.array([np.cos(i*TAU/num),np.sin(i*TAU/num),0]),
                            3.5*np.array([np.cos(t.get_value()*i*TAU/num),np.sin(t.get_value()*i*TAU/num),0]),
                            stroke_width=1)
                    lines_.add(line_i)
            lines_.set_color_by_gradient([RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE])
            lines.become(lines_)
        lines.set_color_by_gradient([RED,ORANGE,YELLOW,GREEN,BLUE,PURPLE])
        dec_num.add_updater(lambda a:a.set_value(t.get_value()))
        self.add(lines, dec_num,text)
        lines.add_updater(func)
        self.add(lines,dec_num)
        self.play(t.set_value, 7, run_time=7, rate_func=linear)

class Kaleidoscope(Scene):
    def Cup(self, x, dt):
        x.t -= dt
        if x.t < 0:
            self.remove(x)
        x.set_width(2*(x.edr-rush_into(x.t/x.allt)*(x.edr-x.opr)))
        x.set_stroke(width=rush_into(x.t/x.allt)*x.st)

    def Ripples(self, pos=ORIGIN, stroke_width=20, start_radius=1, end_radius=2, time=1, color="#aef"):
        C = Circle(radius=start_radius, stroke_width=stroke_width, color=color)
        C.move_to(pos)
        C.opr = start_radius
        C.edr = end_radius
        C.st = stroke_width
        C.t = time
        C.allt = time
        self.add(C)
        C.add_updater(self.Cup)

    def construct(self):
        self.wait(1)
        for i in range(10):
            self.Ripples(pos=random.randint(-4, 4)*LEFT+random.randint(-4, 4)*UP,
                         end_radius=random.randint(2, 5), time=random.randint(5, 10)/10)
            self.wait(random.randint(3, 7)/10)
        self.wait(5)

class Knowledgeimproved(Scene):
    def construct(self):
        tex1 = TexMobject(r"\sqrt x ", stroke_width=2)
        tex2 = TexMobject(r"{(xyz)^2\over 2}", stroke_width=2)
        tex3 = TexMobject(r"S={1\over 2}Ah", stroke_width=2)
        tex4 = TexMobject(r"u^x", stroke_width=2)
        tex5 = TexMobject(
            r"e=\lim_{n\to \infty}\left(1+{1\over n}\right)^n", stroke_width=2)
        tex6 = TexMobject(r"x-y", stroke_width=2)
        tex7 = TexMobject(r"\sqrt{x+y\over x-y}", stroke_width=2)
        tex8 = TexMobject(r"|Z|=\sqrt{a^2+b^2}", stroke_width=2)
        tex9 = TexMobject(r"\sqrt{{1\over 12}+{1\over 48}}", stroke_width=2)
        tex10 = TexMobject(r"y^2={{\sqrt y}\over{x+2}}", stroke_width=2)
        tex11 = Matrix([["x", "x^2+1", "1"], ["y", "y^2+1", "1"],
                        ["z", "z^2+1", "1"]], stroke_width=2)
        self.add(tex11)

class ShiftRotate(Scene):

    def construct(self):
        grid = NumberPlane()
        self.add(grid)
        sq_1 = Square(side_length=1, color=TEAL).shift(LEFT*5)
        sq_1.save_state()

        def func(mob, alpha):
            sq_1.restore()
            sq_1.shift(RIGHT*10*alpha)
            sq_1.rotate(PI*3*alpha)

        self.play(UpdateFromAlphaFunc(sq_1, func), run_time=5, rate_func=sine)
        self.wait()


class RandomWaterMark(Scene):
    def construct(self):
        grid = NumberPlane().set_opacity(0.4)
        self.add(grid)
        text = Text("bilibili独播", font="思源黑体 CN Bold").scale(0.5)

        def move_to_random_place(mob, dt):
            text.move_to(np.array([
                (random.randint(-7, 7))*dt*60,
                (random.randint(-4, 4))*dt*40,
                0
            ]))

        text.add_updater(move_to_random_place)
        self.add(text)
        self.wait(5)

from manimlib.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L
def HSL(hue, saturation=1, lightness=0.5):
    return Color(hsl=(hue, saturation, lightness))


def annularsec():
    ann = VGroup()
    for i in range(3600):
        ann_pre_sec = AnnularSector(
            outer_radius=3.5,
            inner_radius=2.5,
            fill_opacity=1,
            start_angle=0+i*PI/1800,
            angle=PI/180+PI/180000,
            # Gradient direction
            stroke_width=0)
        ann_pre_sec.set_color(Color(hsl=(i/3600, 1, 0.5)))
        ann.add(ann_pre_sec)
    return ann



class colortracker(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": average_color("#1f252A")
        },
    }
    def construct(self):
        # object
        ann_sec = AnnularSector(
            outer_radius=3,
            inner_radius=2.5,
            fill_opacity=1,
            start_angle=0,
            angle=PI / 3,
            # Gradient direction
            sheen_direction=RIGHT,
            stroke_width=0
        )

        y = annularsec()
        square = Square(fill_opacity=1).scale(0.6)
        color_tracker = ValueTracker(0)
        color_label = Integer(color_tracker.get_value(), unit="^\\circ")
        # 整数
        color_label.add_updater(lambda v: v.set_value(color_tracker.get_value()).next_to(square, UP))
        square.add_updater(lambda s: s.set_color(HSL(color_tracker.get_value() / 360)))

        circle1 = Circle(radius=3)
        color_tracker = ValueTracker(0)

        color_label = Integer(color_tracker.get_value(), unit="^\\circ")
        # 整数
        color_label.add_updater(lambda v: v.set_value(color_tracker.get_value()).next_to(square, UP))

        square.add_updater(lambda s: s.set_color(HSL(color_tracker.get_value() / 360)))

        #arrow = Arrow(LEFT, RIGHT)
        #arrow.add_updater(lambda a: a.put_start_and_end_on(ORIGIN, circle1.point_from_proportion(
         #   color_tracker.get_value() / 360)))
        # put_start_and_end_on 把直线的首尾放在 start, end 上 point_from_proportion(alpha)在整条路径上占比为alpha处的点
        dota = Dot().add_updater(lambda a: a.move_to(circle1.point_from_proportion(color_tracker.get_value() / 360)))
        self.add(y)
        self.wait()
        mobjects = VGroup(square, color_label, dota)
        self.play(
            *[FadeIn(mob) for mob in mobjects]
        )
        self.wait(1)
        self.play(
            color_tracker.set_value, 360,
            rate_func=linear,
            run_time=10,
        )
        self.wait(2)

    def get_hsl_set_colors(self, saturation=1, lightness=0.5):
        return [*[HSL(i / 360, saturation, lightness) for i in range(360)]]

