from manim import *
from manim.mobject.opengl.opengl_point_image_mobject import ImagePixelMobject
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface, OpenGLSurface
import numpy as np


class Panorama6(ThreeDScene):
    def construct(self):
        image = ImagePixelMobject("360_big.jpg")
        image.to_center()
        self.add(image)
        self.add(ThreeDAxes(x_length=[-4, 4, 1], x_range=[-4, 4, 1], z_range=[-4, 4, 1]))

        self.set_camera_orientation(phi=75 * DEGREES, theta=15 * DEGREES)

        # self.begin_ambient_camera_rotation(rate=0.5)
        points = image.points
        # [r,phi,theta]
        spherical_points = points.copy()
        r = 8 / PI / 2
        # ϕ = πy - π/2
        spherical_points[:, 2] = PI * (spherical_points[:, 1] / 4) - PI / 2
        # θ = 2πx
        # spherical_points[:, 1] = spherical_points[:, 0]/ 8 * 2 * PI
        #  ϕ= πx : -π 到  π
        spherical_points[:, 1] = PI * spherical_points[:, 0] / 4

        spherical_points[:, 0] = 20

        cartesian_points = np.apply_along_axis(spherical_to_cartesian, axis=1, arr=spherical_points)

        image.points = cartesian_points
        # self.play(ApplyMethod(image.set_points, cartesian_points), run_time=2, rate_func=smooth)
        self.set_camera_orientation(phi=0 * DEGREES, theta=15 * DEGREES)
        text1 = MarkupText("phi=0",font="sans-serif")
        text = MarkupText("phi=45", font="sans-serif")
        text = MarkupText("phi=90", font="sans-serif")
        text = MarkupText("phi=135", font="sans-serif")
        text = MarkupText("phi=180", font="sans-serif")
        # self.add_fixed_orientation_mobjects(text)
        self.set_camera_orientation(phi=90 * DEGREES, theta=5 * DEGREES)
        animate= self.camera.animate.move_to(UP*4)
        self.play(animate,run_time=2)
        return
        # self.move_camera(phi=75 * DEGREES, theta=150 * DEGREES, run_time=1)
        self.set_camera_orientation(phi=0 * DEGREES, theta=15 * DEGREES)

        self.move_camera(phi=45 * DEGREES, theta=15 * DEGREES,run_time=2)

        self.move_camera(phi=90 * DEGREES, theta=15 * DEGREES, run_time=2)

        self.move_camera(phi=135 * DEGREES, theta=15 * DEGREES, run_time=2)

        self.move_camera(phi=180 * DEGREES, theta=15 * DEGREES, run_time=2)



        # self.wait(4)


# "renderer": "opengl" "quality": "fourk_quality",
with tempconfig({"preview": True, "disable_caching": True, "renderer": "opengl"}):
    Panorama6().render()
    exit(1)
