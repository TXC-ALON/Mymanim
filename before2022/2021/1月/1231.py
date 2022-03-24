from manimlib.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L
# Alt + Ctrl + - 快速折叠
#$5
class MoveBraces(Scene):
	def construct(self):
		text=TexMobject(
			"\\frac{d}{dx}f(x)g(x)=",       #0
			"f(x)\\frac{d}{dx}g(x)",        #1
			"+",                            #2
			"g(x)\\frac{d}{dx}f(x)"         #3
		)
		self.play(Write(text))
		brace1 = Brace(text[1], UP, buff = SMALL_BUFF)
		brace2 = Brace(text[3], UP, buff = SMALL_BUFF)
		t1 = brace1.get_text("$g'f$")
		t2 = brace2.get_text("$f'g$")
		brace3 = Brace(text[1], DOWN, buff=SMALL_BUFF)
		brace4 = Brace(text[3], DOWN, buff=SMALL_BUFF)
		t3 = brace3.get_text("$g'f$")
		t4 = brace4.get_text("$f'g$")
		framebox1 = SurroundingRectangle(text[1], buff=.1)
		framebox2 = SurroundingRectangle(text[3], buff=.1)
		self.play(
			GrowFromCenter(brace1),
			FadeIn(t1),
			)
		self.wait()
		self.play(
			ReplacementTransform(brace1,brace2),
			ReplacementTransform(t1,t2)
			)
		self.wait()
		self.play(
			GrowFromCenter(brace3),
			FadeIn(t3),
		)
		self.play(
			ReplacementTransform(brace3.copy(), brace4),
			ReplacementTransform(t3.copy(), t4)
		)
		self.wait()

		self.play(
			ShowCreation(framebox1),
		)
		self.wait()
		self.play(
			ReplacementTransform(framebox1, framebox2),
		)
		self.wait()
#移动上下框
class MoveBraces2(Scene):
	def construct(self):
		text=TexMobject(
			"\\frac{d}{dx}f(x)g(x)=",       #0
			"f(x)\\frac{d}{dx}g(x)",        #1
			"+",                            #2
			"g(x)\\frac{d}{dx}f(x)"         #3
		)
		self.play(Write(text))

		framebox1 = SurroundingRectangle(text[1], buff=.1)
		framebox2 = SurroundingRectangle(text[3], buff=.1)


		self.play(
			ShowCreation(framebox1),
		)
		self.wait()
		self.play(
			ReplacementTransform(framebox1, framebox2),
		)
		self.wait()
		self.play(ShowCreation(framebox2.set_color(BLUE)))
		framebox1 = SurroundingRectangle(text[1], buff=.1)
		#framebox1在之前已经被移动了位置，需要复原。
		self.play(
			ReplacementTransform(framebox2, framebox1),
			path_arc=np.pi*3
			# np.pi 逆时针旋转，
		)
#移动框
class Arrow2(Scene):
	def construct(self):
		step1 = TextMobject("Step 1")
		step2 = TextMobject("Step 2")
		step1.move_to(LEFT*2+DOWN*2)
		step2.move_to(4*RIGHT+2*UP)
		arrow1 = Arrow(step1.get_right(),step2.get_left(),buff=0.1)
		arrow1.set_color(RED)
		arrow2 = Line(step1.get_top(),step2.get_bottom(),buff=0.1)
		arrow2.set_color(BLUE)
		arrow3 = DashedLine(step1.get_right(), step2.get_right(), buff=0.1)
		arrow3.set_color(ORANGE)
		self.play(Write(step1),Write(step2),ShowCreation(arrow3))
		self.play(GrowArrow(arrow1))
		self.play(GrowArrow(arrow2))
		self.wait()

		step3 = TextMobject("Step 3")
		step3.move_to(2*UP+LEFT*2)
		step4=step3.copy()
		step4.move_to(1*UP+3*LEFT)
		line = Line(step1.get_right(), step3.get_bottom(), buff=0.1)
		lineCopy = Arrow(step1.get_right(), step4.get_bottom(), buff=0.1)

		self.play(Write(step3))
		self.play(GrowArrow(line))
		self.play(
			ReplacementTransform(step3, step4),
			ReplacementTransform(line, lineCopy)
		)
		self.wait()
