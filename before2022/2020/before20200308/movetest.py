from manimlib.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L
class TextMove(Scene):

  def construct(self):
    # object
    text1 = TextMobject("I Love Manim")
    text1_col = TextMobject("I Love Manim")
    text0 = TextMobject("Hello Manim!", sheen_direction=RIGHT)
    text2 = TextMobject("这是左上角UL")
    # text2 = TextMobject('这是左上角$\\tiny$UL')
    text3 = TextMobject("这是右上角UR")
    text4 = TextMobject("这是左下角DL")
    text5 = TextMobject("这是右下角DR")
    text6 = TextMobject("这是顶部UP")
    text7 = TextMobject("这是底部DOWN")
    text8 = TextMobject("这是左边LEFT")
    text9 = TextMobject("这是右边RIGHT")

    circle1 = Circle(radius=0.4, fill_color="#E1A158", fill_opacity=0.8)
    square1 = Square(side_length=0.8, fill_color="#77B05D", fill_opacity=1)
    group = VGroup(text1_col, circle1, square1)
    group2 = VGroup(text2, text3, text4, text5)
    group3 = VGroup(text6, text7, text8, text9)
    group4 = VGroup(circle1, square1)
    text1.scale(0.8)
    group2.scale(0.8)
    group3.scale(0.8)
    # position
    text2.to_corner(UL)
    text3.to_corner(UR)
    text4.to_corner(DL)
    text5.to_corner(DR)
    text6.to_edge(UP)
    text7.to_edge(DOWN)
    text8.to_edge(LEFT)
    text9.to_edge(RIGHT)

    circle1.next_to(text1_col, LEFT, buff=0.5)
    square1.next_to(text1_col, RIGHT, buff=0.5)

    # text1.move_to(LEFT)
    # show
    self.play(Write(text1))
    self.wait(1)
    self.play(FadeInFromLarge(group2, scale_factor=0.5))
    self.play(FadeIn(group3))
    # self.play(Write(text2))
    # self.play(Write(text3))
    # self.play(Write(text4))
    # self.play(Write(text5))
    # self.play(ShowCreation(text6))
    # self.play(ShowCreation(text7))
    # self.play(ShowCreation(text8))
    # self.play(ShowCreation(text9))
    self.wait(1)
    text1_col.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
    text0.set_color_by_gradient([RED, GREEN, BLUE])
    text1_col.scale(1.1)
    text0.scale(1.6)
    self.play(ReplacementTransform(text1, text1_col))
    self.play(ShowCreation(circle1))
    self.play(FadeIn(square1))
    self.play(ApplyMethod(group.shift, LEFT * 2),run_time=0.5)
    self.play(ApplyMethod(group.shift, UP * 2),run_time=0.5)
    self.play(ApplyMethod(group.shift, RIGHT * 4),run_time=0.5)
    self.play(ApplyMethod(group.shift, DOWN * 4),run_time=0.5)
    self.play(ApplyMethod(group.shift, LEFT * 4),run_time=0.5)
    self.play(ApplyMethod(group.shift, UP * 2),run_time=0.5)
    self.play(ApplyMethod(group.shift, RIGHT * 2),run_time=0.5)
    self.play(FadeOut(group4))
    self.play(ReplacementTransform(text1_col, text0))
    self.wait(1)
