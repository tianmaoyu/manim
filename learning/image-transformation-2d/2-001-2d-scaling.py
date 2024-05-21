
from manim import *
from manim.mobject.opengl.opengl_cylinder import OpenGLCylinder
from manim.mobject.opengl.opengl_image_mobject import OpenGLImageMobject
from manim.mobject.opengl.opengl_point_image_mobject import ImagePixelMobject, NumpyImage
from manim.mobject.opengl.opengl_shpere import OpenGLSphere
from manim.mobject.opengl.opengl_something import OpenGLCone, OpenGLLine3D
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface, OpenGLSurface
import numpy as np
import sympy as sp
from manim.typing import Image
from PIL import Image


#放大两倍
class Scaling001(ThreeDScene):
    def construct(self):
        image_array = np.array(Image.open("src/test.jpg").convert("RGBA"))
        image_array_part=image_array[50:150,50:150]
        image = NumpyImage(image_array=image_array_part, distance=0.05, stroke_width=2)

        self.play(Create(image))
        text= MathTex(r" \times 2").scale(3).next_to(image,direction=RIGHT)
        self.play(Create(text))
        self.wait()

        new_points=image.points * 2
        self.play(FadeOut(text),ApplyMethod(image.set_points, new_points))





#缩小
class Scaling002(ThreeDScene):
    def construct(self):
        image_array = np.array(Image.open("src/test.jpg").convert("RGBA"))
        image_array_part = image_array[50:150, 50:150]
        image = NumpyImage(image_array=image_array_part, distance=0.05, stroke_width=2)

        self.play(Create(image))
        text = MathTex(r" \times 0.5").scale(3).next_to(image, direction=RIGHT)
        self.play(Create(text))
        self.wait()

        new_points = image.points * 0.5
        self.play(FadeOut(text), ApplyMethod(image.set_points, new_points))


class Scaling003(ThreeDScene):
    def construct(self):
        image_array = np.array(Image.open("src/test.jpg").convert("RGBA"))
        image_array_part = image_array[50:150, 50:150]
        image = NumpyImage(image_array=image_array_part, distance=0.05, stroke_width=2)

        self.play(Create(image))
        text = MathTex(r" \times -1").scale(3).next_to(image, direction=RIGHT)
        self.play(Create(text))

        new_points = image.points * -1
        self.play(FadeOut(text), ApplyMethod(image.set_points, new_points))
        self.wait()





with tempconfig({"preview": True, "disable_caching": True, "renderer": "opengl"}):
    Scaling003().render()
    exit(1)