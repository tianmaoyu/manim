import time

from manim import *
from manim.mobject.opengl.opengl_point_image_mobject import ImagePixelMobject
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface, OpenGLSurface
import numpy as np


class Panorama009(ThreeDScene):
    def construct(self):

        image = ImagePixelMobject("360-2048-1024.jpg", image_width=16, stroke_width=6.0)
        image.to_center()
        self.add(image)
        axex = ThreeDAxes(x_length=[-4, 4, 1], x_range=[-4, 4, 1], z_range=[-4, 4, 1])
        self.add(axex)

        self.move_camera(phi=65 * DEGREES, theta=15 * DEGREES, run_time=2)

        self.set_camera_orientation(phi=75 * DEGREES, theta=15 * DEGREES)

        # self.begin_ambient_camera_rotation(rate=0.5)
        points = image.points
        # [r,phi,theta]
        spherical_points = np.empty_like(points)
        r = 8
        spherical_points[:, 2] = PI * (points[:, 1] / r) - PI / 2
        spherical_points[:, 1] = PI * points[:, 0] / r
        spherical_points[:, 0] = 3

        # 性能改进
        # cartesian_points = np.apply_along_axis(spherical_to_cartesian, axis=1, arr=spherical_points)
        r = spherical_points[:, 0]
        theta = spherical_points[:, 1]
        phi = spherical_points[:, 2]

        x = r * np.cos(theta) * np.sin(phi)
        y = r * np.sin(theta) * np.sin(phi)
        z = r * np.cos(phi)

        cartesian_points = np.stack((x, y, z), axis=-1)

        # image.points = cartesian_points
        self.play(ApplyMethod(image.set_points, cartesian_points), run_time=2, rate_func=smooth)

        # self.move_camera(phi=75 * DEGREES, theta=150 * DEGREES, run_time=1)

        self.begin_ambient_camera_rotation(rate=0.5)
        # self.wait(3)


        self.play(image.animate.scale(7),axex.animate.scale(6),run_time=2)
        # return


        self.move_camera(phi=45 * DEGREES, theta=15 * DEGREES,run_time=2)

        self.move_camera(phi=90 * DEGREES, theta=15 * DEGREES, run_time=2)

        self.move_camera(phi=135 * DEGREES, theta=15 * DEGREES, run_time=2)

        self.move_camera(phi=180 * DEGREES, theta=15 * DEGREES, run_time=2)
        self.play(image.animate.scale(1/7), run_time=2)
        self.wait()


# "renderer": "opengl" "quality": "fourk_quality","force_window":True
with tempconfig({"preview": True, "disable_caching": True, "renderer": "opengl"}):
    Panorama009().render()
    exit(1)
