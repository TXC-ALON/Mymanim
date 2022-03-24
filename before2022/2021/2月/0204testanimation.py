from manimlib.imports import *
class concurrent(Scene):
    def construct(self):
        dot1 = Dot()
        dot2 = Dot().set_color(BLUE)
        dot2.shift(UP)
        dot3 = Dot().set_color(PINK)
        dot3.shift(DOWN)

        # 单个动画的演示
        self.play(Write(dot1))
        # 多个动画演示
        self.play(*[
            Transform(i.copy(), j) for i, j in zip([dot1, dot1], [dot2, dot3])
        ])  # 故意使用i,j是为了显示zip的使用

        self.wait()
class TextArray(Scene):
    def construct(self):
        text = TextMobject("tex1","text2","text3")
        text[0].shift(2*LEFT)
        text[0].set_color(RED)
        text[1].shift(LEFT)
        text[1].set_color(BLUE)
        self.play(Write(text[0]))
        self.wait(2)
        # 显示的还是text[0]只是text[0]值变成了text[1]
        self.play(Transform(text[0],text[1]))
        # 此时没有让text[0]消失，但让text[1]显现并转换为text[2]
        # 最终text[0]的值为初始text[1]的值，text[1]的值为初始text[2]的值
        self.play(Transform(text[1],text[2]))
        # 最终屏幕上显示的是text[0]和text[1]
        self.wait(3)

class Formula(Scene):


    def construct(self):
        CONFIG = {
            "template_tex_file_body": TEMPLATE_TEX_FILE_BODY,
            # 笔画宽度
            "stroke_width": 0,
            # 填充不透明度
            "fill_opacity": 1.0,
            # 笔画的描边宽度
            "background_stroke_width": 5,
            # 笔画的描边颜色
            "background_stroke_color": GOLD,
            "should_center": True,
            "height": 2,
            "organize_left_to_right": False,
            "alignment": [1, 1, 0],
        }
        formula = TexMobject("This is a sentence")
        self.play(Write(formula))
        self.wait(3)
class Text3D3(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES,theta=-45*DEGREES)
        text3d=TextMobject("This is a 3D text")

        self.add_fixed_in_frame_mobjects(text3d) #<----- Add this
        text3d.to_corner(UL)

        self.add(axes)
        self.begin_ambient_camera_rotation()
        self.play(Write(text3d))

        sphere = ParametricSurface(
            lambda u, v: np.array([
                1.5*np.cos(u)*np.cos(v),
                1.5*np.cos(u)*np.sin(v),
                1.5*np.sin(u)
            ]),v_min=0,v_max=TAU,u_min=-PI/2,u_max=PI/2,checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32)).scale(2)

        self.play(ShowCreation(sphere))
        self.wait(2)
