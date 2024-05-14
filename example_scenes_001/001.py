from manim import *
import numpy as np

from manim.mobject.opengl.opengl_shpere import OpenGLSphere
from manim.mobject.opengl.opengl_something import OpenGLDot3D


class RotationPath(ThreeDScene):
    def construct(self):
        # # 创建3D坐标轴
        dot = OpenGLDot3D(radius=0.05, color=WHITE)
        path = TracedPath(dot.get_center, stroke_color=dot.get_color(), stroke_width=2)
        sphere = OpenGLSphere(radius=1.5, color=BLUE)
        dot.move_to(sphere.get_boundary_point(np.array((1.0, 0.5, 0.0))))
        self.add(sphere,dot)

        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        axes1 = ThreeDAxes(
            x_range=[-5, 5, 1],
            x_length=10,
            y_range=[-4, 4, 1],
            y_length=8,
            axis_config={"include_numbers": True, "font_size": 30},
        )

        axes1.set_color(WHITE)
        axes1.add(axes1.get_x_axis_label("x1").set_color(WHITE).scale(0.8)) # add label for x-axis
        axes1.add(axes1.get_y_axis_label("y1").set_color(WHITE).scale(0.8)) # add label for y-axis
        axes1.add(axes1.get_z_axis_label("z1").set_color(WHITE).scale(0.8))  # add label for y-axis
        self.add(axes1)  # add all axes to the scene

        # 获取坐标轴的三个向量


        self.wait()
        axes1.set_opacity(0.5)

        # 第一个坐
        axes2= axes1.copy()
        axes2.set_color(YELLOW)
        dot.set_color(YELLOW)
        axes2.add(axes1.get_x_axis_label("x2").set_color(YELLOW).scale(0.8))  # add label for x-axis
        axes2.add(axes1.get_y_axis_label("y2").set_color(YELLOW).scale(0.8))  # add label for y-axis
        axes2.add(axes1.get_z_axis_label("z2").set_color(YELLOW).scale(0.8))  # add label for y-axis
        self.add(axes2)  # add all axes to the scene

        angle = 45 * DEGREES
        
        self.add(path)
        dot_rotate1= Rotate(dot,angle,axis=OUT,about_point=ORIGIN)
        axes_rotate1=Rotate(axes2,angle,axis=OUT,about_point=ORIGIN)
        self.play(axes_rotate1,dot_rotate1,run_time=1)


        # 第二个坐标
        self.wait()
        axes3 = axes2.copy()
        axes1.set_opacity(0.1)
        axes2.set_opacity(0.5)
        axes3.set_opacity(1)
        axes3.set_color(BLUE)
        dot.set_color(BLUE)
        axes3.add(axes1.get_x_axis_label("x3").set_color(BLUE).scale(0.8))  # add label for x-axis
        axes3.add(axes1.get_y_axis_label("y3").set_color(BLUE).scale(0.8))  # add label for y-axis
        axes3.add(axes1.get_z_axis_label("z3").set_color(BLUE).scale(0.8))  # add label for y-axis
        self.add(axes3)  # add all axes to the scene

        angle = 45 * DEGREES
        y_axis = axes2.get_y_axis()
        y_axis_v = y_axis.get_end() - y_axis.get_start()
        dot_rotate2 = Rotate(dot, angle, axis=y_axis_v, about_point=ORIGIN)
        axes_rotate2 = Rotate(axes3, angle, axis=y_axis_v, about_point=ORIGIN)
        self.play(axes_rotate2, dot_rotate2, run_time=1)

        #第三次旋转
        self.wait()
        axes4 = axes3.copy()
        axes2.set_opacity(0.1)
        axes3.set_opacity(0.5)
        axes4.set_opacity(1)
        axes4.set_color(RED)
        dot.set_color(RED)
        axes4.add(axes4.get_x_axis_label("x4").set_color(RED).scale(0.8))  # add label for x-axis
        axes4.add(axes4.get_y_axis_label("y4").set_color(RED).scale(0.8))  # add label for y-axis
        axes4.add(axes4.get_z_axis_label("z4").set_color(RED).scale(0.8))  # add label for y-axis
        self.add(axes4)  # add all axes to the scene

        angle = 45 * DEGREES
        x_axis = axes3.get_x_axis()
        x_axis_v = x_axis.get_end() - x_axis.get_start()
        dot_rotate3 = Rotate(dot, angle, axis=x_axis_v, about_point=ORIGIN)
        axes_rotate3 = Rotate(axes4, angle, axis=x_axis_v, about_point=ORIGIN)
        self.play(dot_rotate3, axes_rotate3, run_time=1)
        self.wait()

        axes1.set_opacity(1)
        axes2.set_opacity(0)
        axes3.set_opacity(0)
        axes4.set_opacity(0)
        self.wait()


class Orbit(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        sphere = OpenGLSphere(radius=1, color=BLUE)
        dot = OpenGLDot3D(radius=0.05, color=YELLOW)
        dot.move_to(sphere.get_boundary_point(UP))
        path = TracedPath(dot.get_center, stroke_color=dot.get_color())

        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        self.add(axes, sphere, dot, path)
        self.begin_ambient_camera_rotation(rate=0.3)

        self.play(Rotate(dot, 2 * PI, about_point=ORIGIN, axis=OUT))
        self.wait(2)

with tempconfig({"preview": True, "disable_caching": True, "quality": "medium_quality", "renderer": "opengl"}):
    RotationPath().render()
