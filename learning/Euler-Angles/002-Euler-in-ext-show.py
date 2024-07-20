
from manim import *
from manim.mobject.geometry.tips import ArrowTriangleFilledTipSmall

from manim.mobject.opengl.opengl_something import OpenGLCone, OpenGLLine3D, OpenGLArrow3D
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface, OpenGLSurface
import numpy as np



class IN_EXT_Tittle(ThreeDScene):
    def construct(self):

        title=Title("旋转顺序 Z-Y-X",tex_template=TexTemplateLibrary.ctex)
        self.play(FadeIn(title.scale(1.5)))

        text_in = Text("内旋")
        matrix_int = MathTex(r"R_{in}=R_zR_yR_x")

        text_ext = Text("外旋")
        matrix_ext = MathTex(r"R_{ext}=R_xR_yR_z")

        group_ext=VGroup(text_ext,matrix_ext).arrange(direction=RIGHT)
        group_in = VGroup(text_in, matrix_int).arrange(direction=RIGHT)

        group= VGroup(group_ext,group_in).arrange(direction=DOWN)
        self.play(FadeIn(group.scale(2)))
        self.wait()

class Euler_zxy_in_vector(ThreeDScene):
    def init_label (self,point):
        x,y,z=point
        self.num_x = DecimalNumber(number=x)
        self.num_y = DecimalNumber(number=y)
        self.num_z = DecimalNumber(number=z)

        self.tracker_x = ValueTracker(x)
        self.tracker_y = ValueTracker(y)
        self.tracker_z = ValueTracker(z)

        self.num_x.add_updater(lambda m: m.set_value(self.tracker_x.get_value()))
        self.num_y.add_updater(lambda m: m.set_value(self.tracker_y.get_value()))
        self.num_z.add_updater(lambda m: m.set_value(self.tracker_z.get_value()))

    def get_label_animate(self,point):
        animate_x= self.tracker_x.animate.set_value(10)
        animate_y = self.tracker_y.animate.set_value(10)
        animate_z = self.tracker_z.animate.set_value(10)
        return animate_x,animate_y,animate_z


    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=115 * DEGREES)

        axis_config = {
            # "include_tip": False,
            "numbers_to_include": None,
            "include_ticks": False,
        }
        axes = ThreeDAxes(include_numbers=False,
                          x_range=[0, 3, 1],
                          y_range=[0, 3, 1],
                          z_range=[0, 3, 1],
                          x_length=3, y_length=3, z_length=3,
                          axis_config=axis_config,)

        axes.add(axes.get_axis_labels())
        axes.set_color(BLUE_C)
        axes.shift(ORIGIN - axes.c2p(0, 0, 0))
        self.play(Create(axes))
        zRad = 30 * DEGREES
        yRad = -45 * DEGREES
        xRad = 60 * DEGREES
        Rz = np.array([
            [np.cos(zRad), -np.sin(zRad), 0],
            [np.sin(zRad), np.cos(zRad), 0],
            [0, 0, 1]
        ]);
        Ry = np.array([
            [np.cos(yRad), 0, np.sin(yRad)],
            [0, 1, 0],
            [-np.sin(yRad), 0, np.cos(yRad)]
        ]);
        Rx = np.array([
            [1, 0, 0],
            [0, np.cos(xRad), -np.sin(xRad)],
            [0, np.sin(xRad), np.cos(xRad)]
        ]);

        axes1 = ThreeDAxes(include_numbers=False,
                           x_range=[0, 3, 1],
                           y_range=[0, 3, 1],
                           z_range=[0, 3, 1],
                           x_length=3, y_length=3, z_length=3,
                           axis_config=axis_config )

        axes1.shift(ORIGIN - axes1.c2p(0, 0, 0))
        circle = Circle(radius=3, color=BLUE_C, fill_opacity=0.1)
        self.play(Create(circle))
        axes1.add(axes1.get_axis_labels())
        axes1.set_color(RED).set_opacity(0.5)

        vector = OpenGLArrow3D(start=ORIGIN, end=[2, 2, 2], color=YELLOW)

        self.play(Create(axes1),Create(vector))

        # self.play(ReplacementTransform(point_label,MathTex(r"P(5,5,5)").to_corner(UL).fix_in_frame()))
        self.wait()

        # 一
        alpha_arc = Arc(start_angle=0, angle=zRad, arc_center=ORIGIN)
        alpha_arc.add_tip(tip_length=0.15, tip_width=0.15)
        alpha_labels= MathTex(r"\psi")
        alpha_labels.next_to(alpha_arc)
        alpha_labels.fix_orientation()

        animate = axes1.animate.apply_matrix(matrix=Rz)
        animate_vector = vector.animate.apply_matrix(matrix=Rz)

        self.play(animate,animate_vector,Create(alpha_arc),run_time=2)
        self.play(FadeIn(alpha_labels))
        self.wait()
        # 二

        start_point=np.array([-3.2,0,0])
        end_point=np.array([4,0,0])
        start_point= (Rz @ start_point.T).T
        end_point =  (Rz @ end_point.T).T
        arrow1 = Arrow(start=start_point, end=end_point, color=GREEN).set_opacity(0.5)
        dashed_arrow = DashedVMobject(arrow1, num_dashes=20, dashed_ratio=0.5)
        self.add(dashed_arrow)

        start_point2 = np.array([ 0,-3.2, 0])
        end_point2 = np.array([ 0,4, 0])
        start_point2 = (Rz @ start_point2.T).T
        end_point2 = (Rz @ end_point2.T).T
        arrow2 = Arrow(start=start_point2, end=end_point2, color=GREEN).set_opacity(0.5)


        beta_arc = Arc(start_angle=0, angle=-yRad, arc_center=ORIGIN)
        beta_arc.add_tip(tip_length=0.15, tip_width=0.15)
        beta_label = MathTex(r"\theta")


        beta_arc.rotate(axis=RIGHT,angle=90*DEGREES,about_point=ORIGIN)
        beta_arc.apply_matrix(matrix=Rz)
        beta_label.next_to(beta_arc, UR+OUT)
        beta_label.fix_orientation()

        animate = axes1.animate.apply_matrix(matrix=Rz @ Ry @ Rz.T)
        animate_vector = vector.animate.apply_matrix(matrix=Rz @ Ry @ Rz.T)
        self.play(animate,animate_vector,Create(beta_arc),run_time=2)
        self.play(FadeIn(beta_label))
        self.wait()


        # 第三转
        circle_red = Circle(radius=3,stroke_width=1, color=RED,fill_opacity=0.1)
        circle_red.rotate(axis=UP, angle=90 * DEGREES, about_point=ORIGIN)
        circle_red.apply_matrix(matrix=Rz@Ry)
        self.play(Create(circle_red))
        self.add(arrow2)



        gamma_arc = Arc(start_angle=90*DEGREES, angle=xRad, arc_center=ORIGIN,radius=1)
        gamma_arc.rotate(axis=UP, angle=90 * DEGREES, about_point=ORIGIN)
        gamma_arc.apply_matrix(matrix=Rz @ Ry)

        gamma_arc.add_tip(tip_length=0.15, tip_width=0.15)
        gamma_label = MathTex(r"\varphi")
        gamma_label.next_to(gamma_arc, UP)
        gamma_label.fix_orientation()


        animate = axes1.animate.apply_matrix(matrix=(Rz @ Ry) @ Rx @ (Rz @ Ry).T)
        animate_vector = vector.animate.apply_matrix(matrix=(Rz @ Ry) @ Rx @ (Rz @ Ry).T)
        self.play(animate,animate_vector,Create(gamma_arc),run_time=2)
        self.play(FadeIn(gamma_label))
        self.wait()
        # 最后
        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(14)

