from manimlib.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L
def debugTeX(self, texm):
	for i, j in enumerate(texm):
		tex_id = Text(str(i), font="Euclid").scale(0.2).set_color(RED)
		tex_id.move_to(j)
		self.add(tex_id)
class finaltest(Scene):

	def construct(self):
# object
		tex0 = TexMobject("\\lim_{","x","\\to","+","\\infty} ")
		tex1 = TexMobject( "{\\left(", "{\\left(","2n","\\right)", "!!","\\over", "\\left(","2n+1","\\right)","!!","}", "\\right)}")
		tex2 = TexMobject("\\frac{1}{2n+1}  ")
		tex3 = TexMobject("=")
		#tex4 = TexMobject("{\\pi","\\over","2","}")
		#tex4 = TexMobject("\\frac{\pi }{2} ")
		#tex5 = TexMobject("{", "a", "\\over", "b", "}")
		tex4 = TexMobject("{\\pi}","\\over","{2}")
		Tex = VGroup(tex0,tex1,tex2,tex3,tex4).arrange(RIGHT,buff=0.5)
		#tex5.next_to(Tex,DOWN,buff=2)
# position

# show
		#self.play(ShowCreation(Tex))
		#self.wait(2)
		#self.play(ShowCreation(tex5))
		#self.wait()
		self.add(tex1)
		debugTeX(self,tex1)
		self.wait(1)
		self.add(tex2)
		debugTeX(self,tex2)
		self.wait(1)
		self.add(tex3)
		debugTeX(self,tex3)
		self.wait(1)
		self.add(tex4)
		debugTeX(self,tex4)
		self.wait(2)
class testLatex(Scene):
	def construct(self):
		#tex1 = TexMobject("\\lim_{","x","\\to","+","\\infty} ")
		#tex1.scale(4)
		#tex2 = TexMobject("\\left(", " \\frac{", "\\left(", "2n", "\\right)", "!!}", "{\\left(", "2n + 1", "\\right ) ", "!!}", "\\right)" )
		#tex3 = TexMobject("\\left(\\frac{1}{2}\\right)")
		#tex4 = TexMobject("\\frac{","d}","{dx","}","f(","x",")","g(","x",")","=")
		#tex6 = TexMobject("{\\left(", "{\\left(", "{\\left(","x","\\right)","!!","\\over", "\\left(","y","\\right)}", "\\right)}","\\right)}")
		tex6 = TexMobject("\\int_{b}^{a} \\sin x\\cos x\\frac{\\mathrm{d} y}{\\mathrm{d} x}")

		#tex5 = TexMobject("\\left(","x","\\right)" )
		#这就是一个括号
		#\left( \frac{\left(a \right )}{\left(b \right )}  \right )
		#self.play(ShowCreation(tex1))
		#self.wait(
		tex6.scale(3)
		self.play(ShowCreation(tex6))
		self.add(tex6)
		debugTeX(self,tex6[0])
		#妈的自己试了半天结果就是一个【0】！！！cao
		self.wait(3)