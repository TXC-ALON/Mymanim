from manimlib.imports import *


# 用途
class Formula(Scene):

  def construct(self):
    # object
    formula_tex1 = TexMobject(
      r"\frac { d }{ dx } f\left( x \right) =\lim _{ x\rightarrow 0 }{ \frac { \sin { x }  }{ x }  } +\lim _{ h\rightarrow 0 }{ \frac { f\left( x+h \right) -f\left( x \right)  }{ h }  } ")
    formula_tex1.scale(0.8)
    formula_tex2 = TexMobject(
      "\\frac { d }{ dx } f\left( x \\right) =\lim _{ x\\rightarrow 0 }{ \\frac { \sin { x }  }{ x }  } +\lim _{ h\\rightarrow 0 }{ \\frac { f\left( x+h \\right) -f\left( x \\right)  }{ h }  } ")
    formula_tex2.scale(0.8)
    formula_tex3 = TexMobject("{", "a", "\\over", "b", "}")
    matrix_tex = TexMobject(r"""
    \begin{bmatrix} a & b & c \\ d & e & f \\ g & h & 3 \end{bmatrix}
    """)
    matrix_tex.scale(0.8)
    # position
    formula_tex1.move_to([0, 1, 0])
    formula_tex2.move_to([0, -1, 0])
    matrix_tex.to_corner(DL)
    matrix_tex.shift([0,2.5,0])
    # show
    self.add(formula_tex1)
    self.add(formula_tex2)
    self.add(formula_tex3)
    self.add(matrix_tex)
