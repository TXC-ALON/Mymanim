from manimlib.imports import *
from manim_sandbox.utils.imports import *
import math

# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class textshape4(Scene):

    def construct(self):
# object
        text = [r"天行有常",
                r"不为尧存",
                r"不为桀亡",
               ]
        text_group = VGroup(*[
            Text(tex,font = "方正清刻本悦宋简体").set_height(1) for tex in text
        ]).arrange(DOWN).move_to(LEFT*4)
        cir = Circle()
        line = Line(LEFT*4,RIGHT*4,color = GOLD)
        dot = Dot().move_to(text_group[0].get_top())
        dot2 = dot.copy().shift(RIGHT*8)
        line_top = DashedLine(dot,dot2)
        numberline = NumberLine()
# position
        def anim(obj, alpha):
            #obj.add_updater(lambda a: a.scale(alpha))
            #obj.become(obj.scale(2 * alpha+0.01))
            obj.move_to(line.point_from_proportion(alpha))
            obj[0].set_width((alpha+0.001) * 2)
            obj[1].set_height((alpha+0.000001 )*1 )
            obj[2].set_height((alpha )*1.5)

    # show
        self.add(numberline,text_group,cir,dot)
        self.add(text_group.copy().set_color(GREY))
        self.wait()
        self.play(UpdateFromAlphaFunc(text_group,anim),
                  run_time=2, rate_func=linear)
        self.add(dot2,line_top)
        self.wait(2)


class SaveStateRestoreScene(DarkScene):
    def construct(self):
        sq = Square(side_length=2, color=BLUE)
        sq.save_state()
        self.play(sq.shift, RIGHT * 4)
        self.play(sq.restore)
        self.wait(0.3)
        self.play(sq.become, TextMobject("This is a square."))
        self.wait(0.3)
        self.play(Restore(sq))
