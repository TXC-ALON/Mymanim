from manimlib.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L



class Euler(Scene):

    def construct(self):
        # object
        Euler_Tex = TexMobject("e^{ix} =cosx+isinx")
        Ex_Tylor_Tex = TexMobject(
            "e^{x} = 1+\\frac{x}{1!} +\\frac{x^{2} }{2!} +\\frac{x^{3} }{3!} +\\frac{x^{4} }{4!} +\\frac{x^{5} }{5!}\\dots")
        Sinx_Tylor_Tex = TexMobject("sin{x} = x-\\frac{x^{3} }{3!} +\\frac{x^{5} }{5!}\\dots ")
        Cosx_Tylor_Tex = TexMobject("cos{x} = 1-\\frac{x^{2} }{2!} +\\frac{x^{4} }{4!}\\dots ")
        TEX1 = VGroup(Euler_Tex, Ex_Tylor_Tex, Sinx_Tylor_Tex, Cosx_Tylor_Tex).arrange(DOWN, buff=0.4)

        # Ex_Tylor_Tex[2].move_to(np.array([Euler_Tex[3].get_center()[0], Ex_Tylor_Tex[0].get_center()[1], 0]))
        # Sinx_Tylor_Tex[4].move_to(np.array([Euler_Tex[3].get_center()[0], Sinx_Tylor_Tex[0].get_center()[1], 0]))
        # Cosx_Tylor_Tex[4].move_to(np.array([Euler_Tex[3].get_center()[0], Cosx_Tylor_Tex[0].get_center()[1], 0]))
        # 失败，list index out of range

        # position

        # show
        debugTeX(self, TEX1[0][0])
        # debugTeX(self, TEX1[1][0])
        # debugTeX(self, TEX1[2][0])
        # debugTeX(self, TEX1[3][0])
        self.play(ShowCreation(TEX1), run_time=4)

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