#箭头类移动

#$6
def Range(in_val,end_val,step=1):
	return list(np.arange(in_val,end_val+step,step))
class Plot1(GraphScene):
	G = np.arange(0, 8, 0.5)
	X = list(G)
	print(X)
	CONFIG = {
		"y_max" : 50,
		"y_min" : 0,
		"x_max" : 7,
		"x_min" : 0,
		"y_tick_frequency" : 5,
		"x_tick_frequency" : 0.5,
		"axes_color" : BLUE,
		"y_labeled_nums": range(0,60,10),
		"x_labeled_nums": X,
# TODO, this is broken...这里有问题，b=np.arange(0, 7.0+0.5, 0.5) array([0. , 0.5, 1. , 1.5, 2. , 2.5, 3. , 3.5, 4. , 4.5, 5. , 5.5, 6. ,6.5, 7. ])
#		1.5 2 2.5 都被当做是2
		"x_label_decimal":1,
		"y_label_direction": RIGHT,
		"x_label_direction": UP,
		"y_label_decimal":3
	}
	def construct(self):
		self.setup_axes(animate=True)
		graph = self.get_graph(lambda x : x**2,
									color = PINK,
									x_min = 0,
									x_max = 7
									)
		self.play(
			ShowCreation(graph),
			run_time = 3
		)
		self.wait()
##!!试一试坐标，发现有些问题。
class Plot1v2(GraphScene):
	CONFIG = {
		"y_max" : 50,
		"y_min" : 0,
		"x_max" : 7,
		"x_min" : 0,
		"y_tick_frequency" : 5,
		"x_tick_frequency" : 1,
		"axes_color" : BLUE,
		"graph_origin" : np.array((0,0,0))
	}
	def construct(self):
		self.setup_axes(animate=True)
		graph = self.get_graph(lambda x : x**2,
									color = GREEN,
									x_min = 2,
									x_max = 4
									)
		self.play(
			ShowCreation(graph),
			run_time = 2
		)
		self.wait()
#坐标系，设置里中心点
class Plot2(GraphScene):
	CONFIG = {
		"y_max": 70,
		"y_min": 0,
		"x_max": 7,
		"x_min": 0,
		"y_tick_frequency": 5,
		"axes_color": BLUE,
		"x_axis_label": "$t$",
		"y_axis_label": "$f(t)$",
	}

	def construct(self):
		self.setup_axes()
		graph = self.get_graph(lambda x: x ** 2, color=GREEN)
		self.play(
			ShowCreation(graph),
			run_time=2
		)
		self.wait()
# Todo 自己写了个画坐标系的函数 本质上就是在空坐标轴上加number
	def setup_axes(self):
		# Add this line
		GraphScene.setup_axes(self)
		# Parametters of labels
		#   For x
		init_label_x = 2
		end_label_x = 8
		step_x = 1
		#   For y
		init_label_y = 20
		end_label_y = 60
		step_y = 5
		# Position of labels
		#   For x
		self.x_axis.label_direction = DOWN  # DOWN is default
		#   For y
		self.y_axis.label_direction = LEFT
		# Add labels to graph
		#   For x
		self.x_axis.add_numbers(*range(
			init_label_x,
			end_label_x + step_x,
			step_x
		))
		#   For y
		self.y_axis.add_numbers(*range(
			init_label_y,
			end_label_y + step_y,
			step_y
		))
		#   Add Animation
		self.play(
			ShowCreation(self.x_axis),
			ShowCreation(self.y_axis)
		)
