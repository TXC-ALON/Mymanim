from manimlib.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class T(Scene):

  def construct(self):
    # object
    f = TexMobject('f(x)=x^4+3x^3')
    f.shift([0, 1, 0])
    g = TexMobject('g(x)=3x^4+x^2+2')
    # f = TexMobject('f(x)','x^4+3x^3')
    # f.shift([0,1,0])
    # g = TexMobject('g(x)', '3x^4+x^2+2')
    g.shift([0, -1, 0])
    self.play(Write(f), Write(g))
    self.play(f.shift, [-4, 2.5, 0], f.scale, 0.7,color, "#FF0000",
              g.shift, [-4, 3.5, 0], g.scale, 0.7
              )
    self.wait()
    f_ = TexMobject('x^4+3x^3')
    g_= TexMobject('3x^4+x^2+2')
    f_.scale(0.7).next_to(f.get_corner(RIGHT), LEFT)
    g_.scale(0.7).next_to(g.get_corner(RIGHT), LEFT)
    # position

    # show
    # self.add(f_, g_)
    self.wait()
