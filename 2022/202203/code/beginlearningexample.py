from manimlib import *

class InteractiveDevelopment(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)
        square = Square()

        self.play(ShowCreation(square))
        self.wait()
        self.embed()

class TextExample(Scene):
    def construct(self):
        # 想要正确运行这个场景，你需要确保你的计算机中安装了Consolas字体
        # 关于Text全部用法，请见https://github.com/3b1b/manim/pull/680
        text = Text("Here is a text", font="Consolas", font_size=90)
        difference = Text(
            """
            The most important difference between Text and TexText is that\n
            you can change the font more easily, but can't use the LaTeX grammar
            """,
            font="Arial", font_size=24,
            # t2c是一个由 文本-颜色 键值对组成的字典
            t2c={"Text": BLUE, "TexText": BLUE, "LaTeX": ORANGE}
        )
        VGroup(text, difference).arrange(DOWN, buff=1)
        self.play(Write(text))
        self.play(FadeIn(difference, UP))
        self.wait(3)

        fonts = Text(
            "And you can also set the font according to different words",
            font="Arial",
            t2f={"font": "Consolas", "words": "Impact"},
            t2c={"font": BLUE, "words": GREEN}
        )
        fonts.set_width(FRAME_WIDTH - 1)
        slant = Text(
            "And the same as slant and weight",
            font="Consolas",
            t2s={"slant": ITALIC},
            t2w={"weight": BOLD},
            t2c={"slant": ORANGE, "weight": RED}
        )
        VGroup(fonts, slant).arrange(DOWN, buff=0.8)
        self.play(FadeOut(text), FadeOut(difference, shift=DOWN))
        self.play(Write(fonts))
        self.wait()
        self.play(Write(slant))
        self.wait()

class TexTransformExample(Scene):
    def construct(self):
        to_isolate = ["B", "C", "=", "(", ")"]
        lines = VGroup(
            # 将多个参数传递给Tex，这些参数看起来被连接在一起作为一个表达式
            # 但整个mobject的每个submobject为其中的一个字符串
            # 例如，下面的Tex物件将有5个子物件，对应于表达式[A^2，+，B^2，=，C^2]
            Tex("A^2", "+", "B^2", "=", "C^2"),
            # 这里同理
            Tex("A^2", "=", "C^2", "-", "B^2"),
            # 或者，你可以传入关键字参数isolate，其中包含一个字符串列表
            # 这些字符串应该作为它们自己的子物件存在
            # 因此，下面的一行相当于它下面注释掉的一行
            Tex("A^2 = (C + B)(C - B)", isolate=["A^2", *to_isolate]),
            # Tex("A^2", "=", "(", "C", "+", "B", ")", "(", "C", "-", "B", ")"),
            Tex("A = \\sqrt{(C + B)(C - B)}", isolate=["A", *to_isolate])
        )
        lines.arrange(DOWN, buff=LARGE_BUFF)
        for line in lines:
            line.set_color_by_tex_to_color_map({
                "A": BLUE,
                "B": TEAL,
                "C": GREEN,
            })

        play_kw = {"run_time": 2}
        self.add(lines[0])
        # TransformMatchingTex将源和目标中具有匹配tex字符串的部分对应变换
        # 传入path_arc，使每个部分旋转到它们的最终位置，这种效果对于重新排列一个方程是很好的
        self.play(
            TransformMatchingTex(
                lines[0].copy(), lines[1],
                path_arc=90 * DEGREES,
            ),
            **play_kw
        )
        self.wait()

        self.play(
            TransformMatchingTex(lines[1].copy(), lines[2]),
            **play_kw
        )
        self.wait()
        # …这看起来很好，但由于在lines[2]中没有匹配"C^2"或"B^2"的tex，这些子物件会淡出
        # 而C和B两个子物件会淡入，如果我们希望C^2转到C，而B^2转到B，我们可以用key_map来指定
        self.play(FadeOut(lines[2]))
        self.play(
            TransformMatchingTex(
                lines[1].copy(), lines[2],
                key_map={
                    "C^2": "C",
                    "B^2": "B",
                }
            ),
            **play_kw
        )
        self.wait()

        # 也许我们想把^2上的指数转换成根号。目前，lines[2]将表达式A^2视为一个单元
        # 因此我们可能会需要创建同一line的新版本，该line仅分隔出A
        # 这样，当TransformMatchingTex将所有匹配的部分对应时，唯一的不匹配将是来自new_line2的"^2"
        # 和来自最终行的"\sqrt"之间的不匹配。通过传入transform_missmatches=True，它会将此"^2"转换为"\sqrt"
        new_line2 = Tex("A^2 = (C + B)(C - B)", isolate=["A", *to_isolate])
        new_line2.replace(lines[2])
        new_line2.match_style(lines[2])

        self.play(
            TransformMatchingTex(
                new_line2, lines[3],
                transform_mismatches=True,
            ),
            **play_kw
        )
        self.wait(3)
        self.play(FadeOut(lines, RIGHT))

        # 或者，如果您不想故意分解tex字符串，您可以使用TransformMatchingShapes
        # 它将尝试将源mobject的所有部分与目标的部分对齐，而不考虑每个部分中的子对象层次结构
        # 根据这些部分是否具有相同的形状（尽其所能）来自动匹配变换
        source = Text("the morse code", height=1)
        target = Text("here come dots", height=1)

        self.play(Write(source))
        self.wait()
        kw = {"run_time": 3, "path_arc": PI / 2}
        self.play(TransformMatchingShapes(source, target, **kw))
        self.wait()
        self.play(TransformMatchingShapes(target, source, **kw))
        self.wait()

