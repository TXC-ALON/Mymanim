from manimlib.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class TAA(Scene):

  def construct(self):
    # object
    quote = TextMobject("我倒是要好好学学manim")
    quote.set_color(GOLD)
    quote.to_edge(UP)
    quote2 = TextMobject("I will learn manim well to see see")
    quote2.set_color(GREEN)
    author = TextMobject("+-*/-阿伟", color=PURPLE)

    # position

    author.next_to(quote.get_corner(DOWN + RIGHT), DOWN)

    # show
    self.add(quote)
    self.add(author)
    self.wait(2)
    self.play(Transform(quote, quote2), ApplyMethod(author.move_to, quote2.get_corner(DOWN + RIGHT) + DOWN + 2 * LEFT))
    self.play(ApplyMethod(author.scale, 1.6))
    author.match_color(quote2)
    self.play(FadeOut(quote), FadeOut(author))
    self.wait(2)


class moveText(Scene):
  def construct(self):
    square = Square(side_length=5, fill_color=BLUE, fill_opacity=0.5)
    label = TextMobject("斜着来")
    label.bg = BackgroundRectangle(label, fill_opacity=1)
    #改变TextMobject背景的属性
    label_group = VGroup(label.bg, label)
    label_group.rotate(TAU / 6)
    #TAU = 360
    label2 = TextMobject("加个边框", color=PINK)
    label2.bg = BackgroundRectangle(label2, color=BLUE_C, fill_color=RED_B, fill_opacity=0.5)
    label2_group = VGroup(label2.bg, label2)
    label2_group.next_to(label_group, DOWN * 2 + RIGHT)
    label3 = TextMobject("试一试彩虹色如何")
    label3.scale(1.4)
    label3.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
    #颜色渐变
    label3.to_edge(DOWN)

    self.add(square)
    self.play(FadeIn(label_group))
    self.play(FadeIn(label2_group))
    self.play(FadeIn(label3))
    self.wait(2)


