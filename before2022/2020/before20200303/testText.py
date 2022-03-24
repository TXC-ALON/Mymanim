from manimlib.imports import *


# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L
# SizeTextOnLaTeX

class STOL(Scene):
  def construct(self):
    textHuge = TextMobject("{\\Huge Huge Text 17pt.\\#!?} Text")
    texthuge = TextMobject("{\\huge huge Text 14pt.\\#!?} Text")
    textLARGE = TextMobject("{\\LARGE LARGE Text 12pt.\\#!?} Text")
    textLarge = TextMobject("{\\Large Large Text 11pt.\\#!?} Text")
    textlarge = TextMobject("{\\large large Text 10pt.\\#!?} Text")
    textNormal = TextMobject("{\\normalsize normal Text 8pt.\\#!?} Text")
    textsmall = TextMobject("{\\small small Text 7pt.\\#!?} Text")
    textfootnotesize = TextMobject("{\\footnotesize footnotesize Text 6pt.\\#!?} Text")
    textscriptsize = TextMobject("{\\scriptsize scriptsize Text 5pt.\\#!?} Text")
    texttiny = TextMobject("{\\tiny tiny Texto 5pt.\\#!?} Text")
    # textcommand = TextMobject("{\\command command Text 8pt.\\#!?} Text")
    textHuge.to_edge(UP)
    texthuge.next_to(textHuge, DOWN, buff=0.1)
    textLARGE.next_to(texthuge, DOWN, buff=0.1)
    textLarge.next_to(textLARGE, DOWN, buff=0.1)
    textlarge.next_to(textLarge, DOWN, buff=0.1)
    textNormal.next_to(textlarge, DOWN, buff=0.1)
    textsmall.next_to(textNormal, DOWN, buff=0.1)
    textfootnotesize.next_to(textsmall, DOWN, buff=0.1)
    textscriptsize.next_to(textfootnotesize, DOWN, buff=0.1)
    texttiny.next_to(textscriptsize, DOWN, buff=0.1)
    # textcommand.next_to(texttiny, DOWN, buff=0.1)
    # self.play(ShowCreation(textHuge, texthuge, textLARGE, textLarge, textlarge, textNormal, textsmall, textfootnotesize,
    #          textscriptsize, texttiny,textcommand))
    self.add(textHuge, texthuge, textLARGE, textLarge, textlarge, textNormal, textsmall, textfootnotesize,
             textscriptsize, texttiny)
    self.wait(4)
