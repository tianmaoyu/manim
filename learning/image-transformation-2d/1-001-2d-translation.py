import random
import time

from manim import *
from manim.mobject.opengl.opengl_cylinder import OpenGLCylinder
from manim.mobject.opengl.opengl_image_mobject import OpenGLImageMobject
from manim.mobject.opengl.opengl_point_image_mobject import ImagePixelMobject
from manim.mobject.opengl.opengl_shpere import OpenGLSphere
from manim.mobject.opengl.opengl_something import OpenGLCone, OpenGLLine3D
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface, OpenGLSurface
import numpy as np
import sympy as sp
from manim.typing import Image
from PIL import Image


class NumpyImage(OpenGLPMobject):
    def __init__(self, image_array: np.ndarray, stroke_width=2.0, distance=0.025, **kwargs):
        super().__init__(**kwargs, stroke_width=stroke_width, depth_test=True)

        # 构建三维坐标
        height, width, channel = image_array.shape
        assert channel == 4, "必须是r,g,b,a"
        points = np.zeros((height * width, 3))
        y_indices, x_indices = np.mgrid[0:height, 0:width]
        points[:, 0] = x_indices.flatten()  # x坐标
        points[:, 1] = y_indices.flatten()  # y坐标
        rgbas = image_array.reshape(-1, 4)

        # y轴反转和缩小- 一个坐标间隔为1
        points = points * distance * np.array([1, -1, 1])
        # 居中
        points += np.array([-width * distance / 2, height * distance / 2, 0])
        self.points = points
        self.rgbas = rgbas / 255

    def set_points(self,points:np.ndarray):
        self.points = points
        return self


class AddImage001(ThreeDScene):
    def construct(self):
        image = np.zeros((50, 50, 4), dtype=np.uint8)
        image[:, :, 0] = 255
        image[:, :, 3] = 255
        image_obj = NumpyImage(image_array=image, distance=0.05, stroke_width=2)
        self.add(image_obj)
        axes = Axes().add_coordinates()
        axes.add(axes.get_axis_labels())
        self.add(axes)
        plane = NumberPlane()
        self.add(plane)
        lines = axes.get_lines_to_point(axes.c2p(2, 2))
        self.add(lines)
        point=axes.c2p(2, 2)
        vector = Vector(direction=point)
        vector.add(vector.coordinate_label())
        self.add(vector)



#生成一些像素点
class AddImage002(ThreeDScene):

    def construct(self):
        image = np.zeros((50, 50, 4), dtype=np.uint8)
        image[:, :, 0] = 255
        image[:, :, 3] = 255
        image_obj = NumpyImage(image_array=image, distance=0.05, stroke_width=2)
        # self.add(image_obj)
        self.play(Create(image_obj))
        plane = NumberPlane()
        # self.add(plane)
        self.play(Create(plane))
        lines = plane.get_lines_to_point(plane.c2p(2, 2))
        # self.add(lines)
        self.play(Create(lines))

        vector = Vector(direction=[2,2])
        vector.add(vector.coordinate_label())
        self.play(Create(vector))
        # self.add(vector)
        self.next_section("移动图像")
        mover_vector = np.array([2, 2, 0])

        new_points= image_obj.points+mover_vector
        self.play(ApplyMethod(image_obj.set_points,new_points))

        # obj = Matrix(mover_vector)
        # self.add(obj)



class AddImage003(ThreeDScene):
    def construct(self):

        x,y= np.indices((3,3))
        vectors=np.dstack([x,y]).reshape(-1,2)
        vectors = Matrix(vectors.T,h_buff=0.4)
        # 创建网格
        x,y = np.meshgrid(np.arange(3), np.arange(3), indexing='ij')
        coordinates = np.stack((x, y), axis=-1)
        obj = np.indices((3, 3))
        numpy_matrix = np.array([[1, 2], [3, 4]])
        sympy_matrix = sp.Matrix(coordinates)
        # 生成LaTeX字符串表示,需要 加 $$
        latex_str = sp.latex(sympy_matrix)
        tex= Tex(f"${latex_str}$")
        self.play(Create(tex))
        # self.add(vectors)
        mover_vector = np.array([2, 2, 0])
        vector=Vector(mover_vector)
        self.add(vector,vector.coordinate_label(n_dim=3))
        self.wait(1)


#加载一张图片
class AddImage004(ThreeDScene):
    def construct(self):
        image_array = np.array(Image.open("src/test.jpg").convert("RGBA"))
        image_array_part=image_array[50:150,50:150]
        image = NumpyImage(image_array=image_array_part, distance=0.05, stroke_width=2)
        self.play(Create(image))
        start_point=image.points[0]
        end_point =image.points[-1]

        b1 = Brace(image)
        b1.add(b1.get_text("200 pixel"))
        b2 = Brace(image,direction=LEFT)
        b2.add(b2.get_text("200 pixel"))
        self.add(b1,b2)
        self.wait()
        self.play(FadeOut(b1), FadeOut(b2))

        plane = NumberPlane()
        self.play(Create(plane))

        mover_vector = np.array([2, 2, 0])
        vector = Vector(mover_vector,n_dim=3)
        vector.add(vector.coordinate_label())
        self.play(Create(vector))

        new_points = image.points + mover_vector
        self.play(ApplyMethod(image.set_points, new_points))

class Translation001(ThreeDScene):
    config.output_file="Translation001-平移.mp4"
    def construct(self):

        latex_str1 = r"""
\begin{bmatrix}x'\\y'\\\end{bmatrix}
=
\begin{bmatrix}x\\y\\\end{bmatrix}
+
\begin{bmatrix}x_b\\ y_b\end{bmatrix}
=
\begin{bmatrix}x+x_b\\y+y_b\end{bmatrix}
         """
        math_tex1 = MathTex(latex_str1)
        self.play(Create(math_tex1))
        self.play(math_tex1.animate.to_corner(UL))


        image = np.zeros((50, 50, 4), dtype=np.uint8)
        image[:, :, 0] = 255
        image[:, :, 3] = 255
        image_obj = NumpyImage(image_array=image, distance=0.05, stroke_width=2)
        # self.add(image_obj)
        self.play(Create(image_obj))
        # plane = NumberPlane()
        # self.play(Create(plane))
        axes = Axes(x_range=[-7, 7, 1],include_numbers=False, y_range=[-5, 5, 1],x_length=14, y_length=10)
        self.play(Create(axes))
        lines = axes.get_lines_to_point([2,2,0])
        self.play(Create(lines))

        vector = Vector(direction=[2,2,0])
        vector.add(vector.coordinate_label())
        self.play(Create(vector))
        self.next_section("移动图像")
        mover_vector = np.array([2, 2, 0])

        new_points= image_obj.points+mover_vector
        self.play(ApplyMethod(image_obj.set_points,new_points))

with tempconfig({"preview": True, "renderer": "opengl"}):
    Translation001().render()
    exit(1)
