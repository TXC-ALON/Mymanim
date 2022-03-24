from manimlib.imports import *
from manim_sandbox.utils.imports import *


class RollingWheel(DarkScene):
    def construct(self):
        t2c = {"def": PURPLE_B, "anim": TEAL, "VGroup": BLUE, "UpdateFromAlphaFunc": BLUE,
               "set_value": BLUE_D, "save_state": BLUE_D, "self": RED, "run_time": ORANGE,
               ".": GREY, ",": GREY, "=": "#fa8763"}
        ap = TexMobject("\\alpha=").shift(DOWN * 3 + LEFT * 0.7)
        dec = DecimalNumber(0).next_to(ap, RIGHT)
        l = Line(LEFT * 7, RIGHT * 7).shift(DOWN * 2)
        cir = Circle(radius=1).shift(LEFT * PI + DOWN)
        vec = Vector(DOWN, color=YELLOW).shift(LEFT * PI + DOWN)
        gup = VGroup(cir, vec)
        self.play(ShowCreation(l))
        self.play(ShowCreation(gup))

        code = CodeLine(r"""gup = VGroup(cir,vec)
gup.save_state()
def anim(obj, alpha):
    obj.restore()
    obj.shift(RIGHT*TAU*alpha)
    obj.rotate(-TAU*alpha)
    dec.set_value(alpha)
self.play(UpdateFromAlphaFunc(gup, anim),
    run_time=4)""", t2s={"def": ITALIC})
        code.scale(2).to_corner(UL)
        code.set_color_by_t2c(t2c)
        self.play(Write(code))
        self.play(Write(ap), Write(dec))
        gup.save_state()

        def anim(obj, alpha):
            obj.restore()
            obj.shift(RIGHT * TAU * alpha)
            obj.rotate(-TAU * alpha)
            dec.set_value(alpha)

        path = TracedPath(vec.get_end, stroke_width=4, stroke_color=ORANGE)
        self.add(path)
        self.play(UpdateFromAlphaFunc(gup, anim), run_time=4, rate_func=sine)
        self.wait()