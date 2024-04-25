import numpy as np

from manim import *
from manim.mobject.opengl.opengl_vectorized_mobject import OpenGLVMobject


class IntegerMatrixExample(Scene):
    def construct(self):
        array=  np.zeros((3,5))
        matrix = IntegerMatrix(array,v_buff=0.4,h_buff=0.4,add_background_rectangles_to_entries =True)
        row:OpenGLVMobject= matrix.get_rows()[1]
        row.set_fill(YELLOW_A)
        column:OpenGLVMobject= matrix.get_columns()[3]
        column.set_fill(RED)

        self.add(matrix)
        self.wait()
        self.wait()


class GetRowsExample(Scene):
    def construct(self):
        matrix = Matrix([["\pi", 3], [1, 5]],v_buff=0.5,h_buff=0.5)
        row1:OpenGLVMobject= matrix.get_rows()[1]
        matrix.add( row1.set_color(YELLOW_A))
        self.add(matrix)



class SetRowColorsExample(Scene):
    def construct(self):
        m0 = Matrix([["\pi", 1], [-1, 3]],
        ).set_row_colors([RED,BLUE], GREEN)
        self.add(m0)
class MobjectMatrixExample(Scene):
    def construct(self):
        a = Circle().scale(0.3)
        b = Square().scale(0.3)
        c = MathTex("\pi").scale(2)
        d = Star().scale(0.3)
        m0 = MobjectMatrix([[a, b], [c, d]])
        self.add(m0)

with tempconfig({"preview": True, "disable_caching": True, "renderer": "opengl"}):
    IntegerMatrixExample().render()
    exit(1)