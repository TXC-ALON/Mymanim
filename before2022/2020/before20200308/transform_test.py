from manimlib.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class Trans(Scene):

  def construct(self):
    M1 = TextMobject("A")
    M2 = TextMobject("B")
    M3 = TextMobject("这是Transform")
    M4 = TextMobject("这是ReplacementTransform")

    self.add(M1)
    self.wait()
    self.play(Transform(M1, M3))
    self.wait()
    self.clear()
    self.add(M2)
    self.wait()
    self.play(ReplacementTransform(M2, M4))
    self.wait()


class Trans_2(Scene):

  def construct(self):
    TEXT_1 = TextMobject("这是Transform")
    TEXT_2 = TextMobject("这是ReplacementTransform")
    M = TextMobject("A", "B", "C", "D", "E")
    screen_grid = ScreenGrid()
    self.play(ShowCreation(TEXT_1))
    self.play(FadeOut(TEXT_1))
    self.play(ShowCreation(screen_grid))
    self.add(M[0])
    self.wait()
    self.play(Transform(M[0], M[1]))
    self.play(Transform(M[1], M[2]))
    self.play(Transform(M[2], M[3]))
    self.play(Transform(M[3], M[4]))
    self.wait()
    M[0].set_color(RED)
    # M[0].move_to([0, 1, 0])
    self.play(ShowCreation(M[0]))
    self.play(ShowCreation(M))

    self.clear()
    M2 = TextMobject("A", "B", "C", "D", "E")
    self.wait()
    self.play(ShowCreation(TEXT_2))
    self.play(FadeOut(TEXT_2))
    self.add(screen_grid)
    self.add(M2[0])
    self.wait()
    self.play(ReplacementTransform(M2[0], M2[1]))
    self.play(ReplacementTransform(M2[1], M2[2]))
    self.play(ReplacementTransform(M2[2], M2[3]))
    self.play(ReplacementTransform(M2[3], M2[4]))
    self.wait()
    M2[0].set_color(GREEN)
    self.play(ShowCreation(M2[0]))
    self.play(ShowCreation(M2))


class CopyTextV1(Scene):
  def construct(self):
    formula = TexMobject(
      "\\frac{d}{dx}",  # 0
      "(",  # 1
      "u",  # 2
      "+",  # 3
      "v",  # 4
      ")",  # 5
      "=",  # 6
      "\\frac{d}{dx}",  # 7
      "u",  # 8
      "+",  # 9
      "\\frac{d}{dx}",  # 10
      "v"  # 11
    )
    formula.scale(2)
    self.play(Write(formula[0:7]))
    self.wait()
    self.play(
      ReplacementTransform(formula[2], formula[8]),
      ReplacementTransform(formula[4], formula[11]),
      ReplacementTransform(formula[3].copy(), formula[9])

    )
    self.wait()
    self.play(
      ReplacementTransform(formula[0], formula[7]),
      ReplacementTransform(formula[0].copy(), formula[10])

    )
    self.wait()


class CopyTextV2(Scene):
  def construct(self):
    formula = TexMobject("\\frac{d}{dx}",
                         "(", "u", "+", "v", ")", "=",
                         "\\frac{d}{dx}", "u", "+", "\\frac{d}{dx}", "v"

                         )
    formula.scale(2)
    self.play(Write(formula[0:7]))
    self.wait()
    self.play(
      ReplacementTransform(formula[2].copy(), formula[8]),
      ReplacementTransform(formula[4].copy(), formula[11]),
      ReplacementTransform(formula[3].copy(), formula[9])
    )
    self.wait()
    self.play(
      ReplacementTransform(formula[0].copy(), formula[7]),
      ReplacementTransform(formula[0].copy(), formula[10])
    )
    self.wait()


class TextLike1DArrays(Scene):
  def construct(self):
    text = TextMobject("Te", "xt")
    # text=TextMobject("Te","xt")[0] # <- Recent versions
    for i in text:
      self.play(FadeIn(i))
      self.wait()
      self.play(FadeOut(i))
    self.wait()


class TextLike2DArraysV1(Scene):
  def construct(self):
    text = TextMobject("Te", "xt")
    # text=TextMobject("Te","xt")[0] # <- Recent versions
    self.play(FadeIn(text[0][0]))
    self.play(FadeIn(text[0][1]))
    self.play(FadeIn(text[1][0]))
    self.play(FadeIn(text[1][1]))
    self.wait()


