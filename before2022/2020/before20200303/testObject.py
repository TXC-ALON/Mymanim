from manimlib.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class TO(Scene):

  def construct(self):
    # object
    dot1 = Dot(radius=1)
    circle1 = Circle(radius=1, color="YELLOW", fill_color="PURPLE", fill_opacity=1)
    ellipse1 = Ellipse(width=2, height=1, fill_color="DC75CD", fill_opacity=1)
    annulus1 = Annulus(innerradius=0.5, outer_radius=1, fill_color="#FFFF00", full_opacity=1)
    rectangle1 = Rectangle(color="#9CDCEB", height=1, width=2, fill_color="#F9B775", full_opacity=1)
    square1 = Square(side_length=1, fill_color="#9A72AC", full_opacity=1)
    arc1 = Arc(radius=1, num_components=10)
    line1 = Line(np.array([-6, -2.4, 0]), np.array([6, -2.4, 0]), color="RED")
    # position
    dot1.move_to(np.array([-1,1,0]))
    circle1.next_to(dot1, RIGHT, buff=0.1)
    ellipse1.next_to(circle1, RIGHT, buff=0.1)
    annulus1.next_to(ellipse1, RIGHT, buff=0.1)
    rectangle1.next_to(dot1, DOWN, buff=0.1)
    square1.next_to(rectangle1, RIGHT, buff=0.1)
    arc1.next_to(square1, RIGHT, buff=0.1)
    # show
    self.play(ShowCreation(dot1))
    self.play(ShowCreation(circle1))
    self.play(ShowCreation(ellipse1))
    self.play(ShowCreation(annulus1))
    self.play(ShowCreation(rectangle1))
    self.play(ShowCreation(square1))
    self.play(ShowCreation(arc1))
    self.play(ShowCreation(line1))
    self.wait(3)
