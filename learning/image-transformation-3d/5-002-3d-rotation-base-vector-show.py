from manim import *
from manim.mobject.geometry.tips import  ArrowTriangleFilledTipSmall
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


class ThreeDRotationVector向量基础(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=35 * DEGREES)

        axes = ThreeDAxes(include_numbers=False, axis_config={"include_ticks": False}, x_range=[-4, 4, 1],
                          y_range=[-4, 4, 1], z_range=[-3, 3, 1], x_length=8,
                          y_length=8, z_length=6)
        axes.add(axes.get_axis_labels())
        # number_plane = NumberPlane(include_numbers=False, x_range=[-7, 7, 1], y_range=[-7, 7, 1], z_range=[-4, 4, 1],
        #                            x_length=14, y_length=14, z_length=8)
        # self.play(Create(number_plane))
        # self.play(Create(axes))
        vector_length = 2
        # 创建基向量
        e1 = Vector([2, 0, 0], color=RED, stroke_width=3.5, tip_shape=ArrowTriangleFilledTipSmall)
        e2 = Vector([0, 2, 0], color=RED, stroke_width=3.5, tip_shape=ArrowTriangleFilledTipSmall)
        e3 = Vector([0, 0, 2], color=RED, stroke_width=3.5, tip_shape=ArrowTriangleFilledTipSmall)



        # 添加标签
        e1_label = MathTex("e_1").next_to(e1, UP + RIGHT, buff=0).scale(1).set_color(RED)
        e2_label = MathTex("e_2").next_to(e2, LEFT + UP, buff=0).scale(1).set_color(RED)
        e3_label = MathTex("e_3").next_to(e3, OUT, buff=0).scale(1).set_color(RED)
        self.add(axes)


        self.play(Create(e1), Create(e2), Create(e3))
        self.add(e1, e1_label, e2, e2_label, e3, e3_label)

        self.wait()


        start_dot= Dot3D(point=[0,0,0],color=BLUE)
        end_dot=Dot3D([2,2,2],color=BLUE)
        self.play(Create(start_dot),Create(end_dot))

        start_dot_lables= MathTex("O(0,0,0)").scale(0.4)
        # start_dot_lables.shift([0,0,0])
        start_dot_lables.next_to(start_dot)
        # self.add_fixed_orientation_mobjects(start_dot_lables)
        self.add(start_dot_lables)

        end_dot_lables= MathTex("P(x,y,z)").scale(0.4)
        # end_dot_lables.shift([2,2,2])
        end_dot_lables.next_to(end_dot)
        # self.add_fixed_orientation_mobjects(end_dot_lables)
        self.add(end_dot_lables)




        # self.add(dot_lables.next_to(end_dot).rotate(axis=RIGHT,about_point=dot_lables.get_center(),angle=90*DEGREES))


        vector=OpenGLArrow3D(start=[0,0,0],end=[2,2,2],color=BLUE)
        self.play(Create(vector))

        self.begin_ambient_camera_rotation(rate=1)
        # self.wait(2)

        # return
        # self.move_camera(theta=0 * DEGREES, phi=0 * DEGREES)

        # self.remove_fixed_orientation_mobjects(end_dot_lables)
        # self.remove_fixed_orientation_mobjects(start_dot_lables)


        self.move_camera(frame_center=[6, 0, 0])

        # start_dot_lables= MathTex("O(0,0,0)").scale(0.4)
        # start_dot_lables.shift([-6,0,0])
        # self.add_fixed_orientation_mobjects(start_dot_lables)
        #
        # end_dot_lables= MathTex("P(x,y,z)").scale(0.4)
        # end_dot_lables.shift([-4,2,2])
        # self.add_fixed_orientation_mobjects(end_dot_lables)


        self.wait()


        tex1 = MathTex(r"""
\vec{e_1}=\begin{bmatrix} 1 \\ 0 \\ 0\end{bmatrix}
        """)

        self.add_fixed_in_frame_mobjects(tex1)
        # tex1.shift(np.array([7.5, 3, 0]))

        tex2 = MathTex(r"""
        \vec{e_2}=\begin{bmatrix} 0 \\ 1 \\ 0\end{bmatrix}
                """)
        self.add_fixed_in_frame_mobjects(tex2)
        tex3 = MathTex(r"""
        \vec{e_3}=\begin{bmatrix} 0\\ 0 \\ 1\end{bmatrix}
                """)
        self.add_fixed_in_frame_mobjects( tex3)
        self.play(Write(tex1.to_corner(UP)))
        self.play(Write(tex2.next_to(tex1)))
        self.play(Write(tex3.next_to(tex2)))

        self.wait()

class ThreeDRotationVector向量基础2(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=35 * DEGREES)

        axes = ThreeDAxes(include_numbers=False, axis_config={"include_ticks": False}, x_range=[-4, 4, 1],
                          y_range=[-4, 4, 1], z_range=[-3, 3, 1], x_length=8,
                          y_length=8, z_length=6)
        axes.add(axes.get_axis_labels())
        # number_plane = NumberPlane(include_numbers=False, x_range=[-7, 7, 1], y_range=[-7, 7, 1], z_range=[-4, 4, 1],
        #                            x_length=14, y_length=14, z_length=8)
        # self.play(Create(number_plane))
        # self.play(Create(axes))
        vector_length = 2
        # 创建基向量
        e1 = Vector([2, 0, 0], color=RED, stroke_width=3.5, tip_shape=ArrowTriangleFilledTipSmall)
        e2 = Vector([0, 2, 0], color=RED, stroke_width=3.5, tip_shape=ArrowTriangleFilledTipSmall)
        e3 = Vector([0, 0, 2], color=RED, stroke_width=3.5, tip_shape=ArrowTriangleFilledTipSmall)



        # 添加标签
        e1_label = MathTex("e_1").next_to(e1, UP + RIGHT, buff=0).scale(1).set_color(RED)
        e2_label = MathTex("e_2").next_to(e2, LEFT + UP, buff=0).scale(1).set_color(RED)
        e3_label = MathTex("e_3").next_to(e3, OUT, buff=0).scale(1).set_color(RED)
        self.add(axes)


        self.play(Create(e1), Create(e2), Create(e3))
        self.add(e1, e1_label, e2, e2_label, e3, e3_label)

        self.wait()


        start_dot= Dot3D(point=[0,0,0],color=BLUE)
        end_dot=Dot3D([2,2,2],color=BLUE)
        self.play(Create(start_dot),Create(end_dot))

        start_dot_lables= MathTex("O(0,0,0)").scale(0.4)
        start_dot_lables.shift([0,0,0])
        self.add_fixed_orientation_mobjects(start_dot_lables)

        end_dot_lables= MathTex("P(x,y,z)").scale(0.4)
        end_dot_lables.shift([2,2,2])
        self.add_fixed_orientation_mobjects(end_dot_lables)




        # self.add(dot_lables.next_to(end_dot).rotate(axis=RIGHT,about_point=dot_lables.get_center(),angle=90*DEGREES))


        vector=OpenGLArrow3D(start=[0,0,0],end=[2,2,2],color=BLUE)
        self.play(Create(vector))

        # self.begin_ambient_camera_rotation(rate=1)
        # self.wait(2)

        # return
        self.move_camera(theta=0 * DEGREES, phi=0 * DEGREES)
        self.move_camera(frame_center=[5, 0, 0])
        self.wait()


        tex1 = MathTex(r"""
\vec{e_1}=\begin{bmatrix} 1 \\ 0 \\ 0\end{bmatrix}
        """)

        tex1.shift(np.array([7.5, 3, 0]))

        tex2 = MathTex(r"""
        \vec{e_2}=\begin{bmatrix} 0 \\ 1 \\ 0\end{bmatrix}
                """)
        tex3 = MathTex(r"""
        \vec{e_3}=\begin{bmatrix} 0\\ 0 \\ 1\end{bmatrix}
                """)

        self.play(Write(tex1.to_corner(UP)))
        self.play(Write(tex2.next_to(tex1)))
        self.play(Write(tex3.next_to(tex2)))

        self.wait()
