from manimlib.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class TipesOfText2(Scene):
	def construct(self):
		typesOfText = TextMobject("""
			This is a regular text,
			$\\frac{x}{y}$,
			$\\displaystyle\\frac{x}{y}$,
			$x^2+y^2=a^2$，
			$$x^2+y^2=a^2$$
			""")
		trytext = TextMobject(
			'''
			$\\frac{x}{y}$,
			$\\displaystyle\\frac{x}{y}$,
			'''
		)
		#行内公式displaystyle
		self.play(Write(typesOfText))
		self.play(FadeOut(typesOfText))
		self.play(Write(trytext))
		self.wait(3)
#公式格式
class RotateObject(Scene):
	def construct(self):
		textM = TextMobject("Text")
		textC = TextMobject("Reference text")
		textM.shift(UP)
		textM.rotate(PI/4) # <- Radians
		# You can use .rotate(45*DEGREES) too
		self.play(Write(textM),Write(textC))
		self.wait(1)
		self.play(ShowCreation(textM.rotate(PI/4)))
		self.wait(1)
		textM.rotate(PI/4)
		self.wait(1)
		textM.rotate(PI/4)
		self.wait(1)
		textM.rotate(PI)
		self.wait(1)
#旋转
class FlipObject(Scene):
	def construct(self):
		textM = TextMobject("Text")
		textM.flip(UP)
		self.play(Write(textM))
		self.wait(2)
#翻转
class SizeTextOnLaTeX(Scene):
	def construct(self):
		textHuge = TextMobject("{\\Huge Huge Text 012.\\#!?} Text")
		texthuge = TextMobject("{\\huge huge Text 012.\\#!?} Text")
		textLARGE = TextMobject("{\\LARGE LARGE Text 012.\\#!?} Text")
		textLarge = TextMobject("{\\Large Large Text 012.\\#!?} Text")
		textlarge = TextMobject("{\\large large Text 012.\\#!?} Text")
		textNormal = TextMobject("{\\normalsize normal Text 012.\\#!?} Text")
		textsmall = TextMobject("{\\small small Text 012.\\#!?} Texto normal")
		textfootnotesize = TextMobject("{\\footnotesize footnotesize Text 012.\\#!?} Text")
		textscriptsize = TextMobject("{\\scriptsize scriptsize Text 012.\\#!?} Text")
		texttiny = TextMobject("{\\tiny tiny Texto 012.\\#!?} Text normal")
		textHuge.to_edge(UP)
		texthuge.next_to(textHuge,DOWN,buff=0.1)
		textLARGE.next_to(texthuge,DOWN,buff=0.1)
		textLarge.next_to(textLARGE,DOWN,buff=0.1)
		textlarge.next_to(textLarge,DOWN,buff=0.1)
		textNormal.next_to(textlarge,DOWN,buff=0.1)
		textsmall.next_to(textNormal,DOWN,buff=0.1)
		textfootnotesize.next_to(textsmall,DOWN,buff=0.1)
		textscriptsize.next_to(textfootnotesize,DOWN,buff=0.1)
		texttiny.next_to(textscriptsize,DOWN,buff=0.1)
		self.add(textHuge,texthuge,textLARGE,textLarge,textlarge,textNormal,textsmall,textfootnotesize,textscriptsize,texttiny)
		self.wait(3)
#字体大小
class TextFonts(Scene):
	def construct(self):
		textNormal = TextMobject("\\textrm{Roman serif text 012.\\#!?} Text")
		textItalic = TextMobject("\\textit{Italic text 012.\\#!?} Text")
		textTypewriter = TextMobject("\\texttt{Typewritter text 012.\\#!?} Text")
		textBold = TextMobject("\\textbf{Bold text 012.\\#!?} Text")
		textSL = TextMobject("\\textsl{Slanted text 012.\\#!?} Text")
		textSC = TextMobject("\\textsc{Small caps text 012.\\#!?} Text")
		textNormal.to_edge(UP)
		textItalic.next_to(textNormal,DOWN,buff=.5)
		textTypewriter.next_to(textItalic,DOWN,buff=.5)
		textBold.next_to(textTypewriter,DOWN,buff=.5)
		textSL.next_to(textBold,DOWN,buff=.5)
		textSC.next_to(textSL,DOWN,buff=.5)
		self.add(textNormal,textItalic,textTypewriter,textBold,textSL,textSC)
		self.wait(3)
#字体
class FormulaColor1(Scene):
	def construct(self):
		text1 = TexMobject("x","=","{a","\\over","b}")
		text1[0].set_color(RED)
		text1[1].set_color(BLUE)
		text1[2].set_color(GREEN)
		text1[3].set_color(ORANGE)
		text1[4].set_color("#DC28E2")
		text2 = TexMobject("x","=","\\frac{a}{b}")
		text2[0].set_color(RED)
		text2[1].set_color(BLUE)
		text2[2].set_color(GREEN)
		text2.next_to(text1,RIGHT,buff=0.5)
		self.play(Write(text1))
		self.play(Write(text2))
		self.wait(1)
