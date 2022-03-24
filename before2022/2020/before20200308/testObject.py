from manimlib.imports import *


class Grid(VGroup):
  CONFIG = {
    "height": 6.0,
    "width": 6.0,
  }

  def __init__(self, rows, columns, **kwargs):
    digest_config(self, kwargs, locals())
    super().__init__(**kwargs)

    x_step = self.width / self.columns
    y_step = self.height / self.rows

    for x in np.arange(0, self.width + x_step, x_step):
      self.add(Line(
        [x - self.width / 2., -self.height / 2., 0],
        [x - self.width / 2., self.height / 2., 0],
      ))
    for y in np.arange(0, self.height + y_step, y_step):
      self.add(Line(
        [-self.width / 2., y - self.height / 2., 0],
        [self.width / 2., y - self.height / 2., 0]
      ))


class ScreenGrid(VGroup):
  CONFIG = {
    "rows": 8,
    "columns": 14,
    "height": FRAME_Y_RADIUS * 2,
    "width": 14,
    "grid_stroke": 0.5,
    "grid_color": WHITE,
    "axis_color": RED,
    "axis_stroke": 2,
    "labels_scale": 0.25,
    "labels_buff": 0,
    "number_decimals": 2
  }

  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    rows = self.rows
    columns = self.columns
    grid = Grid(width=self.width, height=self.height, rows=rows, columns=columns)
    grid.set_stroke(self.grid_color, self.grid_stroke)

    vector_ii = ORIGIN + np.array((- self.width / 2, - self.height / 2, 0))
    vector_si = ORIGIN + np.array((- self.width / 2, self.height / 2, 0))
    vector_sd = ORIGIN + np.array((self.width / 2, self.height / 2, 0))

    axes_x = Line(LEFT * self.width / 2, RIGHT * self.width / 2)
    axes_y = Line(DOWN * self.height / 2, UP * self.height / 2)

    axes = VGroup(axes_x, axes_y).set_stroke(self.axis_color, self.axis_stroke)

    divisions_x = self.width / columns
    divisions_y = self.height / rows

    directions_buff_x = [UP, DOWN]
    directions_buff_y = [RIGHT, LEFT]
    dd_buff = [directions_buff_x, directions_buff_y]
    vectors_init_x = [vector_ii, vector_si]
    vectors_init_y = [vector_si, vector_sd]
    vectors_init = [vectors_init_x, vectors_init_y]
    divisions = [divisions_x, divisions_y]
    orientations = [RIGHT, DOWN]
    labels = VGroup()
    set_changes = zip([columns, rows], divisions, orientations, [0, 1], vectors_init, dd_buff)
    for c_and_r, division, orientation, coord, vi_c, d_buff in set_changes:
      for i in range(1, c_and_r):
        for v_i, directions_buff in zip(vi_c, d_buff):
          ubication = v_i + orientation * division * i
          coord_point = round(ubication[coord], self.number_decimals)
          label = Text(f"{coord_point}", font="Arial", stroke_width=0).scale(self.labels_scale)
          label.next_to(ubication, directions_buff, buff=self.labels_buff)
          labels.add(label)

    self.add(grid, axes, labels)


class CoordScreen(Scene):
  def construct(self):
    screen_grid = ScreenGrid()
    dot = Dot([1, 1, 0])
    self.add(screen_grid)
    self.play(FadeIn(dot))
    self.wait()

class TO(Scene):

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
    # dot1.move_to(np.array([-1,1,0]))
    dot1.move_to(5*LEFT+1*UP)
    circle1.next_to(dot1, RIGHT, buff=1)
    ellipse1.next_to(circle1, RIGHT, buff=1)
    annulus1.next_to(ellipse1, RIGHT, buff=1)
    rectangle1.move_to(4*LEFT+1.5*DOWN)
    square1.next_to(ellipse1, DOWN, buff=0.7)
    arc1.next_to(annulus1, DOWN, buff=0.7)
    #show
    screen_grid = ScreenGrid()
    self.add(screen_grid)
    self.play(ShowCreation(dot1))
    self.play(ShowCreation(circle1))
    self.play(ShowCreation(ellipse1))
    self.play(ShowCreation(annulus1))
    self.play(ShowCreation(rectangle1))
    self.play(ShowCreation(square1))
    self.play(ShowCreation(arc1))
    self.play(ShowCreation(line1))
    self.wait(3)