class ThreeDRotationVectorLatex(ThreeDScene):
    def construct(self):
        tex1 = MathTex(r"""
\vec{e_1}=\begin{bmatrix} 1 \\ 0 \\ 0\end{bmatrix}
        """)
        tex2 = MathTex(r"""
        \vec{e_2}=\begin{bmatrix} 0 \\ 1 \\ 0\end{bmatrix}
                """)
        tex3 = MathTex(r"""
        \vec{e_3}=\begin{bmatrix} 0\\ 0 \\ 1\end{bmatrix}
                """)

        self.play(Write(tex1.to_corner(UP)))
        self.play(Write(tex2.next_to(tex1)))
        self.play(Write(tex3.next_to(tex2)))

        self.wait()


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

        #
        # axes2.get_z_axis_label().set_opacity(0)
        # axes.get_z_axis_label().set_opacity(0)
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

class ThreeDRotationVector002(ThreeDScene):
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

        self.wait()





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

        #
        # axes2.get_z_axis_label().set_opacity(0)
        # axes.get_z_axis_label().set_opacity(0)
        self.move_camera(frame_center=[5, 0, 0])
        self.wait()

        tex1 = MathTex(r"""
        \vec{e_1}=\begin{bmatrix} 1 \\ 0 \\ 0\end{bmatrix}
                """).scale(0.6)

        tex2 = MathTex(r"""
                \vec{e_2}=\begin{bmatrix} 0 \\ 1 \\ 0\end{bmatrix}
                        """).scale(0.6)

        tex3 = MathTex(r"""
                \vec{e_3}=\begin{bmatrix} 0\\ 0 \\ 1\end{bmatrix}
                        """).scale(0.6)
        tex1.shift(np.array([7.5, 3, 0]))
        self.play(Write(tex1))
        self.play(Write(tex2.next_to(tex1)))
        self.play(Write(tex3.next_to(tex2)))

        # self.add_fixed_in_frame_mobjects(tex3)
        # self.add_fixed_in_frame_mobjects(tex2)
        # self.add_fixed_in_frame_mobjects(tex1)

        tex21 = MathTex(r"""
       \vec{e_1}' =& \begin{bmatrix} \cos(\theta) \\  \sin(\theta) \\ 0\end{bmatrix}\\
                """).scale(0.6)

        tex22 = MathTex(r"""
                \vec{e_2}'=& \begin{bmatrix} -\sin(\theta) \\ \cos(\theta) \\ 0\end{bmatrix}\\
                        """).scale(0.6)

        tex23 = MathTex(r"""
                \vec{e_3}'=&\begin{bmatrix} 0\\ 0 \\ 1\end{bmatrix}
                        """).scale(0.6)
        tex21.shift(np.array([7.5, 2, 0]))
        self.play(Write(tex21))
        self.play(Write(tex22.next_to(tex21)))
        self.play(Write(tex23.next_to(tex21)))

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

class ThreeDRotationVector_x_y_z(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=35 * DEGREES)

        axes = ThreeDAxes(include_numbers=False,  axis_config={"include_ticks": False}, x_range=[-4, 4, 1], y_range=[-4, 4, 1], z_range=[-3, 3, 1], x_length=8,
                          y_length=8, z_length=6)
        axes.add(axes.get_axis_labels(x_label="X",y_label="Y",z_label="Z"))

        e1 = Vector([2,0,0], color=GRAY_A,stroke_width=1.5,tip_shape=ArrowTriangleFilledTipSmall)
        e2 = Vector([0,2,0], color=GRAY_A,stroke_width=1.5,tip_shape=ArrowTriangleFilledTipSmall)
        e3 = Vector([0,0,2], color=GRAY_A,stroke_width=1.5,tip_shape=ArrowTriangleFilledTipSmall)

        # 添加标签
        e1_label = MathTex("e_1").next_to(e1, UP+RIGHT, buff=0).scale(0.5).set_color(GRAY_A)
        e2_label = MathTex("e_2").next_to(e2, LEFT+UP, buff=0).scale(0.5).set_color(GRAY_A)
        e3_label = MathTex("e_3").next_to(e3, OUT, buff=0).scale(0.5).set_color(GRAY_A)

        self.add(axes)

        self.play(Create(e1),Create(e2),Create(e3))
        self.add(e1, e1_label, e2, e2_label, e3,e3_label)
        self.wait()

        group = Group()
        group.add(e1, e1_label, e2, e2_label, e3,e3_label)

        self.move_camera(theta=0 * DEGREES, phi=0 * DEGREES,run_time=1)

        self.move_camera(phi=55 * DEGREES, theta=35 * DEGREES)

        matrix_y= np.array([
            [0,0,1],
            [1,0,0],
            [0,1,0]
        ])
        self.play(ApplyMethod(axes.apply_matrix,matrix_y),ApplyMethod(group.apply_matrix,matrix_y))
        self.move_camera(theta=0 * DEGREES, phi=0 * DEGREES)
        self.move_camera(phi=55 * DEGREES, theta=35 * DEGREES)
        self.wait()


        self.play(ApplyMethod(axes.apply_matrix, matrix_y),ApplyMethod(group.apply_matrix,matrix_y))
        self.move_camera(theta=0 * DEGREES, phi=0 * DEGREES)
        self.move_camera(phi=55 * DEGREES, theta=35 * DEGREES)
        self.wait()


        self.play(ApplyMethod(axes.apply_matrix, matrix_y),ApplyMethod(group.apply_matrix,matrix_y))
        self.move_camera(theta=0 * DEGREES, phi=0 * DEGREES)
        self.move_camera(phi=55 * DEGREES, theta=35 * DEGREES)
        self.wait()

