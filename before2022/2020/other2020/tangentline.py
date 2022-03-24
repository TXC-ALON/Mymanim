#实现导数变化
from manimlib.imports import *
class Secant4(GraphScene):
    CONFIG = {
        "start_x" : -3,
        "big_x" : 6,
        "dx" : 0.01,
        "x_min" : -7,
        "x_max" : 7,
        "y_min" : -50,
        "y_max": 50,
        "y_tick_frequency":5,
        "x_labeled_nums" : list(range(-6, 6, 1)),
        "y_labeled_nums" : list(range(-50,50,10)),
        "graph_origin":ORIGIN  #设置调整坐标轴的选项
    }
    def construct(self):
        self.draw_graph() #画坐标轴和函数图像
        self.draw_secant()

    def draw_graph(self):
        self.setup_axes(animate = True)
        graph = self.get_graph(lambda x : x**3) #根据自己的修改函数
        label = self.get_graph_label(
            graph, "f(x) = x^3",
        )
        label.next_to(graph)
        self.play(ShowCreation(graph))
        self.play(Write(label))
        self.wait()
        self.graph = graph

    def draw_secant(self):
        ss_group = self.get_secant_slope_group(
            self.start_x,self.graph,
            dx=self.dx,
            dx_label= "dx",
            df_label= "dy",
            )   #the result is in the group of {df dx df_lable dx_label secantline}

        secant_line= ss_group.secant_line

        self.play(ShowCreation(ss_group.secant_line)
            )
        ss_group.add(ss_group.secant_line)
        for target_x in self.big_x,4,100:
            self.animate_secant_slope_group_change(
                ss_group,target_dx= self.big_x
             ) #zheshi secant line. 不是导数变化的图像.中间宽度会变大

        self.remove(ss_group)

        deriv=self.get_derivative_graph(self.graph)
        deriv_func= self.get_graph_label(
            deriv, label="f'(x) = 3x**2", #更改导函数的结果
        )
        deriv_func.next_to(deriv)
        self.play(ShowCreation(deriv))
        self.play(Write(deriv_func))
        self.wait(2)


