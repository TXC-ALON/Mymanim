from manimlib.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L
def debugTeX(self, texm):
    for i, j in enumerate(texm):
        tex_id = Text(str(i), font="Euclid").scale(0.5).set_color(RED_D)
        tex_id.move_to(j)
        self.add(tex_id)


class Euler2(Scene):

    def construct(self):
        # object
        Tylor_Expansion = TexMobject(
            r'''\begin{cases}
            e^{ix}&=\cos x+i\sin x\\
            e^{x}&= 1+\displaystyle\frac{x}{1!} +\frac{x^{2} }{2!} +\frac{x^{3} }{3!} +\frac{x^{4} }{4!} +\frac{x^{5} }{5!}\dots\\
            \sin{x}&= x-\displaystyle\frac{x^{3} }{3!} +\frac{x^{5} }{5!}\dots\\
            \cos{x}&= 1-\displaystyle\frac{x^{2} }{2!} +\frac{x^{4} }{4!}\dots
            \end{cases}
            ''')

        # self.add(Tylor_Expansion)
        debugTeX(self, Tylor_Expansion[0])

        Euler_Tex = Tylor_Expansion[0][17:31]
        Ex_Tylor_Tex = Tylor_Expansion[0][31:67]
        Sinx_Tylor_Tex = Tylor_Expansion[0][67:88]
        Cosx_Tylor_Tex = Tylor_Expansion[0][88:]
        TEX1 = VGroup(Euler_Tex, Ex_Tylor_Tex, Sinx_Tylor_Tex, Cosx_Tylor_Tex)  # .arrange(DOWN, buff=0.4)
        self.add(TEX1)
        self.play(ShowCreation(TEX1), run_time=5)
        self.wait(3)


class Euler8(Scene):

    def construct(self):
        # object
        Tylor_Expansion = TexMobject(
            r'''
            e^{ix}&=\cos x&+i\sin x\\
            e^{x}&= 1&+\displaystyle\frac{x}{1!} +\frac{x^{2} }{2!} +\frac{x^{3} }{3!} +\frac{x^{4} }{4!} +\frac{x^{5} }{5!}\dots\\
            \sin{x}&= x&-\displaystyle\frac{x^{3} }{3!} +\frac{x^{5} }{5!}\dots\\
            \cos{x}&= 1&-\displaystyle\frac{x^{2} }{2!} +\frac{x^{4} }{4!}\dots
            ''')

        self.add(Tylor_Expansion)
        debugTeX(self,Tylor_Expansion[0])

        Euler_Tex = Tylor_Expansion[0][0:14]
        Ex_Tylor_Tex = Tylor_Expansion[0][14:50]
        Sinx_Tylor_Tex = Tylor_Expansion[0][50:71]
        Cosx_Tylor_Tex = Tylor_Expansion[0][71:92]
        TEX1 = VGroup(Euler_Tex, Ex_Tylor_Tex, Sinx_Tylor_Tex, Cosx_Tylor_Tex)  # .arrange(DOWN, buff=0.4)
        self.add(TEX1)

class Euler7(Scene):
    def construct(self):
        # object
        Euler_Tex_1 = TexMobject("e^{ix}")
        Euler_Tex_2 = TexMobject("=")
        Euler_Tex_3 = TexMobject("cosx+isinx")
        Euler_Tex = VGroup(Euler_Tex_1,Euler_Tex_2,Euler_Tex_3).arrange(RIGHT,buff=0.3)

        Ex_Tylor_Tex_1 = TexMobject("e^{x} ")
        Ex_Tylor_Tex_2 = TexMobject("=")
        Ex_Tylor_Tex_3 = TexMobject("1+\\frac{x}{1!} +\\frac{x^{2} }{2!} +\\frac{x^{3} }{3!} +\\frac{x^{4} }{4!} +\\frac{x^{5} }{5!}\\dots")
        Ex_Tylor_Tex = VGroup(Ex_Tylor_Tex_1,Ex_Tylor_Tex_2,Ex_Tylor_Tex_3).arrange(RIGHT,buff=0.3)
        for i, item in enumerate(Ex_Tylor_Tex):
            item.align_to(Euler_Tex[i], LEFT)
        Ex_Tylor_Tex.shift(DOWN)

        Sinx_Tylor_Tex_1 = TexMobject("sin{x}")
        Sinx_Tylor_Tex_2 = TexMobject("=")
        Sinx_Tylor_Tex_3 = TexMobject("x-\\frac{x^{3} }{3!} +\\frac{x^{5} }{5!}\\dots ")
        Sinx_Tylor_Tex = VGroup(Sinx_Tylor_Tex_1,Sinx_Tylor_Tex_2,Sinx_Tylor_Tex_3).arrange(RIGHT,buff=0.3)
        for i, item in enumerate(Sinx_Tylor_Tex):
            item.align_to(Ex_Tylor_Tex[i], LEFT)
        Sinx_Tylor_Tex.shift(DOWN)

        Cosx_Tylor_Tex_1 = TexMobject("cos{x}")
        Cosx_Tylor_Tex_2 = TexMobject("=")
        Cosx_Tylor_Tex_3 = TexMobject("1-\\frac{x^{2} }{2!} +\\frac{x^{4} }{4!}\\dots ")
        Cosx_Tylor_Tex = VGroup(Cosx_Tylor_Tex_1,Cosx_Tylor_Tex_2,Cosx_Tylor_Tex_3).arrange(RIGHT,buff=0.3)
        for i, item in enumerate(Cosx_Tylor_Tex):
            item.align_to(Sinx_Tylor_Tex[i], LEFT)
        Cosx_Tylor_Tex.shift(DOWN)

        TEX1 = VGroup(Euler_Tex, Ex_Tylor_Tex, Sinx_Tylor_Tex, Cosx_Tylor_Tex).arrange(DOWN, buff=0.4)


        self.play(ShowCreation(TEX1),run_time = 5)

class textA(Scene):
    def construct(self):
        t1=TextMobject('大','家','好')

        t2=TexMobject("x",'y','z')
        for i,item in enumerate(t2):
            item.align_to(t1[i],RIGHT*20)
        t2.shift(DOWN)

        self.play(Write(t1))
        self.wait(2)
        self.play(Write(t2))