#标准单位基
class ThreeDRotationVector_base_vector(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=35 * DEGREES)

        axes = ThreeDAxes(include_numbers=False,  axis_config={"include_ticks": False}, x_range=[-5, 5, 1], y_range=[-5, 5, 1], z_range=[-4, 4, 1], x_length=10,
                          y_length=10, z_length=8)
        axes.add(axes.get_axis_labels(x_label="X",y_label="Y",z_label="Z"))

        e1 = Vector([2,0,0], color=RED)
        e2 = Vector([0,2,0], color=RED)
        e3 = Vector([0,0,2], color=RED)

        # 添加标签
        e1_label = MathTex("e_1").next_to(e1, UP+RIGHT, buff=0).set_color(RED)
        e2_label = MathTex("e_2").next_to(e2, LEFT+UP, buff=0).set_color(RED)
        e3_label = MathTex("e_3").next_to(e3, OUT, buff=0).set_color(RED)

        self.add(axes)
        number_plane = NumberPlane(include_numbers=False, x_range=[-7, 7, 1], y_range=[-7, 7, 1], z_range=[-4, 4, 1],
                                   x_length=14, y_length=14, z_length=8)
        self.add(number_plane)

        self.play(Create(e1),Create(e2),Create(e3))
        self.add(e1, e1_label, e2, e2_label, e3,e3_label)
        self.wait()

        self.begin_ambient_camera_rotation(rate=0.5)

        tex1 = MathTex(r"""
        \vec{e_1}=\begin{pmatrix} 1 & 0 & 0\end{pmatrix}
                """)
        tex2 = MathTex(r"""
                \vec{e_2}=\begin{pmatrix} 0 & 1 & 0\end{pmatrix}
                        """)
        tex3 = MathTex(r"""
                \vec{e_3}=\begin{pmatrix} 0 & 0 & 1\end{pmatrix}
                        """)

        tex1.to_corner(UR)
        tex2.next_to(tex1,DOWN)
        tex3.next_to(tex2,DOWN)
        tex1.fix_in_frame()
        tex2.fix_in_frame()
        tex3.fix_in_frame()
        self.play(Write(tex1))
        self.play(Write(tex2))
        self.play(Write(tex3))
        self.wait(4)



class ThreeDRotationVector_z(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=35 * DEGREES)

        axes = ThreeDAxes(include_numbers=False,  axis_config={"include_ticks": False}, x_range=[-4, 4, 1], y_range=[-4, 4, 1], z_range=[-3, 3, 1], x_length=8,
                          y_length=8, z_length=6)
        axes.add(axes.get_axis_labels())

        # 创建基向量
        e1 = Vector([2,0,0], color=GRAY_A,stroke_width=1.5,tip_shape=ArrowTriangleFilledTipSmall)
        e2 = Vector([0,2,0], color=GRAY_A,stroke_width=1.5,tip_shape=ArrowTriangleFilledTipSmall)
        e3 = Vector([0,0,2], color=GRAY_A,stroke_width=1.5,tip_shape=ArrowTriangleFilledTipSmall)


        # 添加标签
        e1_label = MathTex("e_1").next_to(e1, UP+RIGHT, buff=0).scale(0.5).set_color(GRAY_A)
        e2_label = MathTex("e_2").next_to(e2, LEFT+UP, buff=0).scale(0.5).set_color(GRAY_A)
        e3_label = MathTex("e_3").next_to(e3, OUT, buff=0).scale(0.5).set_color(GRAY_A)



        self.add(axes)
        self.play(Create(e1),Create(e2),Create(e3))
        self.add(e1, e1_label, e2, e2_label, e3,e3_label)

        self.wait()


        e1_p_label = MathTex("e_1'").next_to(e1, UP + RIGHT, buff=0).scale(0.5).set_color(GRAY_A)
        e2_p_label = MathTex("e_2'").next_to(e2, LEFT + UP, buff=0).scale(0.5).set_color(GRAY_A)
        e3_p_label = MathTex("e_3'").next_to(e3, OUT, buff=0).scale(0.5).set_color(GRAY_A)
        vector_group=Group()
        vector_group.add(e1, e1_p_label, e2, e2_p_label, e3,e3_p_label)

        self.wait(2)

        circle = Circle(radius=2, color=BLUE)

        self.play(Create(circle))


        self.move_camera(theta=0 * DEGREES, phi=0 * DEGREES, run_time=1)

        axes2 = ThreeDAxes(include_numbers=False, axis_config={"include_ticks": False}, x_range=[-4, 4, 1],
                          y_range=[-4, 4, 1], z_range=[-3, 3, 1], x_length=8,
                          y_length=8, z_length=6)
        axes2.set_color(BLUE)
        axes2.add(axes2.get_axis_labels(x_label="x'",y_label="y'",z_label="z'"))
        axes2.set_color(BLUE)
        self.add(axes2)
        vector_group2 = vector_group.copy().set_color(BLUE_B)
        self.add(vector_group2)

        self.wait()
        theta=30*DEGREES
        matrix_z = np.array([
            [np.cos(theta), -np.sin(theta), 0],
            [np.sin(theta), np.cos(theta), 0],
            [0, 0, 1]
        ])


        start_rad = 30 * DEGREES
        end_rad = 90 * DEGREES

        start_point = circle.point_at_angle(start_rad)

        # start_vector = Vector(start_point, color=BLUE,stroke_width=1)
        start_arc = Arc(radius=0.7, start_angle=0, angle=start_rad, color=YELLOW)
        start_arc_label = MathTex(r"\theta", color=YELLOW).scale(0.7).next_to(start_arc, RIGHT, buff=0.15)

        end_arc = Arc(radius=0.7, start_angle=end_rad, angle=start_rad, color=YELLOW)
        end_arc_label = MathTex(r"\theta", color=YELLOW).scale(0.7).next_to(end_arc, UP, buff=0.15)

        self.play(
            ApplyMethod(axes2.apply_matrix, matrix_z),
                  ApplyMethod(vector_group2.apply_matrix, matrix_z),
                  Create(start_arc), Create(end_arc))

        self.add(circle, start_arc,start_arc_label,end_arc_label)

        start_lines = axes.get_lines_to_point(start_point)
        start_lines.set_color(YELLOW)
        self.play(Create(start_lines))

        end_point = circle.point_at_angle(end_rad + start_rad)
        end_lines = axes.get_lines_to_point(end_point)
        end_lines.set_color(YELLOW)
        self.play(Create(end_lines))

        self.wait()

        self.move_camera(theta=0 * DEGREES, phi=0 * DEGREES,run_time=1)

        self.move_camera(phi=55 * DEGREES, theta=35 * DEGREES)

        return

        matrix_y= np.array([
            [0,0,1],
            [1,0,0],
            [0,1,0]
        ])


        self.play(ApplyMethod(axes.apply_matrix,matrix_y),ApplyMethod(axes2.apply_matrix,matrix_y))
        self.move_camera(theta=0 * DEGREES, phi=0 * DEGREES)
        self.move_camera(phi=55 * DEGREES, theta=35 * DEGREES)
        self.wait()


        self.play(ApplyMethod(axes.apply_matrix, matrix_y),ApplyMethod(axes2.apply_matrix,matrix_y))
        self.move_camera(theta=0 * DEGREES, phi=0 * DEGREES)
        self.move_camera(phi=55 * DEGREES, theta=35 * DEGREES)
        self.wait()


        self.play(ApplyMethod(axes.apply_matrix, matrix_y),ApplyMethod(axes2.apply_matrix,matrix_y))
        self.move_camera(theta=0 * DEGREES, phi=0 * DEGREES)
        self.move_camera(phi=55 * DEGREES, theta=35 * DEGREES)
        self.wait()


