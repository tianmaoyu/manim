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



# 逆时针旋转矩阵矩阵
class ThreeDRotation00test(ThreeDScene):
    def construct(self):

        tex1=MathTex(r"x' &= x\cos\alpha - y\sin\alpha\\"
                    r"y' &= x\sin\alpha + y\cos\alpha")
        tex1.to_corner(UP)
        brace1 = Brace(tex1, direction=LEFT)
        self.play(Write(tex1),FadeIn(brace1))

        tex2 = MathTex(r'''
        \begin{bmatrix}
cos(\alpha) & -sin(\alpha) \\
sin(\alpha) & cos(\alpha)
\end{bmatrix}
\cdot \begin{bmatrix} x \\ y \end{bmatrix} 
= \begin{bmatrix} x' \\ y' \end{bmatrix}
        ''')
        tex2.next_to(tex1,direction=DOWN*2)
        self.play(Write(tex2))

        tex3 = MathTex(r'''
R=
\begin{bmatrix}
cos(\theta) & -sin(\theta) \\
sin(\theta) & cos(\theta)
\end{bmatrix}
                ''')
        tex3.next_to(tex2, direction=DOWN*2)
        self.play(Write(tex3))

class ThreeDRotation000(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=35 * DEGREES)

        axes = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1], x_length=6,
                          y_length=6, z_length=6)
        axes.add(axes.get_axis_labels())
        number_plane = NumberPlane(include_numbers=False, x_range=[-7, 7, 1], y_range=[-7, 7, 1], z_range=[-4, 4, 1],
                                   x_length=14, y_length=14, z_length=8)
        self.play(Create(number_plane))
        self.play(Create(axes))


        start_rad = 30 * DEGREES

        circle = Circle(radius=2, color=BLUE)
        start_point = circle.point_at_angle(start_rad)
        start_dot = Dot(point=start_point, color=RED)
        start_vector = Vector(start_point,color=RED)
        start_arc = Arc(radius=1, start_angle=0, angle=start_rad, color=RED)
        start_arc_label = MathTex(r"\theta",color=RED).scale(0.7).next_to(start_arc, RIGHT, buff=0.15)

        self.add(circle,start_dot, start_vector, start_arc,start_arc_label)
        self.wait()

        start_lines = axes.get_lines_to_point(start_point)
        start_lines.set_color(RED)
        self.play(Create(start_lines))

        start_vector_label = MathTex(r"""\begin{bmatrix}x\\y\\z\end{bmatrix}""", color=RED).scale(0.7).next_to(start_dot, direction=RIGHT)
        self.play(Create(start_vector_label))


        #开始动画
        end_rad = 90 * DEGREES
        end_point = circle.point_at_angle(end_rad+start_rad)
        end_vector = start_vector.copy().set_color(YELLOW)
        end_dot = start_dot.copy().set_color(YELLOW)
        end_arc = Arc(radius=0.5, start_angle=start_rad, angle=end_rad, color=YELLOW)
        end_arc_label = MathTex(r"\alpha", color=YELLOW).scale(0.7).next_to(end_arc, UP, buff=0.15)

        self.play(Rotate(end_vector, angle=end_rad, about_point=circle.get_center()),
                        Rotate(end_dot, angle=end_rad, about_point=circle.get_center()),
                        Create(end_arc),
                        Create(end_arc_label),
                        run_time=2)



        end_lines = axes.get_lines_to_point(end_point)
        end_lines.set_color(YELLOW)
        self.play(Create(end_lines))

        end_vector_label = MathTex(r"""\begin{bmatrix}x'\\y'\\z'\end{bmatrix}""",color=YELLOW).scale(0.7).next_to(end_point,direction=LEFT)
        self.play(Create(end_vector_label))


        matrix_y= np.array([
            [0,0,1],
            [1,0,0],
            [0,1,0]
        ])
        self.play(ApplyMethod(axes.apply_matrix,matrix_y))

        self.move_camera(phi=75 * DEGREES, theta=35 * DEGREES)
        self.wait()

        matrix_y = np.array([
            [0, 0, 1],
            [1, 0, 0],
            [0, 1, 0]
        ])
        self.play(ApplyMethod(axes.apply_matrix, matrix_y))

        self.move_camera(phi=75 * DEGREES, theta=35 * DEGREES)
        self.wait()

        matrix_y = np.array([
            [0, 0, 1],
            [1, 0, 0],
            [0, 1, 0]
        ])
        self.play(ApplyMethod(axes.apply_matrix, matrix_y))

        self.move_camera(phi=75 * DEGREES, theta=35 * DEGREES)
        self.wait()