class UpdatersExample2(Scene):
    def construct(self):
        square = Square()
        square.set_fill(BLUE_E, 1)

        brace = always_redraw(Brace, square, UP)

        text, number = label = VGroup(
            Text("Width = "),
            DecimalNumber(
                0,
                show_ellipsis=True,
                num_decimal_places=5,
                include_sign=True,
            )
        )
        label.arrange(LEFT)

        always(label.next_to, brace, UP)
        f_always(number.set_value, square.get_width)

        self.add(square, brace, label)

        self.play(
            square.animate.scale(2),
            rate_func=there_and_back,
            run_time=2,
        )
        self.wait()
        self.play(
            square.animate.set_height(3, stretch=True),
            run_time=3,
        )
        self.wait()
        self.play(
            square.animate.set_width(1),
            run_time=3
        )
        self.wait()

        now = self.time
        w0 = square.get_width()
        square.add_updater(
            lambda m: m.set_width(w0 * math.sin(self.time - now) + w0)
        )
        self.wait(4 * PI)

class CoordinateSystemExample(Scene):
    def construct(self):
        axes = Axes(
            # x轴的范围从-1到10，步长为1
            x_range=(-5, 5),
            # y轴的范围从-2到2，步长为0.5y-axis ranges from -2 to 10 with a step size of 0.5
            y_range=(-2, 2, 0.5),
            # 坐标系将会伸缩来匹配指定的height和width
            height=6,
            width=10,
            # Axes由两个NumberLine组成，你可以通过axis_config来指定它们的样式
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
            },
            # 或者，你也可以像这样分别指定各个坐标轴的样式
            y_axis_config={
                "include_tip": False,
            }
        )
        # add_coordinate_labels方法的关键字参数可以传入DecimalNumber来指定它的样式
        axes.add_coordinate_labels(
            font_size=20,
            num_decimal_places=1,
        )
        self.add(axes)

        # Axes从CoordinateSystem类派生而来，意思是可以调用Axes.coords_to_point
        # （缩写为Axes.c2p）将一组坐标与一个点相关联，如下所示：
        dot = Dot(color=RED)
        dot.move_to(axes.c2p(0, 0))
        self.play(FadeIn(dot, scale=0.5))
        self.play(dot.animate.move_to(axes.c2p(3, 2)))
        self.wait()
        self.play(dot.animate.move_to(axes.c2p(-2, -0.5)))
        self.wait()

        # 同样，你可以调用Axes.point_to_coords（缩写Axes.p2c）
        # print(axes.p2c(dot.get_center()))

        # 我们可以从轴上画线，以便更好地标记给定点的坐标在这里
        # always_redraw命令意味着在每一个新帧上重新绘制线来保证线始终跟随着点移动
        h_line = always_redraw(lambda: axes.get_h_line(dot.get_left()))
        v_line = always_redraw(lambda: axes.get_v_line(dot.get_bottom()))
        #todo 这里当点移动到负数位置就不好用了，待改进

        self.play(
            ShowCreation(h_line),
            ShowCreation(v_line),
        )
        self.play(dot.animate.move_to(axes.c2p(3, -2)))
        self.wait()
        self.play(dot.animate.move_to(axes.c2p(1, 1)))
        self.wait()

        # 如果我们把这个点固定在一个特定的坐标上，当我们移动轴时，它也会跟随坐标系移动
        f_always(dot.move_to, lambda: axes.c2p(1, 1))
        self.play(
            axes.animate.scale(0.5).to_corner(UL),
            run_time=2,
        )
        self.wait()