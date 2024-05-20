from manim import *
from manim.mobject.opengl.opengl_point_image_mobject import ImagePixelMobject
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface, OpenGLSurface
import numpy as np


class WorldToShpere(ThreeDScene):
    """
    world -> cylinder
    """

    def construct(self):
        # self.camera.light_source.animate.move_to()
        image = ImagePixelMobject("world-daytime.jpg")
        image.to_center()
        self.add(image)
        self.add(ThreeDAxes())
        self.wait(1)
        self.set_camera_orientation(phi=90 * DEGREES, theta=15 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.5)
        points = image.points
        # [r,phi,theta]
        spherical_points = points.copy()
        r = 8 / PI / 2
        # ϕ = πy - π/2
        spherical_points[:, 2] = PI * (spherical_points[:, 1] / 4) - PI / 2
        # θ = 2πx
        spherical_points[:, 1] = spherical_points[:, 0] * 2 * PI / 8
        spherical_points[:, 0] = r*2
        cartesian_points = np.apply_along_axis(spherical_to_cartesian, axis=1, arr=spherical_points)
        self.set_camera_orientation(phi=90 * DEGREES, theta=15 * DEGREES)

        image.points = cartesian_points
        # self.play(ApplyMethod(image.set_points, cartesian_points),   run_time=1 ,  rate_func=smooth)
        self.move_camera(phi=75 * DEGREES, theta=150 * DEGREES, run_time=2)
        self.wait(4)



# "renderer": "opengl" "quality": "fourk_quality",
with tempconfig({"preview": True, "disable_caching": True,  "renderer": "opengl"}):
    WorldToShpere().render()
    exit(1)
