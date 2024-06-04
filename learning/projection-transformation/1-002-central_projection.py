import time

from manim import *
from manim.mobject.opengl.opengl_point_image_mobject import ImagePixelMobject, NumpyImage, ImageBox
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface, OpenGLSurface
import numpy as np
from rich.progress import track
from PIL import Image


class CentralProjectionBase(ThreeDScene):
    def construct(self):

        point1=[1,1,2]
        dot= Dot3D(point=point1,color=YELLOW)
        self.add(dot)
        equation1 = MathTex(R"""1x+2y+2z-2=0""")
        self.add_fixed_in_frame_mobjects(equation1.to_corner(UL))
        position_list = [
            [2, 2, -1],
            [2, -2, 2],
            [-2, -2, 5],
            [-2, 2, 2],
        ]
        square1 = Polygon(*position_list, color=PURPLE_B,fill_color=BLUE,fill_opacity=0.5)
        self.add(square1)

        self.set_camera_orientation(theta=35*DEGREES,phi=65*DEGREES)

        axes = ThreeDAxes(include_numbers=False, x_range=[-7, 7, 1], y_range=[-5, 5, 1], z_range=[-4, 4, 1],x_length=14, y_length=10, z_length=6)
        axes.add(axes.get_axis_labels())
        self.add(axes)

        self.begin_ambient_camera_rotation(rate=1)
        self.wait(2)



class CentralProjection001(ThreeDScene):
    def construct(self):
        point1 = [1, 1, 2]
        dot = Dot3D(point=point1, color=YELLOW)
        self.add(dot)
        equation1 = MathTex(R"""1x+2y+2z-2=0""")
        self.add_fixed_in_frame_mobjects(equation1.to_corner(UL))
        position_list = [
            [2, 2, -2],
            [2, -2, 2],
            [-2, -2, 4],
            [-2, 2, 1],
        ]
        square1 = Polygon(*position_list, color=PURPLE_B, fill_color=BLUE, fill_opacity=0.5)
        self.add(square1)

        self.set_camera_orientation(theta=35 * DEGREES, phi=65 * DEGREES)

        axes = ThreeDAxes(include_numbers=False, x_range=[-7, 7, 1], y_range=[-5, 5, 1], z_range=[-4, 4, 1],
                          x_length=14, y_length=10, z_length=6)
        axes.add(axes.get_axis_labels())
        self.add(axes)

        image_array = np.array(Image.open("src/test.jpg").convert("RGBA"))
        image = NumpyImage(image_array=image_array, distance=0.01, stroke_width=2)
        self.play(Create(image))

        # 1x+2y+2z-2=0;
        a=1;  b=2;  c=2; d=-2
        xo=1; yo=1 ; zo=2
        # x=1;y=1;z=1
        # t = -(a * xo + b * yo + c * zo + d) / a * x - a * xo + b * y - b * yo + c * z - c * zo
        # x1 = xo + t * (x - xo);
        # y1 = yo + t * (y - yo);
        # z1 = zo + t * (z - zo)

        new_points=[]
        for point in image.points:
            x = point[0]
            y = point[1]
            z = point[2]

            t = -(a * xo + b * yo + c * zo + d) / (a * x - a * xo + b * y - b * yo + c * z - c * zo)

            x1 = xo + t * (x - xo);
            y1 = yo + t * (y - yo);
            z1 = zo + t * (z - zo)
            new_point=[x1,y1,z1]
            new_points.append(new_point)

        self.begin_ambient_camera_rotation(rate=1)
        self.play(ApplyMethod(image.set_points,np.array(new_points)))
        self.wait(5)





with tempconfig({"preview": True, "disable_caching": False, "renderer": "opengl"}):
    CentralProjection001().render()
    exit(1)