class ThreeDRotationVector_y(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=35 * DEGREES)

        axes = ThreeDAxes(include_numbers=False,  axis_config={"include_ticks": False}, x_range=[-4, 4, 1], y_range=[-4, 4, 1], z_range=[-3, 3, 1], x_length=8,
                          y_length=8, z_length=6)
        axes.add(axes.get_axis_labels(x_label="Z",y_label="X",z_label="Y"))

        # 创建基向量
        e1 = Vector([2,0,0], color=GRAY_A,stroke_width=1.5,tip_shape=ArrowTriangleFilledTipSmall)
        e2 = Vector([0,2,0], color=GRAY_A,stroke_width=1.5,tip_shape=ArrowTriangleFilledTipSmall)
        e3 = Vector([0,0,2], color=GRAY_A,stroke_width=1.5,tip_shape=ArrowTriangleFilledTipSmall)

        # 添加标签
        e1_label = MathTex("e_3").next_to(e1, UP+RIGHT, buff=0).scale(0.5).set_color(GRAY_A)
        e2_label = MathTex("e_1").next_to(e2, LEFT+UP, buff=0).scale(0.5).set_color(GRAY_A)
        e3_label = MathTex("e_2").next_to(e3, OUT, buff=0).scale(0.5).set_color(GRAY_A)



        self.add(axes)
        self.play(Create(e1),Create(e2),Create(e3))
        self.add(e1, e1_label, e2, e2_label, e3,e3_label)

        self.wait()


        e1_p_label = MathTex("e_3'").next_to(e1, UP + RIGHT, buff=0).scale(0.5).set_color(GRAY_A)
        e2_p_label = MathTex("e_1'").next_to(e2, LEFT + UP, buff=0).scale(0.5).set_color(GRAY_A)
        e3_p_label = MathTex("e_2'").next_to(e3, OUT, buff=0).scale(0.5).set_color(GRAY_A)
        vector_group=Group()
        vector_group.add(e1, e1_p_label, e2, e2_p_label, e3,e3_p_label)

        self.wait(1)

        circle = Circle(radius=2, color=BLUE)

        self.play(Create(circle))


        self.move_camera(theta=0 * DEGREES, phi=0 * DEGREES, run_time=1)

        axes2 = ThreeDAxes(include_numbers=False, axis_config={"include_ticks": False}, x_range=[-4, 4, 1],
                          y_range=[-4, 4, 1], z_range=[-3, 3, 1], x_length=8,
                          y_length=8, z_length=6)
        axes2.set_color(BLUE)
        axes2.add(axes2.get_axis_labels(x_label="Z'",y_label="X'",z_label="Y'"))
        axes2.set_color(BLUE)
        self.add(axes2)
        vector_group2 = vector_group.copy().set_color(BLUE_B)
        self.add(vector_group2)

        self.wait()
        theta=30*DEGREES
        matrix_z = np.array([
            [np.cos(theta), -np.sin(theta), 0],
            [np.sin(theta), np.cos(theta), 0],
            [0, 0, 1]
        ])


        start_rad = 30 * DEGREES
        end_rad = 90 * DEGREES

        start_point = circle.point_at_angle(start_rad)

        # start_vector = Vector(start_point, color=BLUE,stroke_width=1)
        start_arc = Arc(radius=0.7, start_angle=0, angle=start_rad, color=YELLOW)
        start_arc_label = MathTex(r"\theta", color=YELLOW).scale(0.7).next_to(start_arc, RIGHT, buff=0.15)

        end_arc = Arc(radius=0.7, start_angle=end_rad, angle=start_rad, color=YELLOW)
        end_arc_label = MathTex(r"\theta", color=YELLOW).scale(0.7).next_to(end_arc, UP, buff=0.15)

        self.play(
            ApplyMethod(axes2.apply_matrix, matrix_z),
                  ApplyMethod(vector_group2.apply_matrix, matrix_z),
                  Create(start_arc), Create(end_arc))

        self.add(circle, start_arc,start_arc_label,end_arc_label)

        start_lines = axes.get_lines_to_point(start_point)
        start_lines.set_color(YELLOW)
        self.play(Create(start_lines))

        end_point = circle.point_at_angle(end_rad + start_rad)
        end_lines = axes.get_lines_to_point(end_point)
        end_lines.set_color(YELLOW)
        self.play(Create(end_lines))

        self.wait()

        self.move_camera(theta=0 * DEGREES, phi=0 * DEGREES,run_time=1)

        self.move_camera(phi=55 * DEGREES, theta=35 * DEGREES)

        return