#公式上色
def debugTeX(self, texm):
	for i, j in enumerate(texm):
		tex_id = Text(str(i), font="Euclid").scale(0.2).set_color(RED)
		tex_id.move_to(j)
		self.add(tex_id)
#公式注释
class FormulaColor3(Scene):

	def construct(self):
		plane = NumberPlane()
		# plane.add(plane.get_axis_labels(x_label_tex="x", y_label_tex="y"))
		plane.add(plane.get_axis_labels())
		# ???plane.add(plane.get_axis_label(label_tex: "x", axis:"y" , edge: UP, direction: DL))
		#self.add(plane)
		text1 = TexMobject("\\sqrt{","\\int_{","a}^","{b}","\\left(","\\frac{x}{y}","\\right)","dx}")
		text1[0].set_color(RED)
		text1[1].set_color(BLUE)
		text1[2].set_color(GREEN)
		text1[3].set_color(YELLOW)
		text1[4].set_color(PINK)
		text1[5].set_color(ORANGE)
		text1[6].set_color(PURPLE)
		text1[7].set_color(MAROON)
		text1.to_corner(UL)
		text1.scale(2)
		text1.move_to([-3.5,2,0])
		self.add(text1)
		debugTeX(self, text1)
		text2 = TexMobject("\\sqrt{", "\\int_{", "a}^", "{b}", "\\left(", "\\frac{x}{y}", "\\right)", "dx.}")
		text2[0].set_color(RED)
		text2[1].set_color(BLUE)
		text2[2].set_color(GREEN)
		text2[3].set_color(YELLOW)
		text2[4].set_color(PINK)
		text2[5].set_color(ORANGE)
		text2[6].set_color(PURPLE)
		text2[7].set_color(MAROON)
		text2.scale(2)
		text2.move_to([3.5, 2, 0])
		self.add(text2)
		debugTeX(self, text2)
		text3 = TexMobject("\\sqrt{", "\\int_", "{a}^", "{b}", "{\\left(", "{x", "\\over", "y}", "\\right)}", "d", "x",
						  ".}")
		text3[0].set_color(RED)
		text3[1].set_color(BLUE)
		text3[2].set_color(GREEN)
		text3[3].set_color(YELLOW)
		text3[4].set_color(PINK)
		text3[5].set_color(ORANGE)
		text3[6].set_color(PURPLE)
		text3[7].set_color(MAROON)
		text3[8].set_color(TEAL)
		text3[9].set_color(GOLD)
		text3.scale(2)
		text3.move_to([-3.5, -2, 0])
		self.add(text3)
		debugTeX(self, text3)
		text4 = TexMobject("\\sqrt{", "\\int_", "{a", "+", "c}^", "{b}", "{\\left(", "{x", "\\over", "y}", "\\right)}",
						  "d", "x", ".}")
		text4[0].set_color(RED)
		text4[1].set_color(BLUE)
		text4[2].set_color(GREEN)
		text4[3].set_color(YELLOW)
		text4[4].set_color(PINK)
		text4[5].set_color(ORANGE)
		text4[6].set_color(PURPLE)
		text4[7].set_color(MAROON)
		text4[8].set_color(TEAL)
		text4[9].set_color(GOLD)
		text4[10].set_color(GRAY)
		text4[11].set_color(RED)
		text4.scale(2)
		text4.move_to([3.5, -2, 0])

		#text = VGroup(text1,text2,text3,text4).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
		self.play(Write(text4[0:6]))
		self.wait(2)
		self.add(text4)
		debugTeX(self, text4)
		self.wait(3)
#公式上色进阶
class ColorByCaracter(Scene):
	def construct(self):
		text = TexMobject("{d","\\over","d","x","}","\\int_","{a}^","{","x","}","f(","t",")d","t","=","f(","x",")")
		#text1 = TexMobject("\\frac{","\\mathrm","{d","}"," }","{","\\mathrm","{","d}"," x}", "\\int_{","a}","^{","x}"," f","(t)","\\mathrm{","d}","t" ,"=" ,"f","(","x",")")
		text1.set_color_by_tex("x",RED)
		self.play(Write(text))
		#self.play(Write(text1))
		self.wait(2)
'''##!!公式字上色，还需要学习latex。'''
class ForTwoVariables(Scene):
	def construct(self): #no usar siempre frac
		text = TexMobject("[0]","[1]","[2]","[3]","[4]","[5]","[6]","[7]")
		for i,color in [(2,RED),(4,PINK)]:
			text[i].set_color(color)
		self.play(Write(text))
		self.wait(3)
#两个变量上色
class ColoringText(Scene):
	def construct(self):
		text = TextMobject("Text or object")
		self.add(text)
		self.wait(0.5)
		for letter in text:
			self.play(LaggedStart(
				letter,
				lambda m: (m.set_color, YELLOW)
			))
		self.wait(0.5)
