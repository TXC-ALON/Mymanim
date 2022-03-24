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
    self.play(ShowCreation(draw_field),run_time = 5)
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
