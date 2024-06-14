from manim import *
from manim.mobject.geometry.tips import  ArrowTriangleFilledTipSmall
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



#
class ThreeDRotationVector001(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=35 * DEGREES)

        axes = ThreeDAxes(include_numbers=False,  axis_config={"include_ticks": False}, x_range=[-4, 4, 1], y_range=[-4, 4, 1], z_range=[-3, 3, 1], x_length=8,
                          y_length=8, z_length=6)
        axes.add(axes.get_axis_labels())
        # number_plane = NumberPlane(include_numbers=False, x_range=[-7, 7, 1], y_range=[-7, 7, 1], z_range=[-4, 4, 1],
        #                            x_length=14, y_length=14, z_length=8)
        # self.play(Create(number_plane))
        # self.play(Create(axes))
        vector_length=2
        # 创建基向量
        e1 = Vector([2,0,0], color=GRAY_A,stroke_width=1.5,tip_shape=ArrowTriangleFilledTipSmall)
        # e1.add(e1.coordinate_label())
        e2 = Vector([0,2,0], color=GRAY_A,stroke_width=1.5,tip_shape=ArrowTriangleFilledTipSmall)
        # e1.add(e2.coordinate_label())
        e3 = Vector([0,0,2], color=GRAY_A,stroke_width=1.5,tip_shape=ArrowTriangleFilledTipSmall)
        # e1.add(e3.coordinate_label())

        # dot1= Dot3D([1,0,0])
        # self.add(dot1)

        # 添加标签
        e1_label = MathTex("e_1").next_to(e1, UP+RIGHT, buff=0).scale(0.5).set_color(GRAY_A)
        e2_label = MathTex("e_2").next_to(e2, LEFT+UP, buff=0).scale(0.5).set_color(GRAY_A)
        e3_label = MathTex("e_3").next_to(e3, OUT, buff=0).scale(0.5).set_color(GRAY_A)

         # NumberLine().normal_vector

        self.add(axes)
        # self.add(e1, e1_label, e2, e2_label, e3, e3_label)

        self.play(Create(e1),Create(e2),Create(e3))
        self.add(e1, e1_label, e2, e2_label, e3)
        # self.add(e1, e2, e3)

        e1_p_label = MathTex("e_1'").next_to(e1, UP + RIGHT, buff=0).scale(0.5).set_color(GRAY_A)
        e2_p_label = MathTex("e_2'").next_to(e2, LEFT + UP, buff=0).scale(0.5).set_color(GRAY_A)
        e3_p_label = MathTex("e_3'").next_to(e3, OUT, buff=0).scale(0.5).set_color(GRAY_A)
        vector_group=Group()
        vector_group.add(e1, e1_p_label, e2, e2_p_label, e3)
        # vector_group.add(e1, e2, e3)



        self.wait(2)

        circle = Circle(radius=2, color=BLUE)

        self.play(Create(circle))
        # self.move_camera(zoom=1)
        # self.wait(2)

        self.move_camera(theta=0 * DEGREES, phi=0 * DEGREES, run_time=1)

        axes2 = ThreeDAxes(include_numbers=False, axis_config={"include_ticks": False}, x_range=[-4, 4, 1],
                          y_range=[-4, 4, 1], z_range=[-3, 3, 1], x_length=8,
                          y_length=8, z_length=6)
        axes2.set_color(BLUE)
        axes2.add(axes2.get_axis_labels(x_label="x'",y_label="y'",z_label="z'"))
        self.add(axes2)
        vector_group2 = vector_group.copy().set_color(BLUE_B)
        self.add(vector_group2)

        self.wait()
        theta=30*DEGREES
        matrix_y = np.array([
            [np.cos(theta), -np.sin(theta), 0],
            [np.sin(theta), np.cos(theta), 0],
            [0, 0, 1]
        ])


        start_rad = 30 * DEGREES
        end_rad = 90 * DEGREES

        start_point = circle.point_at_angle(start_rad)

        # start_vector = Vector(start_point, color=BLUE,stroke_width=1)
        start_arc = Arc(radius=0.7, start_angle=0, angle=start_rad, color=BLUE)
        start_arc_label = MathTex(r"\theta", color=BLUE).scale(0.7).next_to(start_arc, RIGHT, buff=0.15)

        end_arc = Arc(radius=0.7, start_angle=end_rad, angle=start_rad, color=BLUE)
        end_arc_label = MathTex(r"\theta", color=BLUE).scale(0.7).next_to(end_arc, UP, buff=0.15)

        self.play(
            ApplyMethod(axes2.apply_matrix, matrix_y),
                  ApplyMethod(vector_group2.apply_matrix, matrix_y),
                  Create(start_arc), Create(end_arc))

        self.add(circle, start_arc,start_arc_label,end_arc_label)

        start_lines = axes.get_lines_to_point(start_point)
        start_lines.set_color(BLUE)
        self.play(Create(start_lines))

        end_point = circle.point_at_angle(end_rad + start_rad)
        end_lines = axes.get_lines_to_point(end_point)
        end_lines.set_color(BLUE)
        self.play(Create(end_lines))


        axes2.get_z_axis_label().set_opacity(0)
        axes.get_z_axis_label().set_opacity(0)
        self.move_camera(frame_center=[5, 0, 0])
        self.wait()
        return
        tex = MathTex(r"""
        x' =& \sin( \theta+\alpha)   \\
        z' =& \cos(\theta+ \alpha) 
                """)

        tex.shift(np.array([7.5, 3, 0]))
        self.play(Write(tex))

        brace = Brace(tex, direction=LEFT)
        self.play(FadeIn(brace))

        tex1 = MathTex(r"""
        x' =& x\cos\alpha + z\sin\alpha \\
        y' =&y\\
        z' =& -x\sin\alpha + z\cos\alpha
                """)

        tex1.next_to(tex, direction=DOWN, buff=0.4)
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
        self.play(Write(tex12.next_to(tex1, direction=DOWN, buff=0.4)))
        image = self.renderer.get_frame()
        im = Image.fromarray(image)
        im.save("out_img/y-转动.png")


        return


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

        self.move_camera(theta=0 * DEGREES, phi=0 * DEGREES,run_time=1)

        self.move_camera(phi=55 * DEGREES, theta=35 * DEGREES)

        matrix_y= np.array([
            [0,0,1],
            [1,0,0],
            [0,1,0]
        ])
        self.play(ApplyMethod(axes.apply_matrix,matrix_y))
        self.move_camera(theta=0 * DEGREES, phi=0 * DEGREES)
        self.move_camera(phi=55 * DEGREES, theta=35 * DEGREES)
        self.wait()

        matrix_y = np.array([
            [0, 0, 1],
            [1, 0, 0],
            [0, 1, 0]
        ])
        self.play(ApplyMethod(axes.apply_matrix, matrix_y))
        self.move_camera(theta=0 * DEGREES, phi=0 * DEGREES)
        self.move_camera(phi=55 * DEGREES, theta=35 * DEGREES)
        self.wait()

        matrix_y = np.array([
            [0, 0, 1],
            [1, 0, 0],
            [0, 1, 0]
        ])
        self.play(ApplyMethod(axes.apply_matrix, matrix_y))
        self.move_camera(theta=0 * DEGREES, phi=0 * DEGREES)
        self.move_camera(phi=55 * DEGREES, theta=35 * DEGREES)
        self.wait()


with tempconfig({"preview": True, "disable_caching": False, "renderer": "opengl"}):
    ThreeDRotationVector001().render()
    exit(1)