# 注意 绕Y 旋转的角是负 角，未了更维基百科，保持一致
class Euler_zyx_ext_vector(ThreeDScene):
    def construct(self):
        # self.set_camera_orientation(phi=60 * DEGREES, theta=45 * DEGREES)
        self.set_camera_orientation(phi=60 * DEGREES, theta=115 * DEGREES)
        axis_config = {
            # "include_tip": False,
            "numbers_to_include": None,
            "include_ticks": False,
        }
        axes = ThreeDAxes(include_numbers=False,
                          x_range=[0, 3, 1],
                          y_range=[0, 3, 1],
                          z_range=[0, 3, 1],
                          x_length=3, y_length=3, z_length=3,
                          axis_config=axis_config,)

        axes.add(axes.get_axis_labels())
        axes.set_color(BLUE_C)
        axes.shift(ORIGIN - axes.c2p(0, 0, 0))
        self.play(Create(axes))


        zRad = 30 * DEGREES
        yRad = -45 * DEGREES
        xRad= 60 * DEGREES

        Rz = np.array([
            [np.cos(zRad), -np.sin(zRad), 0],
            [np.sin(zRad), np.cos(zRad), 0],
            [0, 0, 1]
        ]);
        Ry = np.array([
            [np.cos(yRad), 0, np.sin(yRad)],
            [0, 1, 0],
            [-np.sin(yRad), 0, np.cos(yRad)]
        ]);
        Rx = np.array([
            [1, 0, 0],
            [0, np.cos(xRad), -np.sin(xRad)],
            [0, np.sin(xRad), np.cos(xRad)]
        ]);


        axes1 = ThreeDAxes(include_numbers=False,
                           x_range=[0, 3, 1],
                           y_range=[0, 3, 1],
                           z_range=[0, 3, 1],
                           x_length=3, y_length=3, z_length=3,
                           axis_config=axis_config )

        axes1.shift(ORIGIN - axes1.c2p(0, 0, 0))
        circle = Circle(radius=3, color=BLUE_C, fill_opacity=0.1)
        self.play(Create(circle))
        axes1.add(axes1.get_axis_labels())
        axes1.set_color(RED).set_opacity(0.5)

        vector_= np.array([2, 2, 2])

        vector = OpenGLArrow3D(start=ORIGIN, end=vector_, color=YELLOW)


        self.play(Create(axes1),Create(vector))


        circle_red = Circle(radius=3, color=RED,stroke_width=1, fill_opacity=0.1)
        # circle_red.rotate(axis=UP, angle=90 * DEGREES, about_point=ORIGIN)
        self.play(Create(circle_red))

        # 第三次转

        gamma_arc = Arc(start_angle=0 * DEGREES, angle=zRad, arc_center=ORIGIN, radius=1)
        gamma_arc.add_tip(tip_length=0.15, tip_width=0.15)
        # gamma_arc.rotate(axis=UP, angle=90 * DEGREES, about_point=ORIGIN)

        gamma_label = MathTex(r"\varphi")
        gamma_label.next_to(gamma_arc, RIGHT)
        gamma_label.fix_orientation()

        arrow = Arrow(start=ORIGIN, end=[4, 0, 0], stroke_width=3, color=GREEN, tip_shape=ArrowTriangleFilledTipSmall)
        dashed_arrow = DashedVMobject(arrow, num_dashes=20, dashed_ratio=0.5)
        arrow_animate = dashed_arrow.animate.apply_matrix(matrix=Rz).set_opacity(0.5)

        animate = axes1.animate.apply_matrix(matrix=Rz)
        circle_red_animate = circle_red.animate.apply_matrix(matrix=Rz)
        vector_animate = vector.animate.apply_matrix(matrix=Rz)
        self.play(animate, circle_red_animate,vector_animate, arrow_animate, Create(gamma_arc), run_time=2)

        self.play(FadeIn(gamma_label))
        self.wait()

        # 第二转

        # beta_arc = Arc(start_angle=90 * DEGREES, angle=-yRad, arc_center=ORIGIN)
        # beta_arc.add_tip(tip_length=0.15, tip_width=0.15)
        # beta_arc.rotate(axis=RIGHT, angle=90 * DEGREES, about_point=ORIGIN)
        beta_arc = Arc(start_angle=0, angle=-yRad, arc_center=ORIGIN)
        beta_arc.add_tip(tip_length=0.15, tip_width=0.15)
        beta_arc.rotate(axis=RIGHT, angle=90 * DEGREES, about_point=ORIGIN)

        beta_label = MathTex(r"\theta")
        beta_label.next_to(beta_arc, OUT)
        beta_label.fix_orientation()

        arrow = Arrow(start=ORIGIN, end=[4, 0, 0], stroke_width=3, color=GREEN, tip_shape=ArrowTriangleFilledTipSmall)
        dashed_arrow = DashedVMobject(arrow, num_dashes=20, dashed_ratio=0.5)
        animate_arrow = dashed_arrow.animate.apply_matrix(matrix=Ry).set_opacity(0.5)

        animate = axes1.animate.apply_matrix(matrix=Ry)
        animate_red = circle_red.animate.apply_matrix(matrix=Ry)
        vector_animate = vector.animate.apply_matrix(matrix=Ry)
        self.play(animate, animate_red,vector_animate, Create(beta_arc), animate_arrow, run_time=2)
        self.play(FadeIn(beta_label))
        self.wait()

        # 第一转
        alpha_arc = Arc(start_angle=90*DEGREES, angle=xRad, arc_center=ORIGIN)
        alpha_arc.add_tip(tip_length=0.15, tip_width=0.15)
        alpha_arc.rotate(axis=UP, angle=90 * DEGREES, about_point=ORIGIN)

        alpha_labels= MathTex(r"\psi")
        alpha_labels.next_to(alpha_arc)
        alpha_labels.fix_orientation()

        arrow = Arrow(start=ORIGIN, end=[0, 4, 0], stroke_width=3, color=GREEN, tip_shape=ArrowTriangleFilledTipSmall)
        dashed_arrow = DashedVMobject(arrow, num_dashes=20, dashed_ratio=0.5)
        arrow_animate=dashed_arrow.animate.apply_matrix(matrix=Rx).set_opacity(0.5)

        animate = axes1.animate.apply_matrix(matrix=Rx)
        animate_red= circle_red.animate.apply_matrix(matrix=Rx)
        vector_animate = vector.animate.apply_matrix(matrix=Rx)

        self.play(animate,animate_red,vector_animate,Create(alpha_arc),arrow_animate,run_time=2)
        self.play(FadeIn(alpha_labels))
        self.wait()

        # # 最后
        # self.begin_ambient_camera_rotation(rate=0.5)
        # self.wait(14)


