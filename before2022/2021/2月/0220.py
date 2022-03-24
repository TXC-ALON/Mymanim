from manimlib.imports import *
from manim_sandbox.utils.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L
class testtriangle(Scene):

    def construct(self):
# object
        tri = Triangle().scale(2.5)
        dot = Dot().move_to(tri.points[0])

        cir = Circle().scale(1).set_color(GOLD).move_to(dot)#.set_fill(color = average_color(GOLD,PINK),opacity = 1)

        cir2 = Circle().scale(0.5).set_color(GREEN).move_to(cir.points[8])
        dot2 = Dot().move_to(cir.points[8])
        def anim(obj1, alpha):
            obj1.move_to(tri.point_from_proportion(alpha))
            cir.add_updater(lambda a: a.move_to(obj1))
            cir2.add_updater(lambda a: a.next_to(cir))

        def anim2(obj2, alpha):
            obj2.move_to(cir.point_from_proportion(alpha))
            cir2.add_updater(lambda a: a.move_to(obj2))
# position

# show
        self.play(ShowCreation(tri))
        self.add(dot,cir,cir2)
        self.wait(1)
        cir.rotate(PI/2)#小细节，不然anim alpha就从右边开始
        self.play(UpdateFromAlphaFunc(dot,anim),
                  UpdateFromAlphaFunc(dot2,anim2),
                  run_time=5, rate_func=linear)
        self.wait(1)

class textchange3(Scene):

        def construct(self):
            def HSL(hue, saturation=1, lightness=0.5):
                return Color(hsl=(hue, saturation, lightness))
            text = Text("天行有常", font="方正清刻本悦宋简体").set_height(1).move_to(UP)
            line = Line(LEFT*4,RIGHT*4,color=GREY)
            text2 = text.copy().move_to(LEFT*4)
            self.add(line)
            self.play(Write(text))

            def anim(obj, alpha):
                # ann_pre_sec.set_color([*[HSL(i / 360, 1, 0.5) for i in range(360)]])
                obj[0].set_color([*[HSL(alpha+0.2, 1, 0.5)]])
                obj[1].set_color([*[HSL(alpha+0.6, 1, 0.5)]])
                obj[2].set_color([*[HSL(alpha+0.8, 1, 0.5)]])
                obj[3].set_color([*[HSL(alpha, 1, 0.5)]])
                obj.set_height(alpha*1+1)
                obj.move_to(line.point_from_proportion(alpha))

            self.play(ReplacementTransform(text,text2))
            self.play(UpdateFromAlphaFunc(text,anim),
                  run_time=4, rate_func=there_and_back)
            self.wait(1)


class textshape3(Scene):

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
            obj[1].set_height((alpha+0.001 )*1 )
            obj[2].scale(math.log(alpha+1.1,2))

    # show
        self.add(numberline,text_group,cir,dot)
        self.add(text_group.copy().set_color(GREY))
        self.wait()
        self.play(UpdateFromAlphaFunc(text_group,anim),
                  run_time=2, rate_func=linear)
        self.add(dot2,line_top)
        self.wait(2)

