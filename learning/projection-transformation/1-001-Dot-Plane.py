import time

from manim import *
from manim.mobject.opengl.opengl_point_image_mobject import ImagePixelMobject, NumpyImage, ImageBox
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface, OpenGLSurface
import numpy as np
from rich.progress import track
from PIL import Image

class DotPlane001(ThreeDScene):


    def construct(self):

        self.set_camera_orientation(phi=65*DEGREES,theta= 35*DEGREES)
        axes = ThreeDAxes(include_numbers=False, x_range=[-7, 7, 1], y_range=[-5, 5, 1], z_range=[-4, 4, 1],
                          x_length=14, y_length=10, z_length=6)
        axes.add(axes.get_axis_labels())

        point1=[3,3,3]
        point2=[1,1,1]

        dot1 = Dot3D(point=point1,color=YELLOW)
        dot2 = Dot3D(point=point2, color=BLUE)


        line1= Line3D(start=point1,end=point2,thickness=0.01,color=YELLOW)
        line2 = Line3D(start=ORIGIN, end=point2,thickness=0.01)

        square = Square(color=BLUE, side_length=4)
        square.shift([0, 0, 1])
        square.set_fill(BLUE, opacity=0.5)

        self.add(square,axes,line1,line2,dot1,dot2,)


class DotPlane002(ThreeDScene):
    def construct(self):

        axes = ThreeDAxes(include_numbers=False, x_range=[-7, 7, 1], y_range=[-5, 5, 1], z_range=[-4, 4, 1],x_length=14, y_length=10, z_length=6)

        axes.add(axes.get_axis_labels())

        point1=[3,3,3]
        point2=[1,1,1]

        dot1 = Dot(point=point1,color=YELLOW)
        dot1_lable=MathTex(r"""P(x,y,z)""")
        dot1_lable.next_to(dot1)



        dot2 = Dot(point=point2, color=BLUE)
        dot2_lable = MathTex(r"""P'(x',y',z')""")
        dot2_lable.next_to(dot2)



        dot3 = Dot(point=ORIGIN, color=BLUE)
        dot3_lable = MathTex(r"""O(0,0,0)""")
        dot3_lable.next_to(dot3)


        line1= Line(start=point1,end=point2,color=YELLOW)
        line2 = Line(start=ORIGIN, end=point2)

        line=DashedLine(start=[1,-5,0],end=[1,5,0],color=BLUE)

        # square = Square(color=BLUE, side_length=4)
        # square.shift([0, 0, 1])
        # square.set_fill(BLUE, opacity=0.5)

        self.add(line,axes,line1,line2,dot1,dot2,dot1_lable,dot2_lable,dot3,dot3_lable)

class DotInLine001(ThreeDScene):
    def construct(self):

        axes = ThreeDAxes(include_numbers=False, x_range=[-7, 7, 1], y_range=[-5, 5, 1], z_range=[-4, 4, 1],x_length=14, y_length=10, z_length=6)

        axes.add(axes.get_axis_labels())

        point1=[3,3,3]
        point2=[1,1,1]
        point3 = [-2, -2, -2]

        dot1 = Dot(point=point1,color=YELLOW)
        dot1_lable=MathTex(r"""P_1(x_1,y_1,z_1)""")
        dot1_lable.next_to(dot1)

        dot2 = Dot(point=point2, color=YELLOW)
        dot2_lable = MathTex(r"""P_2(x_2,y_2,z_2)""")
        dot2_lable.next_to(dot2)

        dot3 = Dot(point=point3, color=YELLOW)
        dot3_lable = MathTex(r"""P_3(x_3,y_3,z_3)""")
        dot3_lable.next_to(dot3)


        line1= Line(start=[-5,-5,-5],end=[5,5,5],color=BLUE)

        self.add(line1,dot1,dot2,dot1_lable,dot2_lable,dot3,dot3_lable)



with tempconfig({"preview": True, "disable_caching": False, "renderer": "opengl"}):
    DotInLine001().render()
    exit(1)
