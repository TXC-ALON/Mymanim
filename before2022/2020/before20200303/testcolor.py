from manimlib.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class TC(Scene):

  def construct(self):
    # object
    text01 = TextMobject("这是颜色测试01-DARK\_BLUE")
    text01.set_color(DARK_BLUE)
    text01.to_edge(UP)
    text02 = TextMobject("这是颜色测试02-DARK\_BROWN")
    text02.set_color(DARK_BROWN)
    text03 = TextMobject("这是颜色测试03-LIGHT\_BROWN")
    text03.set_color(LIGHT_BROWN)
    text04 = TextMobject("这是颜色测试04-BLUE\_E")
    text04.set_color(BLUE_E)
    text05 = TextMobject("这是颜色测试05-BLUE\_C")
    text05.set_color(BLUE_C)
    text06 = TextMobject("这是颜色测试06-BLUE\_B")
    text06.set_color(BLUE_B)
    text07 = TextMobject("这是颜色测试07-BLUE\_A")
    text07.set_color(BLUE_A)
    text08 = TextMobject("这是颜色测试08-TEAL\_E")
    text08.set_color(TEAL_E)
    text09 = TextMobject("这是颜色测试09-TEAL\_D")
    text09.set_color(TEAL_D)
    text10 = TextMobject("这是颜色测试10-TEAL\_C")
    text10.set_color(TEAL_C)

    # position

    # show

    self.add(text01)
    self.wait(0.5)
    self.add(text02)
    self.wait(0.5)
    self.add(text03)
    self.wait(0.5)
    self.add(text04)
    self.wait(0.5)
    self.add(text05)
    self.wait(0.5)
    self.add(text06)
    self.wait(0.5)
    self.add(text07)
    self.wait(0.5)
    self.add(text08)
    self.wait(0.5)
    self.add(text09)
    self.wait(0.5)
    self.add(text10)
    self.wait(2)
