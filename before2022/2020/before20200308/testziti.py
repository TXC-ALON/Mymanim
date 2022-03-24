from manimlib.imports import *

# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class T (Scene):

  def construct(self):

    #object
    text = Text("试试字体", font='方正清刻本悦宋简体', tex_scale_factor=0.75)
    text.set_color(RED)
    # self.add(formulas)
    self.play(ShowCreation(text))
    self.wait(5)
    #position

    #show
