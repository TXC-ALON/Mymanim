from manimlib.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class TAA(Scene):

  def construct(self):
    # object
    text1 = TextMobject("ShowPartial")
    text2 = TextMobject("ShowCreation")
    text3 = TextMobject("Uncreate")
    text4 = TextMobject("DrawBorderThenFill")
    text5 = TextMobject("Write")
    text6 = TextMobject(*list("ShowIncreasingSubsets"), arg_separator="")
    text7 = TextMobject(*list("ShowSubmobjectsOneByOne"), arg_separator="")
    typesOfText = TextMobject("""
                This is a regular text,
                $this is a formula$,
                $$this is a formula$$
                """)
    typesOfText2 = TextMobject("""
                This is a regular text,
                $\\frac{x}{y}$,
                $$x^2+y^2=a^2$$
                """)

    # position

    # show
    # self.play(ShowPartial(text1))
    # self.wait()
    # self.remove()
    self.play(ShowCreation(text2))
    self.wait()
    self.remove(text2)
    self.play(Uncreate(text3))
    self.wait()
    self.play(DrawBorderThenFill(text4))
    self.wait()
    self.remove(text4)
    self.play(Write(text5))
    self.wait()
    self.remove(text5)
    self.play(ShowIncreasingSubsets(text6))
    self.wait()
    self.remove(text6)
    self.play(ShowSubmobjectsOneByOne(text7, remover=True), run_time=3)
    self.wait()
    # self.play(Write(typesOfText))
    # self.wait(3)
    # self.remove(typesOfText)
    # self.play(Write(typesOfText2))
    # self.wait(3)
    # self.remove(typesOfText2)


class TCS2(Scene):
  def construct(self):
    self.add(Circle().shift(2 * LEFT), Square().shift(2 * RIGHT))
    self.wait()
    self.play(FadeOut(Group(*self.mobjects)))
    self.wait()