class ThreeDRotationVector_x(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=35 * DEGREES)

        axes = ThreeDAxes(include_numbers=False,  axis_config={"include_ticks": False}, x_range=[-4, 4, 1], y_range=[-4, 4, 1], z_range=[-3, 3, 1], x_length=8,
                          y_length=8, z_length=6)
        axes.add(axes.get_axis_labels(x_label="Y",y_label="Z",z_label="X"))

        # 创建基向量
        e1 = Vector([2,0,0], color=GRAY_A,stroke_width=1.5,tip_shape=ArrowTriangleFilledTipSmall)
        e2 = Vector([0,2,0], color=GRAY_A,stroke_width=1.5,tip_shape=ArrowTriangleFilledTipSmall)
        e3 = Vector([0,0,2], color=GRAY_A,stroke_width=1.5,tip_shape=ArrowTriangleFilledTipSmall)

        # 添加标签
        e1_label = MathTex("e_2").next_to(e1, UP+RIGHT, buff=0).scale(0.5).set_color(GRAY_A)
        e2_label = MathTex("e_3").next_to(e2, LEFT+UP, buff=0).scale(0.5).set_color(GRAY_A)
        e3_label = MathTex("e_1").next_to(e3, OUT, buff=0).scale(0.5).set_color(GRAY_A)



        self.add(axes)
        self.play(Create(e1),Create(e2),Create(e3))
        self.add(e1, e1_label, e2, e2_label, e3,e3_label)

        self.wait()


        e1_p_label = MathTex("e_2'").next_to(e1, UP + RIGHT, buff=0).scale(0.5).set_color(GRAY_A)
        e2_p_label = MathTex("e_3'").next_to(e2, LEFT + UP, buff=0).scale(0.5).set_color(GRAY_A)
        e3_p_label = MathTex("e_1'").next_to(e3, OUT, buff=0).scale(0.5).set_color(GRAY_A)
        vector_group=Group()
        vector_group.add(e1, e1_p_label, e2, e2_p_label, e3,e3_p_label)

        self.wait(1)

        circle = Circle(radius=2, color=BLUE)

        self.play(Create(circle))


        self.move_camera(theta=0 * DEGREES, phi=0 * DEGREES, run_time=1)

        axes2 = ThreeDAxes(include_numbers=False, axis_config={"include_ticks": False}, x_range=[-4, 4, 1],
                          y_range=[-4, 4, 1], z_range=[-3, 3, 1], x_length=8,
                          y_length=8, z_length=6)
        axes2.set_color(BLUE)
        axes2.add(axes2.get_axis_labels(x_label="Y'",y_label="Z'",z_label="X'"))
        axes2.set_color(BLUE)
        self.add(axes2)
        vector_group2 = vector_group.copy().set_color(BLUE_B)
        self.add(vector_group2)

        self.wait()
        theta=30*DEGREES
        matrix_z = np.array([
            [np.cos(theta), -np.sin(theta), 0],
            [np.sin(theta), np.cos(theta), 0],
            [0, 0, 1]
        ])


        start_rad = 30 * DEGREES
        end_rad = 90 * DEGREES

        start_point = circle.point_at_angle(start_rad)

        # start_vector = Vector(start_point, color=BLUE,stroke_width=1)
        start_arc = Arc(radius=0.7, start_angle=0, angle=start_rad, color=YELLOW)
        start_arc_label = MathTex(r"\theta", color=YELLOW).scale(0.7).next_to(start_arc, RIGHT, buff=0.15)

        end_arc = Arc(radius=0.7, start_angle=end_rad, angle=start_rad, color=YELLOW)
        end_arc_label = MathTex(r"\theta", color=YELLOW).scale(0.7).next_to(end_arc, UP, buff=0.15)

        self.play(
            ApplyMethod(axes2.apply_matrix, matrix_z),
                  ApplyMethod(vector_group2.apply_matrix, matrix_z),
                  Create(start_arc), Create(end_arc))

        self.add(circle, start_arc,start_arc_label,end_arc_label)

        start_lines = axes.get_lines_to_point(start_point)
        start_lines.set_color(YELLOW)
        self.play(Create(start_lines))

        end_point = circle.point_at_angle(end_rad + start_rad)
        end_lines = axes.get_lines_to_point(end_point)
        end_lines.set_color(YELLOW)
        self.play(Create(end_lines))

        self.wait()

        self.move_camera(theta=0 * DEGREES, phi=0 * DEGREES,run_time=1)

        self.move_camera(phi=55 * DEGREES, theta=35 * DEGREES)

        return

