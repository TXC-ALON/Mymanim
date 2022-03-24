from manimlib.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class Graph2D(GraphScene):
  def x_2(self, x):
    return x ** 2

  def construct(self):
    self.setup_axes(animate=True)
    graph = self.get_graph(self.x_2, color=GREEN, x_min=0, x_max=3)
    self.play(ShowCreation(graph), run_time=2)
    self.wait()
