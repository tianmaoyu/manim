from manim import *
from manim.mobject.opengl.opengl_cylinder import OpenGLCylinder
from manim.mobject.opengl.opengl_image_mobject import OpenGLImageMobject
from manim.mobject.opengl.opengl_point_image_mobject import ImagePixelMobject, NumpyImage
from manim.mobject.opengl.opengl_shpere import OpenGLSphere
from manim.mobject.opengl.opengl_something import OpenGLCone, OpenGLLine3D, OpenGLArrow3D
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface, OpenGLSurface
import numpy as np
import sympy as sp
from manim.typing import Image
from PIL import Image







#
class Show001(ThreeDScene):

    def construct(self):
        self.next_section("1", skip_animations=True)

        self.set_camera_orientation(phi=70 * DEGREES, theta=35 * DEGREES)

        axes = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1], x_length=6,
                          y_length=6, z_length=6)
        axes.add(axes.get_axis_labels())
        number_plane = NumberPlane(include_numbers=False, x_range=[-7, 7, 1], y_range=[-7, 7, 1], z_range=[-4, 4, 1],
                                   x_length=14, y_length=14, z_length=8)
        self.add(number_plane)
        self.add(axes)

        rule_image = ImagePixelMobject("src/output_image.png", image_width=4, is_fixed_in_frame=True)
        rule_image.to_center()
        rule_image.to_corner(UL)
        self.add(rule_image)

        center = np.array([0, 0, 2])
        arc = Arc(radius=0.5, arc_center=center, start_angle=0, angle=290 * DEGREES, color=BLUE_D)
        self.play(Create(arc))

        # 添加一个箭头
        end_point = arc.get_end()
        radius_vector = end_point
        tangent_vector = np.array([-radius_vector[1], radius_vector[0], 0])
        arrow = OpenGLCone(height=0.2, base_radius=0.1, direction=tangent_vector, color=BLUE_D)
        arrow.move_to(end_point)
        self.play(Create(arrow))



        number_plane.get_axes().set_color(RED)
        rotate = Rotate(axes, angle=30 * DEGREES)
        self.play(rotate)

        rotate = Rotate(axes, angle=-30 * DEGREES)
        self.play(rotate)

        self.wait()



        start_rad = 30 * DEGREES

        circle = Circle(radius=2, color=BLUE)
        start_point = circle.point_at_angle(start_rad)
        start_dot = Dot(point=start_point, color=RED)
        start_vector = Vector(start_point, color=RED)
        start_arc = Arc(radius=1, start_angle=0, angle=start_rad, color=RED)
        start_arc_label = MathTex(r"\theta", color=RED).scale(0.7).next_to(start_arc, RIGHT, buff=0.15)

        self.add(circle,start_dot, start_vector, start_arc,start_arc_label)

        start_lines = axes.get_lines_to_point(start_point)
        start_lines.set_color(RED)
        self.play(Create(start_lines))

        start_vector_label = MathTex(r"""\begin{bmatrix}x\\y\\z\end{bmatrix}""", color=RED).scale(0.7).next_to(
            start_dot, direction=RIGHT)
        self.play(Create(start_vector_label))

        # 开始动画
        end_rad = 90 * DEGREES
        end_point = circle.point_at_angle(end_rad + start_rad)
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

        end_vector_label = MathTex(r"""\begin{bmatrix}x'\\y'\\z'\end{bmatrix}""", color=YELLOW).scale(0.7).next_to(
            end_point, direction=LEFT)
        self.play(Create(end_vector_label))
        self.move_camera(theta=0 * DEGREES, phi=0 * DEGREES)


        self.next_section("1", skip_animations=False)
        self.wait()
        self.play(FadeOut(number_plane),FadeOut(rule_image),FadeOut(arc),FadeOut(arrow))
        self.move_camera(frame_center=[5.5,0,0])
        self.wait()

        tex = MathTex(r"""
x' =& \cos( \theta+\alpha)   \\
y' =& \sin(\theta+ \alpha) 
        """)

        tex.shift(np.array([7, 3, 0]))
        self.play(Write(tex))

        brace = Brace(tex, direction=LEFT)
        self.play(FadeIn(brace))

        tex1 = MathTex(r"""
x' =& x\cos\alpha-y\sin\alpha \\
y' =& x\sin\alpha +y\cos\alpha \\
z' =& z
        """)

        tex1.next_to(tex, direction=DOWN,buff=0.4)
        brace1 = Brace(tex1, direction=LEFT)
        self.play(Write(tex1), FadeIn(brace1))

        tex12 = MathTex(r"""
\begin{bmatrix} x' \\ y' \\z' \end{bmatrix}
=
\begin{bmatrix} 
cos(\alpha) & -sin(\alpha) &0 \\ 
sin(\alpha) & cos(\alpha) &0\\
0 & 0 &1
\end{bmatrix}
\cdot 
\begin{bmatrix} x \\ y \\z \end{bmatrix}
                """)
        self.play(Write(tex12.next_to(tex1,direction=DOWN,buff=0.4)))
        image = self.renderer.get_frame()
        im = Image.fromarray(image)
        im.save("out_img/z-转动.png")