class ThreeDRotationVector_z_Latex(ThreeDScene):
    def construct(self):

        self.next_section(skip_animations=True,name="1")
        self.set_camera_orientation(phi=70 * DEGREES, theta=35 * DEGREES)


        axes = ThreeDAxes(include_numbers=False,  axis_config={"include_ticks": False}, x_range=[-4, 4, 1], y_range=[-4, 4, 1], z_range=[-3, 3, 1], x_length=8,
                          y_length=8, z_length=6)
        axes.add(axes.get_axis_labels())

        # 创建基向量
        e1 = Vector([2,0,0], color=GRAY_A,stroke_width=1.5,tip_shape=ArrowTriangleFilledTipSmall)
        e2 = Vector([0,2,0], color=GRAY_A,stroke_width=1.5,tip_shape=ArrowTriangleFilledTipSmall)
        e3 = Vector([0,0,2], color=GRAY_A,stroke_width=1.5,tip_shape=ArrowTriangleFilledTipSmall)


        # 添加标签
        e1_label = MathTex("e_1").next_to(e1, UP+RIGHT, buff=0).scale(0.5).set_color(GRAY_A)
        e2_label = MathTex("e_2").next_to(e2, LEFT+UP, buff=0).scale(0.5).set_color(GRAY_A)
        e3_label = MathTex("e_3").next_to(e3, OUT, buff=0).scale(0.5).set_color(GRAY_A)



        self.add(axes)
        self.play(Create(e1),Create(e2),Create(e3))
        self.add(e1, e1_label, e2, e2_label, e3,e3_label)

        self.wait()


        e1_p_label = MathTex("e_1'").next_to(e1, UP + RIGHT, buff=0).scale(0.5).set_color(GRAY_A)
        e2_p_label = MathTex("e_2'").next_to(e2, LEFT + UP, buff=0).scale(0.5).set_color(GRAY_A)
        e3_p_label = MathTex("e_3'").next_to(e3, OUT, buff=0).scale(0.5).set_color(GRAY_A)
        vector_group=Group()
        vector_group.add(e1, e1_p_label, e2, e2_p_label, e3,e3_p_label)

        self.wait(2)

        circle = Circle(radius=2, color=BLUE)

        self.play(Create(circle))


        self.move_camera(theta=0 * DEGREES, phi=0 * DEGREES, run_time=1)

        axes2 = ThreeDAxes(include_numbers=False, axis_config={"include_ticks": False}, x_range=[-4, 4, 1],
                          y_range=[-4, 4, 1], z_range=[-3, 3, 1], x_length=8,
                          y_length=8, z_length=6)
        axes2.set_color(BLUE)
        axes2.add(axes2.get_axis_labels(x_label="x'",y_label="y'",z_label="z'"))
        axes2.set_color(BLUE)
        self.add(axes2)
        vector_group2 = vector_group.copy().set_color(BLUE_B)
        self.add(vector_group2)

        self.wait()
        theta=30*DEGREES
        matrix_z = np.array([
            [np.cos(theta), -np.sin(theta), 0],
            [np.sin(theta), np.cos(theta), 0],
            [0, 0, 1]
        ])


        start_rad = 30 * DEGREES
        end_rad = 90 * DEGREES

        start_point = circle.point_at_angle(start_rad)

        # start_vector = Vector(start_point, color=BLUE,stroke_width=1)
        start_arc = Arc(radius=0.7, start_angle=0, angle=start_rad, color=YELLOW)
        start_arc_label = MathTex(r"\theta", color=YELLOW).scale(0.7).next_to(start_arc, RIGHT, buff=0.15)

        end_arc = Arc(radius=0.7, start_angle=end_rad, angle=start_rad, color=YELLOW)
        end_arc_label = MathTex(r"\theta", color=YELLOW).scale(0.7).next_to(end_arc, UP, buff=0.15)

        self.play(
            ApplyMethod(axes2.apply_matrix, matrix_z),
                  ApplyMethod(vector_group2.apply_matrix, matrix_z),
                  Create(start_arc), Create(end_arc))

        self.add(circle, start_arc,start_arc_label,end_arc_label)

        start_lines = axes.get_lines_to_point(start_point)
        start_lines.set_color(YELLOW)
        self.play(Create(start_lines))

        end_point = circle.point_at_angle(end_rad + start_rad)
        end_lines = axes.get_lines_to_point(end_point)
        end_lines.set_color(YELLOW)
        self.play(Create(end_lines))

        self.move_camera(theta=0 * DEGREES, phi=0 * DEGREES, run_time=1)

        self.next_section(name="texts",skip_animations=False)

        self.move_camera(frame_center=[5, 0, 0])

        self.wait()

        tex1 = MathTex(r"""
             \vec{e_1}=\begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}
             \vec{e_2}=\begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}
             \vec{e_3}=\begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}
                     """)
        tex1.shift(np.array([6.5, 3, 0])).scale(0.6)
        self.play(Write(tex1))

        tex2 = MathTex(r"""
                               \vec{e_1}'=\begin{bmatrix} \cos(\theta) \\  \sin(\theta) \\ 0\end{bmatrix}
                               \vec{e_2}'=\begin{bmatrix} -\sin(\theta) \\ \cos(\theta) \\ 0\end{bmatrix}
                               \vec{e_3}'=\begin{bmatrix} 0\\ 0 \\ 1\end{bmatrix}
                              """)
        tex2.shift(np.array([7.3, 1.5, 0])).scale(0.6).set_color(BLUE)
        self.play(Write(tex2))

        matrix = Matrix([
            [r"\cos\theta", r"-\sin\theta", 0],
            [r"\sin\theta", r"\cos\theta", 0],
            [0, 0, 1]
        ], h_buff=1.7).scale(0.6)

        matrix.shift(np.array([7.6, -0.5, 0]))

        columns0 = SurroundingRectangle(matrix.get_columns()[0], stroke_width=1).set_color(BLUE)
        matrix.add(columns0)
        columns0_labes = MathTex(r"e_1'").next_to(columns0, DOWN).scale(0.6).set_color(BLUE)

        columns1 = SurroundingRectangle(matrix.get_columns()[1], stroke_width=1).set_color(BLUE)
        matrix.add(columns1)
        columns1_labes = MathTex(r"e_2'").next_to(columns1, DOWN).scale(0.6).set_color(BLUE)

        columns2 = SurroundingRectangle(matrix.get_columns()[2], stroke_width=1).set_color(BLUE)
        matrix.add(columns2)
        columns2_labes = MathTex(r"e_3'").next_to(columns2, DOWN).scale(0.6).set_color(BLUE)

        rz = MathTex(r"R_z=")
        rz.next_to(matrix,LEFT)
        self.play(Write(rz))
        self.play(Write(matrix))
        self.play(Write(columns0_labes), Write(columns1_labes), Write(columns2_labes))

