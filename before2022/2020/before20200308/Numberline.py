from manimlib.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class NL(Scene):

  def construct(self):
    # object
    num = NumberLine(color="#FF8080", x_min=-5, x_max=6, unit_size=1, tick_size=0.1,include_numbers=True)
    # position

    # show
    self.play(ShowCreation(num), run_time=3)
    self.wait(2)