#依旧是整数坐标系
class Plot5(GraphScene):
	CONFIG = {
		"y_max" : 50,
		"y_min" : 0,
		"x_max" : 7,
		"x_min" : 0,
		"y_tick_frequency" : 10,
		"x_tick_frequency" : 0.5,
		"axes_color" : BLUE,
	}
	def construct(self):
		self.setup_axes()
		graph = self.get_graph(lambda x : x**2, color = GREEN)

		self.play(
			ShowCreation(graph),
			run_time = 2
		)
		self.wait()

	def setup_axes(self):
		GraphScene.setup_axes(self)
		self.x_axis.label_direction = UP
		values_x = [
			(3.5,"3.5"), # (position 3.5, label "3.5")
			(4.5,"\\frac{9}{2}") # (position 4.5, label "9/2")
		]
		self.x_axis_labels = VGroup() # Create a group named x_axis_labels
		#   pos.   tex.
		for x_val, x_tex in values_x:
			tex = TexMobject(x_tex) # Convert string to tex
			tex.scale(0.6)
			tex.next_to(self.coords_to_point(x_val, 0), DOWN) #Put tex on the position
			self.x_axis_labels.add(tex) #Add tex in graph
		self.play(
			Write(self.x_axis_labels),
			Write(self.x_axis),
			Write(self.y_axis)
		)
#通过tex添加小数和分数
class Plot6(GraphScene):
	CONFIG = {
		"y_max" : 50,
		"y_min" : 0,
		"x_max" : 7,
		"x_min" : 0,
		"y_tick_frequency" : 10,
		"x_tick_frequency" : 0.5,
		"axes_color" : BLUE,
	}
	def construct(self):
		self.setup_axes()
		graph = self.get_graph(lambda x : x**2, color = GREEN)

		self.play(
			ShowCreation(graph),
			run_time = 2
		)
		self.wait()

	def setup_axes(self):
		GraphScene.setup_axes(self)
		self.x_axis.label_direction = UP
		# List of values of positions
		values_decimal_x=[0,0.5,1,1.5,3.35,6.2]
		# Transform positions to tex labels
		list_x = [*["%s"%i for i in values_decimal_x]]
		#list_x 是字符串 加*是为了使列表里每个都是独立元素
		# List touples of (position,label)
		values_x = [
			(i,j)
			for i,j in zip(values_decimal_x,list_x)
		]
		self.x_axis_labels = VGroup()
		for x_val, x_tex in values_x:
			tex = TexMobject(x_tex)
			tex.scale(0.7)
			tex.next_to(self.coords_to_point(x_val, 0), DOWN)
			line = Line(self.coords_to_point(x_val, -4),self.coords_to_point(x_val, 4))
			line.set_color(RED)
			self.x_axis_labels.add(tex)
			self.x_axis_labels.add(line)
		self.play(
			Write(self.x_axis_labels),
			Write(self.x_axis),
			Write(self.y_axis)
		)
#自制，通过line加坐标
class Plot7(GraphScene):
    CONFIG = {
        "y_max" : 50,
        "y_min" : 0,
        "x_max" : 7,
        "x_min" : 0,
        "y_tick_frequency" : 10,
        "x_tick_frequency" : 0.5,
        "axes_color" : BLUE,
    }
    def construct(self):
        self.setup_axes()
        graph = self.get_graph(lambda x : x**2, color = GREEN)

        self.play(
            ShowCreation(graph),
            run_time = 2
        )
        self.wait()

    def setup_axes(self):
        GraphScene.setup_axes(self)
        self.x_axis.label_direction = UP
        # Additional parametters
        init_val_x = 0
        step_x = 0.5
        end_val_x = 7
        # Position of labels
        values_decimal_x=Range(init_val_x,end_val_x,step_x)
        # List of labels
        list_x=[*["%.1f"%i for i in values_decimal_x]]
        # List touples of (posición,etiqueta)
        values_x = [
            (i,j)
            for i,j in zip(values_decimal_x,list_x)
        ]
        self.x_axis_labels = VGroup()
        for x_val, x_tex in values_x:
            tex = TexMobject(x_tex)
            tex.scale(0.7)
            tex.next_to(self.coords_to_point(x_val, 0), DOWN)
            self.x_axis_labels.add(tex)
        self.play(
            Write(self.x_axis_labels),
            Write(self.x_axis),
            Write(self.y_axis)
        )
