from manimlib.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class PF(GraphScene):
  CONFIG = {
    "x_min": -10,
    "x_max": 10.3,
    "y_min": -1.5,
    "y_max": 1.5,
    "graph_origin": ORIGIN,
    "function_color": RED,
    "axes_color": GREEN,
    "x_labeled_nums": range(-10, 12, 2),
    "y_labeled_nums": range(-2, 2, 1),
    # 设置坐标系范围、原点、函数原色、xy轴分割
  }

  def construct(self):
    self.setup_axes(animate=True)
    self.wait(2)
    func_graph = self.get_graph(self.func_to_graph, self.function_color)
    func_graph2 = self.get_graph(self.func_to_graph2, PURPLE)
    # 这里可以指定函数图像颜色，不指定默认蓝色。。。作者喜好吧
    vert_line = self.get_vertical_line_to_graph(TAU, func_graph, color=YELLOW)
    # 指示线
    graph_lab = self.get_graph_label(func_graph, label="\\cos(x)")
    graph_lab2 = self.get_graph_label(func_graph2, label="\\sin(x)", x_val=-10, direction=UP / 2)
    two_pi = TexMobject("x = 2\\pi")
    # 标签
    label_coord = self.input_to_graph_point(TAU, func_graph)
    # coord 等同的意思  不过换成label_2也没什么影响。看来不是什么函数
    two_pi.next_to(label_coord, RIGHT + UP)
    # 定义标签twp_pi 的位置

    self.play(ShowCreation(func_graph), ShowCreation(func_graph2))
    self.wait(2)
    self.play(ShowCreation(vert_line), ShowCreation(graph_lab), ShowCreation(graph_lab2), ShowCreation(two_pi))
    self.wait(2)

  def func_to_graph(self, x):
    return np.cos(x)

  def func_to_graph2(self, x):
    return np.sin(x)
  # 这里是引用numpy库里的sinx、cosx函数
# object

# position

# show
