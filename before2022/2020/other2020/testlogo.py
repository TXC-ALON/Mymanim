from manimlib.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class TestLogo2(Scene):

    def construct(self):
        # object
        p1 = Polygon(ORIGIN, RIGHT, 2 * UP, stroke_width=0).set_fill(average_color(WHITE, BLUE_C), 1)
        p2 = Polygon(1.5 * RIGHT, 3 * UR, 3 * UP, stroke_width=0).set_fill(average_color(WHITE, "#C59978"), 1)
        p3 = Polygon(2 * RIGHT, 3 * RIGHT, 3 * RIGHT + 2 * UP, stroke_width=0).set_fill(average_color(RED, GREEN, PINK),
                                                                                        1)
        # position
        '''p1.move_to(UR * 2)
        p2.move_to(UL * 2)
        p3.move_to(DL * 2)
        '''
        part_ur = VGroup(p1, p2, p3).move_to([2.5, 1., 0] )
        part_ul = part_ur.copy().rotate(PI / 2, about_point=ORIGIN)
        part_dl = part_ur.copy().rotate(PI, about_point=ORIGIN)
        part_dr = part_ur.copy().rotate(3 * PI / 2, about_point=ORIGIN)

        logo = VGroup(part_dl,part_dr,part_ul,part_ur)
        # show
        '''self.play(ShowCreation(p1))
        self.wait()
        self.play(ShowCreation(p2))
        self.wait()
        self.play(ShowCreation(p3))
        self.wait()
    '''
        self.play(ShowCreation(VGroup(p1,p2,p3)))
        self.play(ShowCreation(logo),run_time=4,rate_fun=smooth)
        self.wait()


