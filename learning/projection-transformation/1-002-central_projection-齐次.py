import time

from manim import *
from manim.mobject.opengl.opengl_point_image_mobject import ImagePixelMobject, NumpyImage, ImageBox
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface, OpenGLSurface
import numpy as np
from rich.progress import track
from PIL import Image
from sympy import symbols, Matrix

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



# 改进后
class CentralProjection002(ThreeDScene):
    def construct(self):
        point1 = [1, 1, 2]
        dot = Dot3D(point=point1, color=YELLOW)

        equation1 = MathTex(R"""1x+2y+2z-2=0""")
        self.add_fixed_in_frame_mobjects(equation1.to_corner(UL))
        def func_surface(u, v):
            # 1x+2y+2z-2=0
            x=u
            y=v
            z=(2-x-2*y)/2
            return np.array([x,y,z])


        surface = OpenGLSurface(
            uv_func=func_surface,
            u_range=[-2, 2],
            v_range=[-2, 2],
        )
        self.add(surface)

        self.set_camera_orientation(theta=35 * DEGREES, phi=65 * DEGREES)

        axes = ThreeDAxes(include_numbers=False, x_range=[-7, 7, 1], y_range=[-5, 5, 1], z_range=[-4, 4, 1],
                          x_length=14, y_length=10, z_length=6)
        axes.add(axes.get_axis_labels())
        self.add(axes,dot)

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


# 画辅助线
class CentralProjection003(ThreeDScene):
    def construct(self):
        point1 = [1, 1, 2]
        dot = Dot3D(point=point1, color=YELLOW)

        equation1 = MathTex(R"""1x+2y+2z-2=0""")
        self.add_fixed_in_frame_mobjects(equation1.to_corner(UL))
        def func_surface(u, v):
            # 1x+2y+2z-2=0
            x=u
            y=v
            z=(2-x-2*y)/2
            return np.array([x,y,z])


        surface = OpenGLSurface(
            uv_func=func_surface,
            u_range=[-2, 2],
            v_range=[-2, 2],
        )
        self.add(surface)

        self.set_camera_orientation(theta=35 * DEGREES, phi=65 * DEGREES)

        axes = ThreeDAxes(include_numbers=False, x_range=[-7, 7, 1], y_range=[-5, 5, 1], z_range=[-4, 4, 1],
                          x_length=14, y_length=10, z_length=6)
        axes.add(axes.get_axis_labels())
        self.add(axes,dot)


        image_array = np.array(Image.open("src/test.jpg").convert("RGBA"))
        image = NumpyImage(image_array=image_array, distance=0.01, stroke_width=2)
        self.play(Create(image))

        line1= DashedLine(start=[-1,-1,0],end=point1)
        line2= DashedLine(start=[1,1,0],end=point1)
        line3= DashedLine(start=[-1,1,0],end=point1)
        line4= DashedLine(start=[1,-1,0],end=point1)
        self.add(line1,line4,line3,line2)

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


# 消掉z
class CentralProjection004(ThreeDScene):
    def construct(self):
        point1 = [1, 1, 2]
        dot = Dot3D(point=point1, color=YELLOW)
        equation1 = MathTex(R"""1x+2y+2z-4=0""")
        self.add_fixed_in_frame_mobjects(equation1.to_corner(UL))
        def func_surface(u, v):
            # 1x+2y+2z-2=0
            x = u
            y = v
            z = (4 - x - 2 * y) / 2
            return np.array([x, y, z])

        surface = OpenGLSurface(
            uv_func=func_surface,
            u_range=[-2, 2],
            v_range=[-2, 2],
        )
        self.add(surface)

        self.set_camera_orientation(theta=35 * DEGREES, phi=65 * DEGREES)

        axes = ThreeDAxes(include_numbers=False, x_range=[-7, 7, 1], y_range=[-5, 5, 1], z_range=[-4, 4, 1],
                          x_length=14, y_length=10, z_length=6)
        axes.add(axes.get_axis_labels())
        self.add(axes, dot)

        image_array = np.array(Image.open("src/test.jpg").convert("RGBA"))
        image = NumpyImage(image_array=image_array, distance=0.01, stroke_width=2)
        # self.play(Create(image))
        self.add(image)

        line1 = DashedLine(start=[-1, -1, 0], end=point1)
        line2 = DashedLine(start=[1, 1, 0], end=point1)
        line3 = DashedLine(start=[-1, 1, 0], end=point1)
        line4 = DashedLine(start=[1, -1, 0], end=point1)
        self.add(line1, line4, line3, line2)

        # 1x+2y+2z-4=0;
        a = 1;
        b = 2;
        c = 2;
        d = -4
        xo = 1;
        yo = 1;
        zo = 2
        # x=1;y=1;z=1
        # t = -(a * xo + b * yo + c * zo + d) / a * x - a * xo + b * y - b * yo + c * z - c * zo
        # x1 = xo + t * (x - xo);
        # y1 = yo + t * (y - yo);
        # z1 = zo + t * (z - zo)

        new_points = []
        for point in image.points:
            x = point[0]
            y = point[1]
            z = point[2]

            t = -(a * xo + b * yo + c * zo + d) / (a * x - a * xo + b * y - b * yo + c * z - c * zo)

            x1 = xo + t * (x - xo);
            y1 = yo + t * (y - yo);
            z1 = zo + t * (z - zo)
            new_point = [x1, y1, z1]
            new_points.append(new_point)

        self.begin_ambient_camera_rotation(rate=1)
        image.points= np.array(new_points)
        self.wait(4)


        image2 = NumpyImage(image_array=image_array, distance=0.01, stroke_width=2)
        points2=[]
        for point in new_points.copy():
            new_point=(point[0]/point[2],point[1]/point[2],1)
            points2.append(new_point)

        image2.rgbas=image.rgbas.copy()
        image2.points=np.array(points2)
        axes2= Axes().scale(0.3).to_corner(UR)
        self.add_fixed_in_frame_mobjects(axes2)
        self.add_fixed_in_frame_mobjects(image2.to_corner(UR))
        self.wait()


        image3 = NumpyImage(image_array=image_array, distance=0.01, stroke_width=2)
        points3 = []
        for point in new_points.copy():
            new_point = (point[0] / point[1], 1, point[2] / point[1])
            points3.append(new_point)

        image3.rgbas = image.rgbas.copy()
        image3.points = np.array(points3)
        axes3 = Axes().scale(0.3).to_corner(RIGHT)
        self.add_fixed_in_frame_mobjects(axes3)
        self.add_fixed_in_frame_mobjects(image3.to_corner(RIGHT))
        self.wait()



        image4 = NumpyImage(image_array=image_array, distance=0.01, stroke_width=2)
        points4 = []
        for point in new_points.copy():
            new_point = (1, point[1] / point[0], point[2] / point[0])
            points4.append(new_point)

        image4.rgbas = image.rgbas.copy()
        image4.points = np.array(points4)
        axes4 = Axes().scale(0.3).to_corner(DR)
        self.add_fixed_in_frame_mobjects(axes4)
        self.add_fixed_in_frame_mobjects(image4.to_corner(DR))
        self.wait()

