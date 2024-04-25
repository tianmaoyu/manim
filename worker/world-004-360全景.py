from manim import *
from manim.mobject.opengl.opengl_point_image_mobject import ImagePixelMobject
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface, OpenGLSurface
import numpy as np


class Panorama(ThreeDScene):
    def construct(self):
        image = ImagePixelMobject("360.jpg",image_width=16)
        image.to_center()
        self.add(image)
        self.add(ThreeDAxes(x_length=[-4, 4, 1], x_range=[-4, 4, 1], z_range=[-4, 4, 1]))
        # return
        self.wait(1)
        self.set_camera_orientation(phi=75 * DEGREES, theta=15 * DEGREES)
        # self.move_camera(phi=75 * DEGREES, theta=150 * DEGREES, run_time=1)
        # self.begin_ambient_camera_rotation(rate=0.5)
        points = image.points
        # [r,phi,theta]
        spherical_points = points.copy()
        r = 8 / PI / 2
        # ϕ = πy - π/2
        spherical_points[:, 2] = PI * (spherical_points[:, 1] / 8) - PI / 2
        # θ = 2πx
        # spherical_points[:, 1] = spherical_points[:, 0]/ 8 * 2 * PI
        # θ = πx : -π 到  π
        spherical_points[:, 1] = PI * spherical_points[:, 0] / 8

        spherical_points[:, 0] = r * 3

        cartesian_points = np.apply_along_axis(spherical_to_cartesian, axis=1, arr=spherical_points)

        # image.points = cartesian_points
        self.play(ApplyMethod(image.set_points, cartesian_points), run_time=2, rate_func=smooth)

        # self.move_camera(phi=75 * DEGREES, theta=150 * DEGREES, run_time=1)

        self.move_camera(phi=75 * DEGREES, theta=150 * DEGREES,run_time=2)
        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(4)


# "renderer": "opengl" "quality": "fourk_quality",
with tempconfig({"preview": True, "disable_caching": True, "renderer": "opengl"}):
    Panorama().render()
    exit(1)
