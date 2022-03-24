from manimlib.imports import *

def HSL(hue,saturation=1,lightness=0.5):
    # 色度，饱和度，亮度
    return Color(hsl=(hue,saturation,lightness))

class ValueTrackerWithColor(Scene):
    def construct(self):
        gradient_rectangle1 = Rectangle(
                                    width=FRAME_WIDTH-1,
                                    height=1,
                                    fill_opacity=1,
                                    # Gradient direction
                                    sheen_direction=RIGHT,
                                    stroke_width=0
                                    )

        gradient_rectangle1.to_edge(UP,buff=1)
        gradient_rectangle1.set_color(color=self.get_hsl_set_colors())
        gradient_rectangle2 = gradient_rectangle1.copy()
        gradient_rectangle2.to_edge(DOWN, buff=1)
        gradient_rectangle2.set_color(color=self.get_hsl_set_colors2())
        gradient_rectangle3 = gradient_rectangle2.copy()
        gradient_rectangle3.move_to(ORIGIN)
        gradient_rectangle3.set_color(color=self.get_hsl_set_colors3())
        self.add(gradient_rectangle1,gradient_rectangle2,gradient_rectangle3)
        self.wait(3)

    def get_hsl_set_colors(self, saturation=1, lightness=0.5):
        return [*[HSL(i / 3, saturation, lightness) for i in range(3)]]
    def get_hsl_set_colors3(self, saturation=1, lightness=0.5):
        return [*[HSL(i / 720, saturation, lightness) for i in range(720)]]
    def get_hsl_set_colors2(self, saturation=1, lightness=0.5):
        return [*[HSL(i / 1080, saturation, lightness) for i in range(1080)]]


def double_linear(t):
    if t < 0.5:
        return linear(t*2)
    else:
        return linear(1-(t-0.5)*2)
#来去函数变得线性
class ValueTrackerWithColor2(Scene):
    def construct(self):
        gradient_rectangle = Rectangle(
                                    width=FRAME_WIDTH-1,
                                    height=1,
                                    fill_opacity=1,
                                    # Gradient direction
                                    sheen_direction=RIGHT,
                                    stroke_width=0
                                    )
        square = Square(fill_opacity=1)
        square.to_edge(UP,buff=1)
        gradient_rectangle.to_edge(DOWN,buff=1)

        gradient_rectangle.set_color(color=self.get_hsl_set_colors())

        color_tracker = ValueTracker(0)

        color_label = Integer(color_tracker.get_value(),unit="^\\circ")
        #整数
        color_label.add_updater(lambda v: v.set_value(color_tracker.get_value()).next_to(square,UP))

        square.add_updater(lambda s: s.set_color(HSL(color_tracker.get_value()/360)))

        line_color = Line(
                        gradient_rectangle.get_corner(UL),
                        gradient_rectangle.get_corner(UR)
                        )
        line_color.move_to(ORIGIN)
        #一个看不见的线
        #arrow = Arrow(LEFT,RIGHT)
        arrow = Arrow(UP,DOWN+LEFT)
        #这个arrow鸟用没有
        arrow.add_updater(lambda a: a.put_start_and_end_on(square.get_bottom()+DOWN*0.3,line_color.point_from_proportion(color_tracker.get_value()/360)))
        # put_start_and_end_on 把直线的首尾放在 start, end 上 point_from_proportion(alpha)在整条路径上占比为alpha处的点
        self.add(gradient_rectangle,square,color_label,arrow)
        self.wait(3)
        self.play(
            color_tracker.set_value,360,
            rate_func=double_linear,
            run_time=10,
            )
        self.wait(3)

    def get_hsl_set_colors(self,saturation=1,lightness=0.5):
        return [*[HSL(i/360,saturation,lightness) for i in range(360)]]
# 区分颜色细度
class testMmodNTracker(Scene):
    CONFIG = {
        "number_of_lines": 30,
        "gradient_colors":[RED,GREEN,BLUE],
        "end_value":100,
        "total_time":100,
    }
    def construct(self):
        circle = Circle().set_height(FRAME_HEIGHT*0.9)
        mod_tracker = ValueTracker(0)
        lines = self.get_m_mod_n_objects(circle,mod_tracker.get_value())
        lines.add_updater(
            lambda mob: mob.become(
                self.get_m_mod_n_objects(circle,mod_tracker.get_value())
                )
            )
        self.add(circle,lines)
        self.wait(3)
        self.play(
            mod_tracker.set_value,self.end_value,
            rate_func=linear,
            run_time=self.total_time
            )
        self.wait(3)

    def get_m_mod_n_objects(self,circle,x,y=None):
        if y==None:
            y = self.number_of_lines
        lines = VGroup()
        for i in range(y):
            start_point = circle.point_from_proportion((i%y)/y)
            end_point = circle.point_from_proportion(((i*x)%y)/y)
            line = Line(start_point,end_point).set_stroke(width=1)
            lines.add(line)
        lines.set_color_by_gradient(*self.gradient_colors)
        return lines
# todo 需要细品