'''##!!字符串上色，新旧版本，需要理解'''
class FrameBox1(Scene):
	def construct(self):
		text=TexMobject(
			"\\hat g(", "f", ")", "=", "\\int", "_{t_1}", "^{t_{2}}",
			"g(", "t", ")", "e", "^{-2\\pi i", "f", "t}", "dt"
		)
		frameBox = SurroundingRectangle(text[4], buff = 0.2*SMALL_BUFF,color=BLUE)
		seleccion = VGroup(text[7], text[8], text[9])
		frameBox2 = SurroundingRectangle(seleccion, buff=0.5 * SMALL_BUFF)
		frameBox2.set_stroke(GREEN, 9)
		cross = Cross(text[11])
		cross.set_stroke(RED, 6)
		eq = VGroup(text[2], text[3])
		cross2= Cross(eq)
		cross2.set_stroke(PINK, 3)
		self.play(Write(text))
		self.wait(.5)
		self.play(ShowCreation(frameBox))
		self.wait(.5)
		self.play(ShowCreation(frameBox2))
		self.wait(.5)
		self.play(ShowCreation(cross))
		self.wait(.5)
		self.play(ShowCreation(cross2))
		self.wait(2)
#框框及叉叉
class BraceText(Scene):
	def construct(self):
		text=TexMobject(
			"\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
			"g(x)\\frac{d}{dx}f(x)"
		)
		self.play(Write(text))
		brace_top = Brace(text[1], UP, buff = SMALL_BUFF)
		brace_bottom = Brace(text[3], DOWN, buff = SMALL_BUFF)
		text_top = brace_top.get_text("$g'f$")
		text_bottom = brace_bottom.get_text("$f'g$")
		self.play(
			GrowFromCenter(brace_top),
			GrowFromCenter(brace_bottom),
			FadeIn(text_top),
			FadeIn(text_bottom)
			)
		self.wait()
#上框及下框
class TransformIssues(Scene):
	def construct(self):
		#                   0   1   2
		text_1=TextMobject("A","B","C")
		#                   0
		text_2=TextMobject("B")

		text_2.next_to(text_1,UP,buff=1)

		#Add the elements 0 and 2 of text_1 to screen and text_2
		self.play(
					*[
						FadeIn(text_1[i])
						for i in [0,2]
					],
					FadeIn(text_2)
			)

		self.wait()

		self.play(
					ReplacementTransform(text_2[:],text_1[1])
			)

		self.wait()
#物体变换，貌似并没有贝多芬发现的问题，不管加不加：
class CopyTextV1(Scene):
	def construct(self):
		formula = TexMobject(
			"\\frac{d}{dx}", #0
			"(", #1
			"u", #2
			"+", #3
			"v", #4
			")", #5
			"=", #6
			"\\frac{d}{dx}", #7
			"u", #8
			"+", #9
			"\\frac{d}{dx}", #10
			"v" #11
			)
		formula.scale(2)
		for letter, color in [("u", RED), ("v", BLUE)]:
			formula.set_color_by_tex(letter, color)
		self.play(Write(formula[0:7]))
		#这里只能到第六个
		self.wait()
		self.play(
			ReplacementTransform(formula[2].copy(),formula[8]),
			ReplacementTransform(formula[4].copy(),formula[11]),
			ReplacementTransform(formula[3].copy(),formula[9])
			)
		self.wait()
		self.play(
			ReplacementTransform(formula[0].copy(),formula[7]),
			ReplacementTransform(formula[0].copy(),formula[10])
			)
		self.wait()
		self.add(formula)
		debugTeX(self, formula)
		self.wait(3)
#公式复制及上色
class CopyTwoFormulas2(Scene):
	def construct(self):
		formula1 = TexMobject(
				"\\neg","\\forall","x",":","P(x)"
			)
		formula2 = TexMobject(
				"\\exists","x",":","\\neg","P(x)"
			)
		for tam,pos,formula in [(2,2*UP,formula1),(2,2*DOWN,formula2)]:
			formula.scale(tam)
			formula.move_to(pos)
		self.play(Write(formula1))
		self.wait(3)
		changes = [
			# First time
			[(2,3,4),
			# | | |
			# v v v
			 (1,2,4)],
			# Second time
			[(0,),
			# |
			# v
			 (3,)],
			# Third time
			[(1,),
			# |
			# v
			 (0,)]
		]
		for pre_ind,post_ind in changes:
			self.play(*[
				ReplacementTransform(
					formula1[i].copy(),formula2[j]
					)
				for i,j in zip(pre_ind,post_ind)
				],
					  #zip将两个表打包成元组
				run_time=2
			)
			self.wait()
#公式变换，有个骚操作可以学一下
class ChangeColorAndSizeAnimation(Scene):
	def construct(self):
		text = TextMobject("T", "e", "x", "t")
		text.scale(2)
		text.shift(LEFT*2)
		self.play(Write(text))
		self.wait()
		self.play(
                text.shift, RIGHT*2,
                text.scale, 2,
                text[2].set_color, RED,
				text[2].next_to(text[1],RIGHT,buff=1),
				text[2].scale, 2,
                run_time=2,
            )
		self.wait(2)
'''想实现字符串中一个字边移动边变大边变色，差一点意思'''
