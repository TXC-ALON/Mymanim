from manimlib.imports import *
from manim_sandbox.utils.imports import *

class RateFunctions(Scene):
    def construct(self):
        title = VGroup(
            Text("linear", font="Monaco for Powerline").scale(0.5),
            Text("smooth", font="Monaco for Powerline").scale(0.5),
            Text("rush_into", font="Monaco for Powerline").scale(0.5),
            Text("rush_from", font="Monaco for Powerline").scale(0.5),
            Text("slow_into", font="Monaco for Powerline").scale(0.5),
            Text("double_smooth", font="Monaco for Powerline").scale(0.5),
            Text("there_and_back", font="Monaco for Powerline").scale(0.5)
        ).arrange_submobjects(
            DOWN, aligned_edge=RIGHT, buff=0.55
        ).move_to(LEFT*7, aligned_edge=LEFT)
        dots = VGroup(
            *[
                Dot(color=BLUE).move_to([-2.5, i, 0])
                for i in range(3, -4, -1)
            ]
        )
        transform_dots = VGroup(
            *[
                Dot(color=BLUE).move_to([6, i, 0], aligned_edge=DOWN)
                for i in range(3, -4, -1)
            ]
        )
        self.add(title, dots)
        self.wait(2)
        self.play(TransformFromCopy(dots[0], transform_dots[0], rate_func=linear))
        self.play(TransformFromCopy(dots[1], transform_dots[1], rate_func=smooth))
        self.play(TransformFromCopy(dots[2], transform_dots[2], rate_func=rush_into))
        self.play(TransformFromCopy(dots[3], transform_dots[3], rate_func=rush_from))
        self.play(TransformFromCopy(dots[4], transform_dots[4], rate_func=slow_into))
        self.play(TransformFromCopy(dots[5], transform_dots[5], rate_func=double_smooth))
        self.play(TransformFromCopy(dots[6], transform_dots[6], rate_func=there_and_back))
        self.wait(2)
        self.play(
            ReplacementTransform(dots[0], transform_dots[0], rate_func=linear),
            ReplacementTransform(dots[1], transform_dots[1], rate_func=smooth),
            ReplacementTransform(dots[2], transform_dots[2], rate_func=rush_into),
            ReplacementTransform(dots[3], transform_dots[3], rate_func=rush_from),
            ReplacementTransform(dots[4], transform_dots[4], rate_func=slow_into),
            ReplacementTransform(dots[5], transform_dots[5], rate_func=double_smooth),
            ReplacementTransform(dots[6], transform_dots[6], rate_func=there_and_back),
            run_time=3
        )
        self.wait(2)


class RateFunctions2(Scene):
    def construct(self):
        title = VGroup(
            Text("there_and_back_with_pause", font="Monaco for Powerline").scale(0.3),
            Text("running_start", font="Monaco for Powerline").scale(0.3),
            Text("wiggle", font="Monaco for Powerline").scale(0.3),
            Text("lingering", font="Monaco for Powerline").scale(0.3),
            Text("exponential_decay", font="Monaco for Powerline").scale(0.3)
        ).arrange_submobjects(
            DOWN, aligned_edge=RIGHT, buff=0.65
        ).move_to(LEFT*7, aligned_edge=LEFT)
        dots = VGroup(
            *[
                Dot(color=BLUE).move_to([-2, i, 0])
                for i in range(2, -3, -1)
            ]
        )
        transform_dots = VGroup(
            *[
                Dot(color=BLUE).move_to([6, i, 0], aligned_edge=DOWN)
                for i in range(2, -3, -1)
            ]
        )
        self.add(title, dots)
        self.wait(2)
        self.play(
            Transform(dots[0], transform_dots[0], rate_func=there_and_back_with_pause),
            Transform(dots[1], transform_dots[1], rate_func=running_start),
            Transform(dots[2], transform_dots[2], rate_func=wiggle),
            Transform(dots[3], transform_dots[3], rate_func=lingering),
            Transform(dots[4], transform_dots[4], rate_func=exponential_decay),
            run_time=3
        )
        self.wait(2)


class RateFunctions3(Scene):
    def construct(self):
        mover = Dot(color=BLUE).move_to(UR)
        targets = [
            Dot(color=BLUE).move_to(DR),
            Dot(color=BLUE).move_to(DL),
            Dot(color=BLUE).move_to(UL)
        ]
        self.wait()
        self.add(mover)
        self.wait(2)
        self.play(Succession(
            *[
                Transform(mover, target, rate_func=linear)
                for target in targets
            ],
            run_time = 5
        ))
        self.wait(2)