class Show002(ThreeDScene):

    def construct(self):
        self.next_section("1", skip_animations=True)

        self.set_camera_orientation(phi=70 * DEGREES, theta=35 * DEGREES)

        axes = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1], x_length=6,
                          y_length=6, z_length=6)
        axes.add(axes.get_axis_labels())
        number_plane = NumberPlane(include_numbers=False, x_range=[-7, 7, 1], y_range=[-7, 7, 1], z_range=[-4, 4, 1],
                                   x_length=14, y_length=14, z_length=8)
        self.add(number_plane)
        self.add(axes)

        rule_image = ImagePixelMobject("src/output_image.png", image_width=4, is_fixed_in_frame=True)
        rule_image.to_center()
        rule_image.to_corner(UL)
        self.add(rule_image)

        center = np.array([0, 0, 2])
        arc = Arc(radius=0.5, arc_center=center, start_angle=0, angle=290 * DEGREES, color=BLUE_D)
        self.play(Create(arc))

        # 添加一个箭头
        end_point = arc.get_end()
        radius_vector = end_point
        tangent_vector = np.array([-radius_vector[1], radius_vector[0], 0])
        arrow = OpenGLCone(height=0.2, base_radius=0.1, direction=tangent_vector, color=BLUE_D)
        arrow.move_to(end_point)
        self.play(Create(arrow))



        number_plane.get_axes().set_color(RED)
        rotate = Rotate(axes, angle=30 * DEGREES)
        self.play(rotate)

        rotate = Rotate(axes, angle=-30 * DEGREES)
        self.play(rotate)

        self.wait()



        start_rad = 30 * DEGREES

        circle = Circle(radius=2, color=BLUE)
        start_point = circle.point_at_angle(start_rad)
        start_dot = Dot(point=start_point, color=RED)
        start_vector = Vector(start_point, color=RED)
        start_arc = Arc(radius=1, start_angle=0, angle=start_rad, color=RED)
        start_arc_label = MathTex(r"\theta", color=RED).scale(0.7).next_to(start_arc, RIGHT, buff=0.15)

        self.add(circle,start_dot, start_vector, start_arc,start_arc_label)

        start_lines = axes.get_lines_to_point(start_point)
        start_lines.set_color(RED)
        self.play(Create(start_lines))

        start_vector_label = MathTex(r"""\begin{bmatrix}x\\y\\z\end{bmatrix}""", color=RED).scale(0.7).next_to(
            start_dot, direction=RIGHT)
        self.play(Create(start_vector_label))

        # 开始动画
        end_rad = 90 * DEGREES
        end_point = circle.point_at_angle(end_rad + start_rad)
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

        end_vector_label = MathTex(r"""\begin{bmatrix}x'\\y'\\z'\end{bmatrix}""", color=YELLOW).scale(0.7).next_to(
            end_point, direction=LEFT)
        self.play(Create(end_vector_label))
        self.move_camera(theta=0 * DEGREES, phi=0 * DEGREES)

        matrix_y = np.array([
            [0, 0, 1],
            [1, 0, 0],
            [0, 1, 0]
        ])
        self.play(ApplyMethod(axes.apply_matrix, matrix_y))
        self.move_camera(theta=0 * DEGREES, phi=0 * DEGREES)

        self.next_section("1", skip_animations=False)
        self.wait()
        self.play(FadeOut(number_plane),FadeOut(rule_image),FadeOut(arc),FadeOut(arrow))
        self.move_camera(frame_center=[5.5,0,0])
        self.wait()

        tex = MathTex(r"""
x' =& \sin( \theta+\alpha)   \\
z' =& \cos(\theta+ \alpha) 
        """)

        tex.shift(np.array([7, 3, 0]))
        self.play(Write(tex))

        brace = Brace(tex, direction=LEFT)
        self.play(FadeIn(brace))

        tex1 = MathTex(r"""
x' =& x\cos\alpha + z\sin\alpha \\
y' =&y\\
z' =& -x\sin\alpha + z\cos\alpha
        """)

        tex1.next_to(tex, direction=DOWN,buff=0.4)
        brace1 = Brace(tex1, direction=LEFT)
        self.play(Write(tex1), FadeIn(brace1))

        tex12 = MathTex(r"""
\begin{bmatrix} x' \\ y' \\z' \end{bmatrix}
=
\begin{bmatrix} 
cos(\alpha) & 0& sin(\alpha)  \\ 
0 & 1 &0\\
-sin(\alpha) & 0 & cos(\alpha) 
\end{bmatrix}
\cdot 
\begin{bmatrix} x \\ y \\z \end{bmatrix}
                """)
        self.play(Write(tex12.next_to(tex1,direction=DOWN,buff=0.4)))
        image = self.renderer.get_frame()
        im = Image.fromarray(image)
        im.save("out_img/y-转动.png")