class ThreeDRotationVector_y_Latex(ThreeDScene):
    def construct(self):

        self.next_section(skip_animations=True,name="1")
        self.set_camera_orientation(phi=70 * DEGREES, theta=35 * DEGREES)


        axes = ThreeDAxes(include_numbers=False,  axis_config={"include_ticks": False}, x_range=[-4, 4, 1], y_range=[-4, 4, 1], z_range=[-3, 3, 1], x_length=8,
                          y_length=8, z_length=6)
        axes.add(axes.get_axis_labels(x_label="Z",y_label="X",z_label="Y"))

        # 创建基向量
        e1 = Vector([2,0,0], color=GRAY_A,stroke_width=1.5,tip_shape=ArrowTriangleFilledTipSmall)
        e2 = Vector([0,2,0], color=GRAY_A,stroke_width=1.5,tip_shape=ArrowTriangleFilledTipSmall)
        e3 = Vector([0,0,2], color=GRAY_A,stroke_width=1.5,tip_shape=ArrowTriangleFilledTipSmall)


        # 添加标签
        e1_label = MathTex("e_3").next_to(e1, UP+RIGHT, buff=0).scale(0.5).set_color(GRAY_A)
        e2_label = MathTex("e_1").next_to(e2, LEFT+UP, buff=0).scale(0.5).set_color(GRAY_A)
        e3_label = MathTex("e_2").next_to(e3, OUT, buff=0).scale(0.5).set_color(GRAY_A)



        self.add(axes)
        # self.play(Create(e1),Create(e2),Create(e3))
        self.add(e1, e1_label, e2, e2_label, e3,e3_label)

        # self.wait()


        e1_p_label = MathTex("e_3'").next_to(e1, UP + RIGHT, buff=0).scale(0.5).set_color(GRAY_A)
        e2_p_label = MathTex("e_1'").next_to(e2, LEFT + UP, buff=0).scale(0.5).set_color(GRAY_A)
        e3_p_label = MathTex("e_2'").next_to(e3, OUT, buff=0).scale(0.5).set_color(GRAY_A)
        vector_group=Group()
        vector_group.add(e1, e1_p_label, e2, e2_p_label, e3,e3_p_label)

        # self.wait(2)

        circle = Circle(radius=2, color=BLUE)


        self.add(circle)
        # self.play(Create(circle))


        self.move_camera(theta=0 * DEGREES, phi=0 * DEGREES, run_time=1)

        axes2 = ThreeDAxes(include_numbers=False, axis_config={"include_ticks": False}, x_range=[-4, 4, 1],
                          y_range=[-4, 4, 1], z_range=[-3, 3, 1], x_length=8,
                          y_length=8, z_length=6)
        axes2.set_color(BLUE)
        axes2.add(axes2.get_axis_labels(x_label="Z'",y_label="X'",z_label="Y'"))
        axes2.set_color(BLUE)
        self.add(axes2)
        vector_group2 = vector_group.copy().set_color(BLUE_B)
        self.add(vector_group2)

        # self.wait()
        theta=30*DEGREES
        matrix_z = np.array([
            [np.cos(theta), -np.sin(theta), 0],
            [np.sin(theta), np.cos(theta), 0],
            [0, 0, 1]
        ])


        start_rad = 30 * DEGREES
        end_rad = 90 * DEGREES

        start_point = circle.point_at_angle(start_rad)

        # start_vector = Vector(start_point, color=BLUE,stroke_width=1)
        start_arc = Arc(radius=0.7, start_angle=0, angle=start_rad, color=YELLOW)
        start_arc_label = MathTex(r"\theta", color=YELLOW).scale(0.7).next_to(start_arc, RIGHT, buff=0.15)

        end_arc = Arc(radius=0.7, start_angle=end_rad, angle=start_rad, color=YELLOW)
        end_arc_label = MathTex(r"\theta", color=YELLOW).scale(0.7).next_to(end_arc, UP, buff=0.15)

        self.play(
            ApplyMethod(axes2.apply_matrix, matrix_z),
                  ApplyMethod(vector_group2.apply_matrix, matrix_z),
                  Create(start_arc), Create(end_arc),run_time=0.1)

        self.add(circle, start_arc,start_arc_label,end_arc_label)

        start_lines = axes.get_lines_to_point(start_point)
        start_lines.set_color(YELLOW)
        self.add(start_lines)

        end_point = circle.point_at_angle(end_rad + start_rad)
        end_lines = axes.get_lines_to_point(end_point)
        end_lines.set_color(YELLOW)
        self.add(end_lines)

        self.move_camera(theta=0 * DEGREES, phi=0 * DEGREES, run_time=0.1)

        self.next_section(name="texts",skip_animations=False)

        self.move_camera(frame_center=[5, 0, 0])

        self.wait()

        tex1 = MathTex(r"""
             \vec{e_1}=\begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}
             \vec{e_2}=\begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}
             \vec{e_3}=\begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}
                     """)
        tex1.shift(np.array([6.5, 3, 0])).scale(0.6)
        self.play(Write(tex1))

        tex2 = MathTex(r"""
                               \vec{e_1}'=\begin{bmatrix} cos(\theta) \\ 0 \\ -sin(\theta) \end{bmatrix}
                               \vec{e_2}'=\begin{bmatrix} 0 \\ 1 \\ 0  \end{bmatrix}
                               \vec{e_3}'=\begin{bmatrix} sin(\theta) \\ 0 \\ cos(\theta) \end{bmatrix}
                              """)
        tex2.shift(np.array([7.3, 1.5, 0])).scale(0.6).set_color(BLUE)
        self.play(Write(tex2))

        matrix = Matrix([
            [r"\cos\theta",0, r"\sin\theta"],
            [0, 1, 0],
            [r"-\sin\theta",  0,r"\cos\theta"],
        ], h_buff=1.7).scale(0.6)

        matrix.shift(np.array([7.6, -0.5, 0]))

        columns0 = SurroundingRectangle(matrix.get_columns()[0], stroke_width=1).set_color(BLUE)
        matrix.add(columns0)
        columns0_labes = MathTex(r"e_1'").next_to(columns0, DOWN).scale(0.6).set_color(BLUE)

        columns1 = SurroundingRectangle(matrix.get_columns()[1], stroke_width=1).set_color(BLUE)
        matrix.add(columns1)
        columns1_labes = MathTex(r"e_2'").next_to(columns1, DOWN).scale(0.6).set_color(BLUE)

        columns2 = SurroundingRectangle(matrix.get_columns()[2], stroke_width=1).set_color(BLUE)
        matrix.add(columns2)
        columns2_labes = MathTex(r"e_3'").next_to(columns2, DOWN).scale(0.6).set_color(BLUE)

        rz = MathTex(r"R_y=")
        rz.next_to(matrix,LEFT)
        self.play(Write(rz))
        self.play(Write(matrix))
        self.play(Write(columns0_labes), Write(columns1_labes), Write(columns2_labes))