class AexsMatix(ThreeDScene):
    def construct(self):
        self.move_camera(zoom=0.8)
        axes = Axes(include_numbers=False, x_range=[-4, 4, 1], y_range=[-4, 4, 1], z_range=[-4, 4, 1], x_length=8,
                    y_length=8, z_length=6)
        axes.add(axes.get_axis_labels())

        dot = Dot(point=[2, 0.5, 0])
        lable = MarkupText("P(2,0.5)").scale(0.3)
        lable.next_to(dot, RIGHT, buff=0.1)
        self.add(lable)
        self.play(FadeIn(axes), FadeIn(dot), FadeIn(lable))

        self.wait()

        axes1 = Axes(include_numbers=False, x_range=[-4, 4, 1], y_range=[-4, 4, 1], z_range=[-4, 4, 1], x_length=8,
                     y_length=8, z_length=6)

        axes1.add(axes1.get_axis_labels(x_label="x'", y_label="y'"))
        axes1.set_color(YELLOW)
        dot1 = Dot(point=[2, 0.5, 0], color=YELLOW)
        lable1 = MarkupText("P'(2,0.5)").set_color(YELLOW).scale(0.3)
        lable1.next_to(dot1, RIGHT, buff=0.1)

        rad = 30 * DEGREES
        matrix_y = np.array([
            [np.cos(rad), -np.sin(rad), 0],
            [np.sin(rad), np.cos(rad), 0],
            [0, 0, 1]
        ])
        self.play(
            ApplyMethod(axes1.apply_matrix, matrix_y),
            ApplyMethod(dot1.apply_matrix, matrix_y),
            ApplyMethod(lable1.apply_matrix, matrix_y)
        )

        matrix = MathTex(r"""
               M=
               \begin{bmatrix}
               1 & 0 \\
               0 & 1 
               \end{bmatrix}""", tex_template=TexTemplateLibrary.ctex)

        matrix2 = MathTex(r"""
               M' =
               \begin{bmatrix} 
               cos(\theta) & -sin(\theta) \\ 
               sin(\theta) & cos(\theta) 
               \end{bmatrix} """, tex_template=TexTemplateLibrary.ctex).set_color(YELLOW)

        self.play(
            Create(matrix.to_corner(UL + LEFT)),
            Create(matrix2.next_to(matrix, direction=DOWN, aligned_edge=LEFT)),
        )

        self.wait()

        self.play(
            axes1.animate.shift([2, 2, 0]),
            lable1.animate.shift([2, 2, 0]),
            dot1.animate.shift([2, 2, 0]),

        )
        dot_o1 = Dot(point=ORIGIN)
        lable_o1 = MarkupText("O(0,0)").scale(0.3)
        lable_o1.next_to(dot_o1, RIGHT, buff=0.1)

        dot_o2 = Dot(point=[2, 2, 0], color=YELLOW)
        lable_o2 = MarkupText("O'(2,2)").set_color(YELLOW).scale(0.3)
        lable_o2.next_to(dot_o2, RIGHT, buff=0.1)

        self.add(dot_o1, lable_o1, dot_o2, lable_o2)
        self.wait()


with tempconfig({"preview": True, "disable_caching": False, "renderer": "opengl","save_last_frame" : True}):
    AexsMatix().render()
    exit(1)
