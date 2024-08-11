import random
import time

from manim import *
from manim.mobject.opengl.opengl_cylinder import OpenGLCylinder
from manim.mobject.opengl.opengl_image_mobject import OpenGLImageMobject
from manim.mobject.opengl.opengl_point_image_mobject import ImagePixelMobject, ImageBox, NumpyImage
from manim.mobject.opengl.opengl_shpere import OpenGLSphere
from manim.mobject.opengl.opengl_something import OpenGLCone, OpenGLLine3D, OpenGLCube
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface, OpenGLSurface
import numpy as np
import sympy as sp

from manim.mobject.opengl.opengl_vectorized_mobject import OpenGLVGroup
from manim.typing import Image
from PIL import Image
import json
import re


class TexturedCube(OpenGLVGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.texture_files = {
            'pos_x': 'src/X.png',
            'neg_x': 'src/-X.png',
            'pos_y': 'src/Y.png',
            'neg_y': 'src/-Y.png',
            'pos_z': 'src/Z.png',
            'neg_z': 'src/-Y.png'
        }
        self.create_cube()

    def create_cube(self):
        cube = OpenGLCube()
        self.add(cube)
        Square()
        def get_rotation_matrix(self, direction_vectors):
            # Helper function to get the rotation matrix based on the direction vectors
            axis = np.cross(direction_vectors[0], direction_vectors[2])
            angle = np.arccos(np.dot(direction_vectors[0], direction_vectors[2]))
            return rotation_matrix(angle, axis)

        for face, texture_key in zip(cube, self.texture_files.values()):
            face.set_fill(opacity=0)  # Make the face transparent
            face.set_stroke(width=0)  # Remove the border
            face.apply_texture(texture_key)
class ThreeDDemo001(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        axes = ThreeDAxes(include_numbers=False,tips=False);
        self.add(axes)

        cube= OpenGLCube()

        img_x = ImagePixelMobject("src/X.PNG").scale(0.5),
        img_inv_x = OpenGLImageMobject("src/-X.PNG").scale(0.5),
        img_y = OpenGLImageMobject("src/Y.PNG").scale(0.5),
        img_inv_y = OpenGLImageMobject("src/-Y.PNG").scale(0.5),
        img_z = OpenGLImageMobject("src/Z.PNG").scale(0.5),
        img_inv_z = OpenGLImageMobject("src/-Z.PNG").scale(0.5)

        # offset=1
        # left =img_x.apply_matrix(rotation_matrix(90 * DEGREES, axis=UP) )
        # left = left.T + np.array([-offset, 0, 0])


        # right = rotation_matrix(90 * DEGREES, axis=UP)
        # right = right.T + np.array([offset, 0, 0])
        #
        #
        # up = rotation_matrix(90 * DEGREES, axis=RIGHT)
        # up = up.T + np.array([0, offset, 0])
        #
        # down = rotation_matrix(90 * DEGREES, axis=RIGHT)
        # down = down.T + np.array([0, -offset, 0])
        #
        # z_out =  np.array([0, 0, offset])

        obj = ImageMobject("src/X.PNG")

        # 将图像添加到场景中
        self.add(obj)


class MyScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        textured_cube = TexturedCube()
        self.add(textured_cube)
        self.play(Rotate(textured_cube, angle=PI / 4, axis=UP))
        self.wait()



class SquarePyramidScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        vertex_coords = [
            [1, 1, 0],
            [1, -1, 0],
            [-1, -1, 0],
            [-1, 1, 0],
            [0, 0, 2]
        ]
        faces_list = [
            [0, 1, 4],
            [1, 2, 4],
            [2, 3, 4],
            [3, 0, 4],
            [0, 1, 2, 3]
        ]
        pyramid = Polyhedron(vertex_coords, faces_list)
        self.add(pyramid)

        obj = Tetrahedron()
        self.add(obj.to_corner(UP))
        obj = ImageMobject("src/X.PNG")
        # 透明
        obj.pixel_array[:,:,3]=0
        self.add(obj)

#  三维旋转
# "renderer": "opengl"
with tempconfig({"preview": True, "disable_caching": False, }):
    SquarePyramidScene().render()
    exit(1)

