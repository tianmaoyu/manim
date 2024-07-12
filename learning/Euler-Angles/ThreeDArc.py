from manim import *


class ThreeDArc(ThreeDScene):
    def construct(self):
        # 设置摄像机角度
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # 定义弧的参数
        start_angle = 0
        angle = -PI / 2  # 这里你可以使用你的 yRad

        # 定义一个参数化函数来创建 3D 弧
        arc = ParametricFunction(
            lambda t: np.array([
                np.cos(start_angle + t * angle),
                np.sin(start_angle + t * angle),
                0  # 如果你想让弧在 xy 平面上
            ]),
            t_range=np.array([0, 1]),
            color=BLUE
        )

        # 添加弧到场景中
        self.add(arc)

        # 添加轴以更好地展示 3D 效果
        axes = ThreeDAxes()
        self.add(axes)

        # 旋转和显示
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(1)
# "#004000"
with tempconfig({"preview": True, "disable_caching": False, "renderer": "opengl","background_color" : "#000000"}):
    ThreeDArc().render()
    exit(1)