class TextLike2DArraysV2(Scene):
  def construct(self):
    text = TextMobject("Te", "xt")
    for i in text:
      for j in i:
        self.play(FadeIn(j))

    self.wait()


class TextLike2DArraysV3(Scene):
  def construct(self):
    text = TextMobject("Te", "xt")
    # text=TextMobject("Te","xt")[0] # <- Recent versions
    for i in range(len(text)):
      for j in range(len(text[i])):
        self.play(FadeIn(text[i][j]))

    self.wait()


class TransformIssues(Scene):
  def construct(self):
    #                   0   1   2
    text_1 = TextMobject("A", "B", "C")
    # text_1=TextMobject("A","B","C")[0] # <- Recent versions
    #                   0
    text_2 = TextMobject("B")
    # text_2=TextMobject("B")[0]

    text_2.next_to(text_1, UP, buff=1)

    # Add the elements 0 and 2 of text_1 to screen and text_2
    self.play(
      *[
        FadeIn(text_1[i])
        for i in [0, 2]
      ],
      FadeIn(text_2)
    )

    self.wait()

    self.play(
      ReplacementTransform(text_2, text_1[1])
    )

    self.wait()


class TransformVGroup(Scene):
  def construct(self):
    text_n = TextMobject("A")
    text_v = VGroup(TextMobject("A")).next_to(text_n, DOWN)

    self.play(Write(text_n))

    self.play(ReplacementTransform(text_n, text_v))
    # Solution
    #         ReplacementTransform(text_n,text_v[0])
    self.wait()


class TransformIssuesSolution1(Scene):
  def construct(self):
    #                   0   1   2
    text_1 = TextMobject("A", "B", "C")
    # text_1=TextMobject("A","B","C")[0] # <- Recent versions
    #                   0
    text_2 = TextMobject("B")
    # text_2=TextMobject("B")[0]

    text_2.next_to(text_1, UP, buff=1)

    # Add the elements 0 and 2 of text_1 to screen and text_2
    self.play(
      *[
        FadeIn(text_1[i])
        for i in [0, 2]
      ],
      FadeIn(text_2)
    )

    self.wait()

    self.play(
      # Add [:] to the firts or second parameter
      ReplacementTransform(text_2[:], text_1[1])
    )

    self.wait()


class TransformIssuesSolutionInfallible(Scene):
  def construct(self):
    #                   0   1   2
    text_1 = TextMobject("A", "B", "C")
    # text_1=TextMobject("A","B","C")[0] # <- Recent versions
    #                   0
    text_2 = TextMobject("B")
    # text_2=TextMobject("B")[0]

    text_2.next_to(text_1, UP, buff=1)

    # Create a copy of the objects

    text_1_1_c = TextMobject("B") \
      .match_style(text_1[1]) \
      .match_width(text_1[1]) \
      .move_to(text_1[1])

    # Add the elements 0 and 2 of text_1 to screen and text_2
    self.play(
      *[
        FadeIn(text_1[i])
        for i in [0, 2]
      ],
      FadeIn(text_2)
    )

    self.wait()

    self.play(
      # Add [:] to the firts or second parameter
      ReplacementTransform(text_2, text_1_1_c)
    )
    self.remove(text_1_1_c)
    self.add(text_1[1])

    self.wait()


class CopyText3(Scene):
  def construct(self):
    formula = TexMobject("\\frac{d}{dx}",
                         "(", "u", "+", "v", ")", "=",
                         "\\frac{d}{dx}", "u", "+", "\\frac{d}{dx}", "v"
                         )
    formula.scale(2)
    self.play(Write(formula[0:7]))
    self.wait()
    changes = [
      # step1
      [(2, 4, 3),
       # | | |
       # v v v
       (8, 11, 9)],
      # step2
      [(0, 0),
       # | |
       # v v
       (7, 10)]
    ]
    for pre_ind, post_ind in changes:
      self.play(
        *[
          ReplacementTransform(formula[i].copy(), formula[j])
          for i, j in zip(pre_ind, post_ind)
        ]
      )
      self.wait()


class ChangeColorAndSizeAnimation(Scene):
  def construct(self):
    text = TextMobject("Text")
    self.play(Write(text))

    text.generate_target()
    text.target = TextMobject("Target")
    text.target.set_color(RED)
    text.target.scale(2)
    text.target.shift(LEFT)

    self.play(MoveToTarget(text), run_time=2)
    self.wait()