class ThreeDRotation00z(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(phi=65 * DEGREES, theta=35 * DEGREES)
        axes = ThreeDAxes(include_numbers=False, x_range=[-7, 7, 1], y_range=[-7, 7, 1], z_range=[-4, 4, 1], x_length=14, y_length=14, z_length=8)
        axes.add(axes.get_axis_labels())
        self.play(Create(axes))

        number_plane = NumberPlane(include_numbers=False, x_range=[-7, 7, 1], y_range=[-7, 7, 1], z_range=[-4, 4, 1], x_length=14, y_length=14, z_length=8)
        self.play(Create(number_plane))

        start_rad = 30 * DEGREES

        circle = Circle(radius=2, color=BLUE)
        start_point = circle.point_at_angle(start_rad)
        start_dot = Dot(point=start_point, color=RED)
        start_vector = Vector(start_point,color=RED)
        start_arc = Arc(radius=1, start_angle=0, angle=start_rad, color=RED)
        start_arc_label = MathTex(r"\theta",color=RED).scale(0.7).next_to(start_arc, RIGHT, buff=0.15)

        self.add(circle,start_dot, start_vector, start_arc,start_arc_label)
        self.wait()

        start_lines = axes.get_lines_to_point(start_point)
        start_lines.set_color(RED)
        self.play(Create(start_lines))

        start_vector_label = start_vector.coordinate_label(n_dim=3,color=RED).scale(0.7)
        start_vector_label = MathTex(r"""\begin{bmatrix}x\\y\\z\end{bmatrix}""", color=RED).scale(0.7).next_to(start_dot, direction=RIGHT)
        self.play(Create(start_vector_label))

        #开始动画
        end_rad = 90 * DEGREES
        end_point = circle.point_at_angle(end_rad+start_rad)
        end_vector = start_vector.copy().set_color(YELLOW)
        end_dot = start_dot.copy().set_color(YELLOW)
        end_arc = Arc(radius=0.5, start_angle=start_rad, angle=end_rad, color=YELLOW)
        end_arc_label = MathTex(r"\alpha", color=YELLOW).scale(0.7).next_to(end_arc, UP, buff=0.15)

        self.play(Rotate(end_vector, angle=end_rad, about_point=circle.get_center()),
                        Rotate(end_dot, angle=end_rad, about_point=circle.get_center()),
                        Create(end_arc),
                        Create(end_arc_label),
                        run_time=2)



        end_lines = axes.get_lines_to_point(end_point)
        end_lines.set_color(YELLOW)
        self.play(Create(end_lines))

        end_vector_label = end_vector.coordinate_label(n_dim=3,color=YELLOW).scale(0.7)
        end_vector_label = MathTex(r"""\begin{bmatrix}x'\\y'\\z'\end{bmatrix}""",color=YELLOW).scale(0.7).next_to(end_point,direction=LEFT)
        self.play(Create(end_vector_label))

        self.move_camera(theta=0*DEGREES, phi=0*DEGREES)

class ThreeDRotation00y(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(phi=65 * DEGREES, theta=35 * DEGREES)

        axes = ThreeDAxes(include_numbers=False, x_range=[-4, 4, 1], y_range=[-4, 4, 1], z_range=[-4, 4, 1], x_length=8, y_length=8, z_length=8)
        axes.add(axes.get_axis_labels(x_label="z",y_label="x",z_label="y"))
        self.play(Create(axes))

        number_plane = NumberPlane(include_numbers=False, x_range=[-7, 7, 1], y_range=[-7, 7, 1], z_range=[-4, 4, 1], x_length=14, y_length=14, z_length=8)
        self.play(Create(number_plane))


        start_rad = 30 * DEGREES

        circle = Circle(radius=2, color=BLUE)
        start_point = circle.point_at_angle(start_rad)
        start_dot = Dot(point=start_point, color=RED)
        start_vector = Vector(start_point,color=RED)
        start_arc = Arc(radius=1, start_angle=0, angle=start_rad, color=RED)
        start_arc_label = MathTex(r"\theta",color=RED).scale(0.7).next_to(start_arc, RIGHT, buff=0.15)

        self.add(circle,start_dot, start_vector, start_arc,start_arc_label)
        self.wait()

        start_lines = axes.get_lines_to_point(start_point)
        start_lines.set_color(RED)
        self.play(Create(start_lines))

        start_vector_label = MathTex(r"""\begin{bmatrix}x\\..\\z\end{bmatrix}""", color=RED).scale(0.7).next_to(start_dot, direction=RIGHT)
        self.play(Create(start_vector_label))


        #开始动画
        end_rad = 90 * DEGREES
        end_point = circle.point_at_angle(end_rad+start_rad)
        end_vector = start_vector.copy().set_color(YELLOW)
        end_dot = start_dot.copy().set_color(YELLOW)
        end_arc = Arc(radius=0.5, start_angle=start_rad, angle=end_rad, color=YELLOW)
        end_arc_label = MathTex(r"\alpha", color=YELLOW).scale(0.7).next_to(end_arc, UP, buff=0.15)

        self.play(Rotate(end_vector, angle=end_rad, about_point=circle.get_center()),
                        Rotate(end_dot, angle=end_rad, about_point=circle.get_center()),
                        Create(end_arc),
                        Create(end_arc_label),
                        run_time=2)



        end_lines = axes.get_lines_to_point(end_point)
        end_lines.set_color(YELLOW)
        self.play(Create(end_lines))

        end_vector_label = MathTex(r"""\begin{bmatrix}x'\\..\\z'\end{bmatrix}""",color=YELLOW).scale(0.7).next_to(end_point,direction=LEFT)
        self.play(Create(end_vector_label))

        self.move_camera(theta=0 * DEGREES, phi=0 * DEGREES)





        # self.move_camera(theta=10*DEGREES, phi=30*DEGREES)

class ThreeDRotation00x(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(phi=65 * DEGREES, theta=35 * DEGREES)

        axes = ThreeDAxes(include_numbers=False, x_range=[-4, 4, 1], y_range=[-4, 4, 1], z_range=[-4, 4, 1], x_length=8, y_length=8, z_length=8)
        axes.add(axes.get_axis_labels(x_label="y",y_label="z",z_label="x"))
        self.play(Create(axes))

        number_plane = NumberPlane(include_numbers=False, x_range=[-7, 7, 1], y_range=[-7, 7, 1], z_range=[-4, 4, 1], x_length=14, y_length=14, z_length=8)
        self.play(Create(number_plane))


        start_rad = 30 * DEGREES

        circle = Circle(radius=2, color=BLUE)
        start_point = circle.point_at_angle(start_rad)
        start_dot = Dot(point=start_point, color=RED)
        start_vector = Vector(start_point,color=RED)
        start_arc = Arc(radius=1, start_angle=0, angle=start_rad, color=RED)
        start_arc_label = MathTex(r"\theta",color=RED).scale(0.7).next_to(start_arc, RIGHT, buff=0.15)

        self.add(circle,start_dot, start_vector, start_arc,start_arc_label)
        self.wait()

        start_lines = axes.get_lines_to_point(start_point)
        start_lines.set_color(RED)
        self.play(Create(start_lines))

        start_vector_label = MathTex(r"""\begin{bmatrix}..\\y\\z\end{bmatrix}""", color=RED).scale(0.7).next_to(start_dot, direction=RIGHT)
        self.play(Create(start_vector_label))


        #开始动画
        end_rad = 90 * DEGREES
        end_point = circle.point_at_angle(end_rad+start_rad)
        end_vector = start_vector.copy().set_color(YELLOW)
        end_dot = start_dot.copy().set_color(YELLOW)
        end_arc = Arc(radius=0.5, start_angle=start_rad, angle=end_rad, color=YELLOW)
        end_arc_label = MathTex(r"\alpha", color=YELLOW).scale(0.7).next_to(end_arc, UP, buff=0.15)

        self.play(Rotate(end_vector, angle=end_rad, about_point=circle.get_center()),
                        Rotate(end_dot, angle=end_rad, about_point=circle.get_center()),
                        Create(end_arc),
                        Create(end_arc_label),
                        run_time=2)



        end_lines = axes.get_lines_to_point(end_point)
        end_lines.set_color(YELLOW)
        self.play(Create(end_lines))

        end_vector_label = MathTex(r"""\begin{bmatrix}..\\y'\\z'\end{bmatrix}""",color=YELLOW).scale(0.7).next_to(end_point,direction=LEFT)
        self.play(Create(end_vector_label))

        self.move_camera(theta=0 * DEGREES, phi=0 * DEGREES)


with tempconfig({"preview": True, "disable_caching": True, "renderer": "opengl"}):
    ThreeDRotation000().render()
    exit(1)
