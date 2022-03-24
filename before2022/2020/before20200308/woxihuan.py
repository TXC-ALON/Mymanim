from manimlib.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class WXH(Scene):

  def construct(self):
    # object
    wxh = TextMobject("我", "喜欢", "你")
    wxh.set_color_by_tex_to_color_map({"我": BLUE, "喜欢": RED, "你": "#DC75CD"})

    # position

    # show
    self.play(ShowCreation(wxh))
    self.wait(2)
