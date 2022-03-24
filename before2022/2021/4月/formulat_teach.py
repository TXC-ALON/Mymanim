from manimlib.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L


class Formula_Teach(Scene):

  def construct(self):
    # object
    formula1 = TexMobject(r"x=-\left( \frac { b }{ 2a }  \right) \pm \frac { \sqrt { { b }^{ 2 }-4ac }  }{ 4a } ")
    self.add(formula1)

# def debugTeX(self, texm):
#   for i, j in zip(range(100), texm):
#     tex_id = TextMobject(str(i)).scale(0.1).set_color(PURPLE)
#     tex_id.move_to(j)
#     self.add(tex_id)

# def debugTeX(self, texm):
#   for i, j in enumerate(texm):
#     tex_id = Text(str(i), font="Euclid").scale(0.2).set_color(RED)
#     tex_id.move_to(j)
#     self.add(tex_id)
# class Formula_Teach_2(Scene):


  def construct(self):
    formula2 = TexMobject("x", "=", "-", "\\left(", "\\frac { b }{ 2a } ", "\\right)", " \\pm", " { \\sqrt {", " { b }^", "{ 2 }", "-", "4","a","c}", "\\over", "4a } ")
    formula2[11].set_color(BLUE)
    formula2[12].set_color(RED)
    formula2[13].set_color(GREEN)
    formula2[14].set_color(PINK)
    formula2[15].set_color(YELLOW)

    self.add(formula2)


class Formula_Teach_0(Scene):

  def construct(self):
    formula0 = TexMobject("x", "=", "-", "{3a", "\\over", "2b}")
    self.add(formula0)
    debugTeX(self, formula0)
