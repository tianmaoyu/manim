from manim import *
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface, OpenGLSurface
import numpy as np


class ParametricCurve(Scene):
    def construct(self):
        parametric_curve = ParametricFunction(
            lambda t: np.array([-5 + t, np.cos(t * 3), 0]),
            t_range=np.array([0, 5 * PI]),
            fill_opacity=0
        )
        parametric_curve.set_color(BLUE)
        self.play(Create(parametric_curve), run_time=5, rate_func=linear)



class Demo(ThreeDScene):
    def construct(self):
        p = RegularPolygon(5, color=DARK_GRAY, stroke_width=6).scale(3)
        lbl = VMobject()
        self.add(p, lbl)
        p = p.copy().set_color(BLUE)
        for time_width in [0.2, 0.5, 1, 2]:
            lbl.become(Tex(r"\texttt{time\_width=%.1f}" % time_width))
            self.play(ShowPassingFlash(
                p.copy().set_color(BLUE),
                run_time=2,
                time_width=time_width
            ))


class ConnectingDots(Scene):
    def construct(self):
        # 创建一个空的点集
        points = [ORIGIN]
        # 创建一个线段，初始时只有起点
        line = Line(points[0], points[0])
        self.add(line)

        # 动态添加点并更新线段的函数
        def update_line(mob, alpha):
            # 在这里你可以定义如何产生新点，这里以sin函数为例
            new_point = np.array([alpha * 5 * np.pi, np.sin(alpha * 5 * np.pi), 0])
            points.append(new_point)
            mob.become(Line(points[0], points[-1]))

        # 使用UpdateFromAlphaFunc来更新线段
        self.add(line)
        self.play(UpdateFromAlphaFunc(line, update_line), run_time=5)

        # 等待动画完成
        self.wait()


class DynamicPointLinking(Scene):
    def construct(self):
        # 初始化一个 ValueTracker 用于记录时间

        time_tracker = ValueTracker(0)
        # 创建一个空的点列表
        points = []

        # 定义一个函数来生成新的点
        def generate_point(dt):
            t = time_tracker.get_value()
            # 根据时间 t 生成一个新的点，这里用的是简单的参数方程
            new_point = np.array([np.sin(t), np.cos(t), 0])
            points.append(new_point)
            return new_point
            # 创建一个更新曲线的函数

        def update_curve(curve):
            if points:
                curve.set_points_smoothly(points)
            return curve

        curve = VMobject()
        curve.set_points_as_corners([ORIGIN, ORIGIN])  # 初始点
        # 使用 always_redraw 使曲线动态更新
        dynamic_curve = always_redraw(lambda: update_curve(curve))

        # 添加到场景中
        self.add(dynamic_curve)

        # 动画：在一定时间内不断生成新的点并更新曲线
        self.play(
            time_tracker.animate.set_value(2 * PI),  # 设定时间范围
            rate_func=linear,
            run_time=3  # 设定动画时长
        )

        # 在动画过程中不断生成点
        self.add_updater(lambda dt: generate_point())

        self.wait()


with tempconfig({"preview": True, "disable_caching": True,}):
    ParametricCurve().render()
    exit(1)
