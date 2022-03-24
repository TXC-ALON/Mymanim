from manimlib.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L
def HSL(hue, saturation=1, lightness=0.5):
    return Color(hsl=(hue, saturation, lightness))


def annularsec():
    ann = VGroup()
    for i in range(36):
        ann_pre_sec = AnnularSector(
            outer_radius=3,
            inner_radius=2.5,
            fill_opacity=1,
            start_angle=0+i*PI/18,
            angle=PI/18+PI/180,
            # Gradient direction
            stroke_width=0)
        ann_pre_sec.set_color(Color(hsl=(i/36, 1, 0.5)))
        ann.add(ann_pre_sec)
    return ann

def annularsec2():
    ann = VGroup()
    for i in range(36):
        ann_pre_sec = AnnularSector(
            outer_radius=3,
            inner_radius=2.5,
            fill_opacity=1,
            start_angle=0+i*PI/18,
            angle=PI/18,
            # Gradient direction
            stroke_width=0)
        ann_pre_sec.set_color(Color(hsl=(i/36, 1, 0.7)))
        ann.add(ann_pre_sec)
    return ann

class TestObject(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }
    def construct(self):
        # object
        ann_sec = AnnularSector(
            outer_radius=3,
            inner_radius=2.5,
            fill_opacity=1,
            start_angle=0,
            angle=PI / 3,
            # Gradient direction
            sheen_direction=RIGHT,
            stroke_width=0
        )
        ann_sec.set_color(color=self.get_hsl_set_colors())
        ann_sec.to_edge(LEFT)
        y = annularsec()
        self.play(ShowCreation(ann_sec))
        self.wait()
        self.play(ShowCreation(y),run_time = 6)
        self.wait(3)

    def get_hsl_set_colors(self, saturation=1, lightness=0.5):
        return [*[HSL(i / 360, saturation, lightness) for i in range(360)]]
