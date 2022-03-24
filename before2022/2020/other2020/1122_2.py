class TestObject(Scene):

  def construct(self):
    # object
    dot1 = Dot(radius=0.4)
    circle1 = Circle(color="#FFFF00", radius=1, fill_color="#B189C6", fill_opacity=0.8)
    ellipse1 = Ellipse(width=3, height=2, fill_color="DC75CD", fill_opacity=1)
    annulus1 = Annulus(inner_radius=0.5, outer_radius=1, fill_color="#FFFF00", fill_opacity=1, stroke_width=2)
    rectangle1 = Rectangle(color="#F9B775", height=1.5, width=3, fill_color="#9CDCEB", fill_opacity=1,stroke_width=1)
    square1 = Square(side_length=1.5, fill_color="#F0AC5F", fill_opacity=1)
    arc1 = Arc(radius=1.5,num_component=9,Start_angle=0,angle=2*PI/3)
    line1 = Line(np.array([-6, -0.25, 0]), np.array([6, -0.25, 0]), color="RED")
    # position
    dot1.move_to(5*LEFT+1*UP)
    circle1.next_to(dot1, RIGHT, buff=1)
    ellipse1.next_to(circle1, RIGHT, buff=1)
    annulus1.next_to(ellipse1, RIGHT, buff=1)
    rectangle1.move_to(4*LEFT+1.5*DOWN)
    square1.next_to(ellipse1, DOWN, buff=0.7)
    arc1.next_to(annulus1, DOWN, buff=0.7)
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

from manimlib.imports import *

# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class SF(Scene):

  def construct(self):

    #object
    plane = NumberPlane()
    #plane.add(plane.get_axis_labels(x_label_tex="x", y_label_tex="y"))
    plane.add(plane.get_axis_labels())
    #???plane.add(plane.get_axis_label(label_tex: "x", axis:"y" , edge: UP, direction: DL))
    
    self.add(plane)
    points = [x * RIGHT + y * UP
              for x in np.arange(-5, 5, 1)
              for y in np.arange(-5, 5, 1)
              ]
    vec_field = []

    #position
    for point in points:
      field = 0.5 * RIGHT + 0.5* UP
      result = Vector(field).shift(point).set_color(YELLOW)
      vec_field.append(result)
    #show
    draw_field = VGroup(*vec_field)
    self.play(ShowCreation(draw_field),run_time = 25)
    self.wait(2)



class SF2(Scene):

  def construct(self):

    numplane = NumberPlane()
    x, y = np.linspace(-5, 5, 11), np.linspace(-4, 4, 9)

    vect_group = VGroup()
    for y_i in y:
      for x_j in x:
        vect_ij = Vector(UR * 0.5, color=YELLOW).shift(x_j * RIGHT + y_i * UP)
        vect_group.add(vect_ij)

    self.play(ShowCreation(numplane))
    self.wait()
    self.play(ShowCreation(vect_group))

    self.wait(5)