class ThreeDRotationVector_x_Latex(ThreeDScene):
    def construct(self):

        self.next_section(skip_animations=True,name="1")
        self.set_camera_orientation(phi=70 * DEGREES, theta=35 * DEGREES)


        axes = ThreeDAxes(include_numbers=False,  axis_config={"include_ticks": False}, x_range=[-4, 4, 1], y_range=[-4, 4, 1], z_range=[-3, 3, 1], x_length=8,
                          y_length=8, z_length=6)
        axes.add(axes.get_axis_labels(x_label="Y",y_label="Z",z_label="X"))

        # 创建基向量
        e1 = Vector([2,0,0], color=GRAY_A,stroke_width=1.5,tip_shape=ArrowTriangleFilledTipSmall)
        e2 = Vector([0,2,0], color=GRAY_A,stroke_width=1.5,tip_shape=ArrowTriangleFilledTipSmall)
        e3 = Vector([0,0,2], color=GRAY_A,stroke_width=1.5,tip_shape=ArrowTriangleFilledTipSmall)


        # 添加标签
        e1_label = MathTex("e_2").next_to(e1, UP+RIGHT, buff=0).scale(0.5).set_color(GRAY_A)
        e2_label = MathTex("e_3").next_to(e2, LEFT+UP, buff=0).scale(0.5).set_color(GRAY_A)
        e3_label = MathTex("e_1").next_to(e3, OUT, buff=0).scale(0.5).set_color(GRAY_A)



        self.add(axes)
        # self.play(Create(e1),Create(e2),Create(e3))
        self.add(e1, e1_label, e2, e2_label, e3,e3_label)

        # self.wait()


        e1_p_label = MathTex("e_2'").next_to(e1, UP + RIGHT, buff=0).scale(0.5).set_color(GRAY_A)
        e2_p_label = MathTex("e_3'").next_to(e2, LEFT + UP, buff=0).scale(0.5).set_color(GRAY_A)
        e3_p_label = MathTex("e_1'").next_to(e3, OUT, buff=0).scale(0.5).set_color(GRAY_A)
        vector_group=Group()
        vector_group.add(e1, e1_p_label, e2, e2_p_label, e3,e3_p_label)

        # self.wait(2)

        circle = Circle(radius=2, color=BLUE)


        self.add(circle)
        # self.play(Create(circle))


        self.move_camera(theta=0 * DEGREES, phi=0 * DEGREES, run_time=1)

        axes2 = ThreeDAxes(include_numbers=False, axis_config={"include_ticks": False}, x_range=[-4, 4, 1],
                          y_range=[-4, 4, 1], z_range=[-3, 3, 1], x_length=8,
                          y_length=8, z_length=6)
        axes2.set_color(BLUE)
        axes2.add(axes2.get_axis_labels(x_label="Y'",y_label="Z'",z_label="X'"))
        axes2.set_color(BLUE)
        self.add(axes2)
        vector_group2 = vector_group.copy().set_color(BLUE_B)
        self.add(vector_group2)

        # self.wait()
        theta=30*DEGREES
        matrix_z = np.array([
            [np.cos(theta), -np.sin(theta), 0],
            [np.sin(theta), np.cos(theta), 0],
            [0, 0, 1]
        ])


        start_rad = 30 * DEGREES
        end_rad = 90 * DEGREES

        start_point = circle.point_at_angle(start_rad)

        # start_vector = Vector(start_point, color=BLUE,stroke_width=1)
        start_arc = Arc(radius=0.7, start_angle=0, angle=start_rad, color=YELLOW)
        start_arc_label = MathTex(r"\theta", color=YELLOW).scale(0.7).next_to(start_arc, RIGHT, buff=0.15)

        end_arc = Arc(radius=0.7, start_angle=end_rad, angle=start_rad, color=YELLOW)
        end_arc_label = MathTex(r"\theta", color=YELLOW).scale(0.7).next_to(end_arc, UP, buff=0.15)

        self.play(
            ApplyMethod(axes2.apply_matrix, matrix_z),
                  ApplyMethod(vector_group2.apply_matrix, matrix_z),
                  Create(start_arc), Create(end_arc),run_time=0.1)

        self.add(circle, start_arc,start_arc_label,end_arc_label)

        start_lines = axes.get_lines_to_point(start_point)
        start_lines.set_color(YELLOW)
        self.add(start_lines)

        end_point = circle.point_at_angle(end_rad + start_rad)
        end_lines = axes.get_lines_to_point(end_point)
        end_lines.set_color(YELLOW)
        self.add(end_lines)

        self.move_camera(theta=0 * DEGREES, phi=0 * DEGREES, run_time=0.1)

        self.next_section(name="texts",skip_animations=False)

        self.move_camera(frame_center=[5, 0, 0])

        self.wait()

        tex1 = MathTex(r"""
             \vec{e_1}=\begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}
             \vec{e_2}=\begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}
             \vec{e_3}=\begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}
                     """)
        tex1.shift(np.array([6.5, 3, 0])).scale(0.6)
        self.play(Write(tex1))

        tex2 = MathTex(r"""
                               \vec{e_1}'=\begin{bmatrix} 1 \\ 0 \\ 0  \end{bmatrix}
                               \vec{e_2}'=\begin{bmatrix} 0 \\ cos(\theta) \\  sin(\theta) \end{bmatrix}
                               \vec{e_3}'=\begin{bmatrix} 0 \\ -sin(\theta) \\ cos(\theta) \end{bmatrix}
                              """)
        tex2.shift(np.array([7.3, 1.5, 0])).scale(0.6).set_color(BLUE)
        self.play(Write(tex2))

        matrix = Matrix([
            [1, 0, 0],
            [0,r"\cos\theta", r"-\sin\theta"],
            [ 0, r"\sin\theta", r"\cos\theta"],
        ], h_buff=1.7).scale(0.6)

        matrix.shift(np.array([7.6, -0.5, 0]))

        columns0 = SurroundingRectangle(matrix.get_columns()[0], stroke_width=1).set_color(BLUE)
        matrix.add(columns0)
        columns0_labes = MathTex(r"e_1'").next_to(columns0, DOWN).scale(0.6).set_color(BLUE)

        columns1 = SurroundingRectangle(matrix.get_columns()[1], stroke_width=1).set_color(BLUE)
        matrix.add(columns1)
        columns1_labes = MathTex(r"e_2'").next_to(columns1, DOWN).scale(0.6).set_color(BLUE)

        columns2 = SurroundingRectangle(matrix.get_columns()[2], stroke_width=1).set_color(BLUE)
        matrix.add(columns2)
        columns2_labes = MathTex(r"e_3'").next_to(columns2, DOWN).scale(0.6).set_color(BLUE)

        rz = MathTex(r"R_x=")
        rz.next_to(matrix,LEFT)
        self.play(Write(rz))
        self.play(Write(matrix))
        self.play(Write(columns0_labes), Write(columns1_labes), Write(columns2_labes))




with tempconfig({"preview": True, "disable_caching": False, "renderer": "opengl"}):
    ThreeDRotationVector_base_vector().render()
    exit(1)