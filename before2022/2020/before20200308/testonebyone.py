from manimlib.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class TO(Scene):

  def construct(self):
    # object
    test = TextMobject("onebyone is a good version")
    # position

    # show
    self.play(FadeIn(test, lag_radio=0.5), run_time=3)
    self.wait(2)
