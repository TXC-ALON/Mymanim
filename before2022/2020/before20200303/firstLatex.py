from manimlib.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class FL(Scene):

  def construct(self):
    # object
    title = TextMobject("This is some \\LaTeX")
    basel = TexMobject(
      "\\sum_{n=1}^\\infty "
      "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
    )

    # position
    VGroup(title, basel).arrange(DOWN)
    # show
    self.play(
      Write(title),
      FadeInFrom(basel, UP)
    )
    self.wait(2)


class SL(Scene):
  def construct(self):
    equal = TextMobject("=", color=RED)
    eq_left01 = TextMobject("$1^3+2^3+3^3+\\quad\\dots\\quad+n^3$", color=GREEN)
    eq_right01 = TextMobject("$(1+2+3\\quad\\dots\\quad+n)^2$", color=YELLOW)

    eq_left02 = TextMobject("$\Sigma_{i=1}^{n} i^{3}$", color=GREEN)
    eq_right02 = TextMobject("$(\Sigma_{i=1}^{n} i)^{2}$", color=YELLOW)

    equation02 = VGroup(equal, eq_left02, eq_right02)

    eq_left01.next_to(equal, LEFT)
    eq_right01.next_to(equal, RIGHT)
    eq_left02.next_to(equal, LEFT)
    eq_right02.next_to(equal, RIGHT)

    self.play(FadeIn(eq_left01), FadeIn(equal), FadeIn(eq_right01))
    self.wait(1)
    self.play(ReplacementTransform(eq_left01, eq_left02))
    self.play(ReplacementTransform(eq_right01, eq_right02))
    self.wait(1)
    self.play(ApplyMethod(equation02.scale, 2.4))
    self.wait(1)

    eq3 = equation02.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
    self.play(ReplacementTransform(equation02, eq3))
    self.wait(2)
