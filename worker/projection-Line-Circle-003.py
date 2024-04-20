import math

import moderngl
from scipy.interpolate import interp2d

from manim import *
from manim.mobject.opengl.opengl_image_mobject import OpenGLImageMobject
from manim.mobject.opengl.opengl_mobject import OpenGLMobject, OpenGLPoint
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface, OpenGLSurface
import numpy as np
from PIL import Image

circle_r = 1
circle_init_point = np.array([0, 0, 0])
x_list=np.arange(0,4,0.1)

class LineToCircle(Scene):
    def construct(self):

        self.show001()

    def show001(self):

        self.camera.move_to(RIGHT * 2)

        circle = Circle(radius=circle_r)
        line = NumberLine(include_ticks=False)
        dot_list = [Dot(point=[x+circle_r, 0, 0],radius=0.04) for x in x_list]
        path_list = [TracedPath(dot.get_center) for dot in dot_list]

        self.add(circle, line, *dot_list, *path_list)

        self.time = 0

        def upadate_func(dt):
            self.time += dt

            circle_point = circle_init_point + np.array([self.time, 0, 0])
            circle.move_to(circle_point)

            for index, dot in enumerate(dot_list):
                update_dot(dot, x_list[index], self.time)

        def update_dot(dot: Dot, init_x, rad):
            if rad >= init_x:
                real_rad = rad - init_x
                x = np.cos(-real_rad) + real_rad
                y = np.sin(-real_rad)
                new_point = np.array([x + init_x, y, 0])
                dot.move_to(new_point)

        self.add_updater(func=upadate_func)
        self.wait(2 * PI)



# "renderer": "opengl"  "background_color":"WHITE",
with tempconfig({"preview": True, "disable_caching": True, "renderer": "opengl"}):
    LineToCircle().render()
    exit(1)
