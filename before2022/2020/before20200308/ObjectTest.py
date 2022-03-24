from manimlib.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class OT(Scene):

  def construct(self):
    # object
    circle1 = Circle(color="#76DDC0", radius=1.5, fill_color="#FFEA94", fill_opacity=0.8)
    ellipse1 = Ellipse(width=3, height=2, fill_color="#FFFFFF",fill_opacity=0.8)
    Text1 = TextMobject("Try everything")
    Ans = Annulus(color='#ffff00', fill_color='000000',fill_opacity=0.7,radius=2.5,stroke_width=8)
    # position
    ellipse1.move_to(UR * 2)
    ellipse1.rotate(PI / 3)
    Text1.to_corner(DL)
    Text1.flip()
    # show
    self.play(ShowCreation(circle1))
    self.wait()
    self.play(ShowCreation(ellipse1))
    self.wait()
    self.play(Write(Text1))
    self.play(ShowCreation(Ans),run_time=4,rate_fun=smooth)
    self.wait()