class CentralProjectionShow(ThreeDScene):
    def construct(self):
        self.begin_ambient_camera_rotation(rate=1)
        point1 = [1, 1, 2]
        dot = Dot3D(point=point1, color=YELLOW)
        equation1 = MathTex(R"""\text{投影面:}1x+2y+2z-4=0""",tex_template=TexTemplateLibrary.ctex)
        self.add_fixed_in_frame_mobjects(equation1.to_corner(UL))
        equation2 = MathTex(R"""\text{投影中心:}P(1,1,2) """, tex_template=TexTemplateLibrary.ctex)
        self.add_fixed_in_frame_mobjects(equation2.next_to(equation1,direction=DOWN))
        def func_surface(u, v):
            # 1x+2y+2z-2=0
            x = u
            y = v
            z = (4 - x - 2 * y) / 2
            return np.array([x, y, z])

        Surface
        surface = OpenGLSurface(
            uv_func=func_surface,
            u_range=[-2, 2],
            v_range=[-2, 2],
            opacity=0.5,
            color="#458d92"


        )
        # self.add(image)



        self.set_camera_orientation(theta=35 * DEGREES, phi=65 * DEGREES)

        axes = ThreeDAxes(include_numbers=False, x_range=[-7, 7, 1], y_range=[-5, 5, 1], z_range=[-4, 4, 1],
                          x_length=14, y_length=10, z_length=6)
        axes.add(axes.get_axis_labels())
        # self.add(axes, dot)
        self.play(Create(axes),Create(dot))

        self.play(Create(surface))
        self.wait(3)


        image_array = np.array(Image.open("src/test.jpg").convert("RGBA"))
        image = NumpyImage(image_array=image_array, distance=0.01, stroke_width=2)
        self.play(Create(image))
        self.wait(3)


        line1 = DashedLine(start=[-1, -1, 0], end=point1)
        line2 = DashedLine(start=[1, 1, 0], end=point1)
        line3 = DashedLine(start=[-1, 1, 0], end=point1)
        line4 = DashedLine(start=[1, -1, 0], end=point1)
        self.play(Create(line1),Create(line2),Create(line3),Create(line4))
        self.wait(3)
        # 1x+2y+2z-4=0;
        a = 1;
        b = 2;
        c = 2;
        d = -4
        xo = 1;
        yo = 1;
        zo = 2
        # x=1;y=1;z=1
        # t = -(a * xo + b * yo + c * zo + d) / a * x - a * xo + b * y - b * yo + c * z - c * zo
        # x1 = xo + t * (x - xo);
        # y1 = yo + t * (y - yo);
        # z1 = zo + t * (z - zo)

        new_points = []
        for point in image.points:
            x = point[0]
            y = point[1]
            z = point[2]

            t = -(a * xo + b * yo + c * zo + d) / (a * x - a * xo + b * y - b * yo + c * z - c * zo)

            x1 = xo + t * (x - xo);
            y1 = yo + t * (y - yo);
            z1 = zo + t * (z - zo)
            new_point = [x1, y1, z1]
            new_points.append(new_point)



        self.play(ApplyMethod(image.set_points, np.array(new_points)))
        # image.points= np.array(new_points)
        self.wait(3)


        image2 = NumpyImage(image_array=image_array, distance=0.01, stroke_width=2)
        points2=[]
        for point in new_points.copy():
            new_point=(point[0]/point[2],point[1]/point[2],1)
            points2.append(new_point)

        image2.rgbas=image.rgbas.copy()
        image2.points=np.array(points2)

        axes2 = Axes(is_fixed_in_frame=True).scale(0.3).to_corner(UR)
        self.add_fixed_in_frame_mobjects(axes2)
        self.add_fixed_in_frame_mobjects(image2.to_corner(UR))
        self.play(Create(axes2),Create(image2))
        self.wait(3)




with tempconfig({"preview": True, "disable_caching": True, "renderer": "opengl"}):
    CentralProjectionShow().render()
    exit(1)