#接近完美了

class PlotSinCos(GraphScene):
    CONFIG = {
        "y_max" : 1.5,
        "y_min" : -1.5,
        "x_max" : 3*PI/2,
        "x_min" : -3*PI/2,
        "y_tick_frequency" : 0.5,
        "x_tick_frequency" : PI/2,
        "graph_origin" : ORIGIN,
        "y_axis_label": None, # Don't write y axis label
        "x_axis_label": None,
    }
    def construct(self):
        self.setup_axes()
        plotSin = self.get_graph(lambda x : np.sin(x),
                                    color = GREEN,
                                    x_min=-4,
                                    x_max=4,
                                )
        plotCos = self.get_graph(lambda x : np.cos(x),
                                    color = PINK,
                                    x_min=-PI,
                                    x_max=PI,
                                )
        plotSin.set_stroke(width=3) # width of line
        plotCos.set_stroke(width=2)
        # Animation
        for plot in (plotSin,plotCos):
            self.play(
                    ShowCreation(plot),
                    run_time = 2
                )
        self.wait()

    def setup_axes(self):
        GraphScene.setup_axes(self)
        # width of edges
        self.x_axis.set_stroke(width=2)
        self.y_axis.set_stroke(width=2)
        # color of edges
        self.x_axis.set_color(RED)
        self.y_axis.set_color(YELLOW)
        # Add x,y labels
        func = TexMobject("\\sin\\theta")
        var = TexMobject("\\theta")
        func.set_color(BLUE)
        var.set_color(PURPLE)
        func.next_to(self.y_axis,UP)
        var.next_to(self.x_axis,RIGHT+UP)
        # Y labels
        self.y_axis.label_direction = LEFT*1.5
        self.y_axis.add_numbers(*[-1,1])
        #Parametters of x labels
        init_val_x = -3*PI/2
        step_x = PI/2
        end_val_x = 3*PI/2
        # List of the positions of x labels
        values_decimal_x=Range(init_val_x,end_val_x,step_x)
        # List of tex objects
        list_x=TexMobject("-\\frac{3\\pi}{2}", #   -3pi/2
                            "-\\pi", #              -pi
                            "-\\frac{\\pi}{2}", #   -pi/2
                            "\\,", #                 0 (space)
                            "\\frac{\\pi}{2}", #     pi/2
                            "\\pi",#                 pi
                            "\\frac{3\\pi}{2}" #     3pi/2
                          )
        #List touples (position,label)
        values_x = [(i,j)
            for i,j in zip(values_decimal_x,list_x)
        ]
        self.x_axis_labels = VGroup()
        for x_val, x_tex in values_x:
            x_tex.scale(0.7)
            if x_val == -PI or x_val == PI: #if x is equals -pi or pi
                x_tex.next_to(self.coords_to_point(x_val, 0), 2*DOWN) #Put 2*Down
            else: # In another case
                x_tex.next_to(self.coords_to_point(x_val, 0), DOWN)
            self.x_axis_labels.add(x_tex)

        self.play(
            *[Write(objeto)
            for objeto in [
                    self.y_axis,
                    self.x_axis,
                    self.x_axis_labels,
                    func,var
                ]
            ],
            run_time=2
        )
#画sincos
#简单总结画坐标系，目前来看由于np的不知名原因，list里的浮点数会变凑整。贝多芬的方法是用list来确定位置，自己来做字符串或tex进行填充，
#我觉得可以理解。操作性也可以。