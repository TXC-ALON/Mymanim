from manimlib.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class TO(Scene):

  def construct(self):
    # object
    dot1 = Dot(radius=1)
    circle1 = Circle(color="#FFFF00", radius=1, fill_color="#B189C6", fill_opacity=0.8)
    ellipse1 = Ellipse(width=3, height=2, fill_color="DC75CD", fill_opacity=1)
    annulus1 = Annulus(inner_radius=0.5, outer_radius=1, fill_color="#FFFF00", fill_opacity=1, stroke_width=2)
    rectangle1 = Rectangle(color="#9CDCEB", height=1, width=2, fill_color="#F9B775", fill_opacity=1,stroke_width=4)
    square1 = Square(side_length=1, fill_color="#9A72AC", fill_opacity=1)
    arc1 = Arc(radius=1,num_component=9,Start_angle=0,angle=2*PI/3)
    line1 = Line(np.array([-6, -2.4, 0]), np.array([6, -2.4, 0]), color="RED")
    # position
    # dot1.move_to(np.array([-1,1,0]))
    dot1.to_corner(UL)
    circle1.next_to(dot1, RIGHT, buff=0.3)
    ellipse1.next_to(circle1, RIGHT, buff=0.3)
    annulus1.next_to(ellipse1, RIGHT, buff=0.3)
    rectangle1.next_to(dot1, DOWN, buff=0.5)
    square1.next_to(rectangle1, RIGHT, buff=0.3)
    arc1.next_to(square1, RIGHT, buff=0.3)
    #show
    self.play(ShowCreation(dot1))
    self.play(ShowCreation(circle1))
    self.play(ShowCreation(ellipse1))
    self.play(ShowCreation(annulus1))
    self.play(ShowCreation(rectangle1))
    self.play(ShowCreation(square1))
    self.play(ShowCreation(arc1))
    self.play(ShowCreation(line1))
    self.wait(3)