class Show003(ThreeDScene):

    def construct(self):
        self.next_section("1", skip_animations=True)

        self.set_camera_orientation(phi=70 * DEGREES, theta=35 * DEGREES)

        axes = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1], x_length=6,
                          y_length=6, z_length=6)
        axes.add(axes.get_axis_labels())
        number_plane = NumberPlane(include_numbers=False, x_range=[-7, 7, 1], y_range=[-7, 7, 1], z_range=[-4, 4, 1],
                                   x_length=14, y_length=14, z_length=8)
        self.add(number_plane)
        self.add(axes)

        rule_image = ImagePixelMobject("src/output_image.png", image_width=4, is_fixed_in_frame=True)
        rule_image.to_center()
        rule_image.to_corner(UL)
        self.add(rule_image)

        center = np.array([0, 0, 2])
        arc = Arc(radius=0.5, arc_center=center, start_angle=0, angle=290 * DEGREES, color=BLUE_D)
        self.play(Create(arc))

        # 添加一个箭头
        end_point = arc.get_end()
        radius_vector = end_point
        tangent_vector = np.array([-radius_vector[1], radius_vector[0], 0])
        arrow = OpenGLCone(height=0.2, base_radius=0.1, direction=tangent_vector, color=BLUE_D)
        arrow.move_to(end_point)
        self.play(Create(arrow))



        number_plane.get_axes().set_color(RED)
        rotate = Rotate(axes, angle=30 * DEGREES)
        self.play(rotate)

        rotate = Rotate(axes, angle=-30 * DEGREES)
        self.play(rotate)

        self.wait()



        start_rad = 30 * DEGREES

        circle = Circle(radius=2, color=BLUE)
        start_point = circle.point_at_angle(start_rad)
        start_dot = Dot(point=start_point, color=RED)
        start_vector = Vector(start_point, color=RED)
        start_arc = Arc(radius=1, start_angle=0, angle=start_rad, color=RED)
        start_arc_label = MathTex(r"\theta", color=RED).scale(0.7).next_to(start_arc, RIGHT, buff=0.15)

        self.add(circle,start_dot, start_vector, start_arc,start_arc_label)

        start_lines = axes.get_lines_to_point(start_point)
        start_lines.set_color(RED)
        self.play(Create(start_lines))

        start_vector_label = MathTex(r"""\begin{bmatrix}x\\y\\z\end{bmatrix}""", color=RED).scale(0.7).next_to(
            start_dot, direction=RIGHT)
        self.play(Create(start_vector_label))

        # 开始动画
        end_rad = 90 * DEGREES
        end_point = circle.point_at_angle(end_rad + start_rad)
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

        end_vector_label = MathTex(r"""\begin{bmatrix}x'\\y'\\z'\end{bmatrix}""", color=YELLOW).scale(0.7).next_to(
            end_point, direction=LEFT)
        self.play(Create(end_vector_label))
        self.move_camera(theta=0 * DEGREES, phi=0 * DEGREES)

        matrix_y = np.array([
            [0, 0, 1],
            [1, 0, 0],
            [0, 1, 0]
        ])
        self.play(ApplyMethod(axes.apply_matrix, matrix_y))
        self.move_camera(theta=0 * DEGREES, phi=0 * DEGREES)
        matrix_y = np.array([
            [0, 0, 1],
            [1, 0, 0],
            [0, 1, 0]
        ])
        self.play(ApplyMethod(axes.apply_matrix, matrix_y))

        self.next_section("1", skip_animations=False)
        self.wait()
        self.play(FadeOut(number_plane),FadeOut(rule_image),FadeOut(arc),FadeOut(arrow))
        self.move_camera(frame_center=[5.5,0,0])
        self.wait()

        tex = MathTex(r"""
y' =& \cos( \theta+\alpha)   \\
z' =& \sin(\theta+ \alpha) 
        """)

        tex.shift(np.array([7, 3, 0]))
        self.play(Write(tex))

        brace = Brace(tex, direction=LEFT)
        self.play(FadeIn(brace))

        tex1 = MathTex(r"""
x' =& x \\
y' =& y\cos\alpha - z\sin\alpha \\
z' =& y\sin\alpha + z\cos\alpha
        """)

        tex1.next_to(tex, direction=DOWN,buff=0.4)
        brace1 = Brace(tex1, direction=LEFT)
        self.play(Write(tex1), FadeIn(brace1))

        tex12 = MathTex(r"""
\begin{bmatrix} x' \\ y' \\z' \end{bmatrix}
=
\begin{bmatrix}
1&0&0\\
0&\cos\alpha& -sin\alpha\\
0 &sin\alpha &cos\alpha
\end{bmatrix}
\cdot
\begin{bmatrix} x \\ y \\z \end{bmatrix}
                """)
        self.play(Write(tex12.next_to(tex1,direction=DOWN,buff=0.4)))
        image = self.renderer.get_frame()
        im = Image.fromarray(image)
        im.save("out_img/x-转动.png")

with tempconfig({"preview": True, "disable_caching": True, "renderer": "opengl"}):
    Show001().render()
    exit(1)
