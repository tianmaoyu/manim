from manim import *


class Demo(ThreeDScene):
    def construct(self):
        NumberLine
        self.set_camera_orientation(phi=75 * DEGREES, theta=15 * DEGREES)
        axes = ThreeDAxes()
        # self.play(Write(axes))
        # self.wait()
        # self.play(FadeOut(axes))
        # self.wait()

        x_axis = Vector(axes.x_axis.get_unit_vector() * 4)
        y_axis = Vector(axes.y_axis.get_unit_vector() * 4)
        z_axis = Vector(axes.z_axis.get_unit_vector() * 4)
        vgroup = VGroup(x_axis, y_axis, z_axis)
        self.play(Write(vgroup))
        rotate= Rotate(vgroup, angle=45*DEGREES, axis=axes.x_axis.get_unit_vector(),about_point=ORIGIN)
        self.play(rotate,run_time=2)
        # self.play(Write(x_axis))
        # self.play(Write(y_axis))
        # self.play(Write(z_axis))


# "renderer": "opengl"
with tempconfig({"preview": True, "disable_caching": True, "renderer": "opengl"}):
    Demo().render()
    exit(1)
