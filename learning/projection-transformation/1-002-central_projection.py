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


# 矩阵多平面， 投影到面 a, 再投影到面b
class CentralProjection004(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(theta=35 * DEGREES, phi=65 * DEGREES)
        self.begin_ambient_camera_rotation(rate=1)
        axes = ThreeDAxes(include_numbers=False, x_range=[-7, 7, 1], y_range=[-5, 5, 1], z_range=[-4, 4, 1],
                          x_length=14, y_length=10, z_length=6)
        axes.add(axes.get_axis_labels())
        self.add(axes)

        image_array = np.array(Image.open("src/test.jpg").convert("RGBA"))
        image = NumpyImage(image_array=image_array, distance=0.01, stroke_width=2)
        self.play(Create(image))
        # 定义符号变量
        x, y, z, x_o, y_o, z_o, a, b, c, d = symbols('x y z x_o y_o z_o a b c d')

        # 定义矩阵
        symbols_matrix = Matrix([
            [-(b * y_o + c * z_o + d), b * x_o, c * x_o, d * x_o],
            [a * y_o, -(a * x_o + c * z_o + d), c * y_o, d * y_o],
            [a * z_o, b * z_o, -(a * x_o + b * y_o + d), d * z_o],
            [a, b, c, -(a * x_o + b * y_o + c * z_o)]
        ])

        symbols_matrix = symbols_matrix

        # 点O： (1, 1, 2)
        # 平面方程： 1x+2y+2z-2=0
        # 点P (1,1,0)
        key_vaules1 = {a: 1, b: 2, c: 2, d: -2, x_o: 1, y_o: 1, z_o: 2,}
        matrix1 = symbols_matrix.subs(key_vaules1)


        image_points:np.ndarray = image.points.copy()

        image_points=np.hstack((image_points, np.ones((image_points.shape[0], 1))))
        print(matrix1)
        matrix1= np.array(matrix1.tolist(), dtype=float)# 保留两精度
        print(matrix1)
        points= matrix1 @ image_points.T
        points=points.T
        new_points=[]
        for point in points:
            new_point=(point[0]/point[3],point[1]/point[3],point[2]/point[3])
            new_points.append(new_point)


        # image.points=np.array(new_points)


        point1 = [1, 1, 2]
        dot1 = Dot3D(point=point1, color=BLUE)
        def func_surface1(u, v):
            # 1x+2y+2z-2=0
            x = u
            y = v
            z = (2 - x - 2 * y) / 2
            return np.array([x, y, z])

        surface1 = OpenGLSurface(
            uv_func=func_surface1,
            u_range=[-2, 2],
            v_range=[-2, 2],
            color=BLUE,
            opacity=0.5
        )
        self.add(dot1,surface1)
        self.play(ApplyMethod(image.set_points, np.array(new_points)), run_time=2)
        self.wait(2)

        # 点O： (0, 0, 0)
        # 平面方程： 0x+oy+1z+1=0
        # 点P (2,2,2)
        # 点 p'(1,1,1)
        key_vaules2 = {a: 0, b: 0, c: 1, d: 1, x_o: 0, y_o: 0, z_o: -4}
        matrix2 = symbols_matrix.subs(key_vaules2)
        matrix2=np.array(matrix2.tolist(), dtype=float)
        image_points: np.ndarray = image.points.copy()
        image_points = np.hstack((image_points, np.ones((image_points.shape[0], 1))))
        points = matrix2 @ image_points.T
        points=points.T
        new_points = []
        for point in points:
            new_point = (point[0] / point[3], point[1] / point[3], point[2] / point[3])
            new_points.append(new_point)

        point2 = [0, 0, -4]
        dot2 = Dot3D(point=point2, color=RED)

        def func_surface2(u, v):
            x = u
            y = v
            z = -1
            return np.array([x, y, z])

        surface2 = OpenGLSurface(
            uv_func=func_surface2,
            u_range=[-3, 3],
            v_range=[-3, 3],
            color=RED,
            opacity=0.5
        )

        self.add(surface2, dot2)
        self.play(ApplyMethod(image.set_points, np.array(new_points)), run_time=2)
        self.wait(2)





with tempconfig({"preview": True, "disable_caching": False, "renderer": "opengl"}):
    CentralProjection004().render()
    exit(1)
