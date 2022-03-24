from manimlib.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class TVT(Scene):

  def construct(self):
    # object
    text = TexMobject(
      "\\frac{d}{dx}f(x)g(x)=", "f(x)\\frac{d}{dx}g(x)", "+",
      "g(x)\\frac{d}{dx}f(x)"
    )
    text2 = TexMobject(
      "\\frac{d}{dx}f(x)g(x)=", "g'f", "+",
      "f'g"
    )
    framebox1 = SurroundingRectangle(text[1], buff=.1)
    t1 = TexMobject("g'f")
    step1 = TextMobject("Step 1")
    step2 = TextMobject("Step 2")
    arrow = Arrow(LEFT, RIGHT)
    arrow.set_stroke(width=3)
    brace1 = Brace(text[3], UP, buff=SMALL_BUFF)
    t2 = brace1.get_text("$f'g$")
    # position
    t1.next_to(framebox1, UP, buff=0.1)
    # text2[0].next_to(text[0], DOWN * 4, aligned_edge=TOP)
    # text2[1].next_to(text[1], DOWN * 4, aligned_edge=BOTTOM)
    # text2[2].next_to(text[2], DOWN * 4.5, aligned_edge=TOP)
    #text2[3].next_to(text[3], DOWN * 4, aligned_edge=BOTTOM)
    text2[0].move_to(text[0].get_center()[0], DOWN * 5)
    #text2[0].next_to(text[0], DOWN * 5)
    # text2[1].next_to(text[1], DOWN * 4)
    # text2[2].next_to(text[2], DOWN * 4.5)
    # text2[3].next_to(text[3], DOWN * 4)
    text2[1].move_to(np.array([text[1].get_center()[0], text2[0].get_center()[1], 0]))
    text2[2].move_to(np.array([text[2].get_center()[0], text2[0].get_center()[1], 0]))
    text2[3].move_to(np.array([text[3].get_center()[0], text2[0].get_center()[1], 0]))

    # text2[0].shift((text[0].get_center()[1] - text2[0].get_center()[1]) * UP)
    # text2[1].shift((text[1].get_center()[1] - text2[1].get_center()[1]) * UP)
    # text2[2].shift((text[2].get_center()[1] - text2[2].get_center()[1]) * UP)
    # text2[3].shift((text[3].get_center()[1] - text2[3].get_center()[1]) * UP)

    step1.move_to(LEFT * 1 + UP * 2)
    arrow.next_to(step1, RIGHT, buff=.1)
    step2.next_to(arrow, RIGHT, buff=.1)
    # show
    self.play(Write(text))
    self.play(Write(step1))

    self.play(
      ShowCreation(framebox1),
      FadeIn(t1)
    )
    self.wait()
    self.play(GrowArrow(arrow))
    self.play(Write(step2))
    self.wait()
    self.play(
      GrowFromCenter(brace1),
      FadeIn(t2),
    )
    self.play(ApplyMethod(Group(*self.mobjects).shift, UP * 1.5), run_time=0.5)

    arrow2 = Arrow(text[1].get_bottom(), text2[1].get_top())
    self.play(Write(text2))
    self.play(GrowArrow(arrow2))
    arrow3 = DashedLine(text[3].get_bottom(), text2[3].get_top(), buff=0.1)
    arrow3.set_color(RED)
    self.play(ShowCreation(arrow3))
    # debugTeX(self, text)
    # debugTeX(self, text2)
    self.wait()
