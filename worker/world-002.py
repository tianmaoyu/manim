
from manim import *
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface, OpenGLSurface
import numpy as np

class WorldDemo(ThreeDScene):
    def construct(self):
        # self.set_camera_orientation(phi=90 * DEGREES, theta=15 * DEGREES)
        # self.begin_ambient_camera_rotation(rate=0.5)
        # self.camera.light_source.animate.move_to()
        def uv_func(u, v):
            return 4 * np.array([
                np.cos(u) * np.sin(v),
                np.sin(u) * np.sin(v),
                -np.cos(v)
            ])
        #必须严格的 分辨率，范围
        sphere = OpenGLSurface(
            uv_func,
            u_range=[0, TAU],
            v_range=[0, PI],
            checkerboard_colors=[RED_D, RED_E],
            resolution=(101, 51))

        # 替换为你的纹理图片的路径 dark_image_file="night.jpg"
        #360_big.jpg
        texture = OpenGLTexturedSurface(uv_surface=sphere, image_file="360_big.jpg")
        self.add(texture)

        # self.play(texture.animate.scale(6),run_time=3)

        self.set_camera_orientation(phi=0 * DEGREES, theta=15 * DEGREES)

        self.move_camera(phi=45 * DEGREES, theta=15 * DEGREES,run_time=2)

        self.move_camera(phi=90 * DEGREES, theta=15 * DEGREES, run_time=2)

        # self.move_camera(phi=135 * DEGREES, theta=15 * DEGREES, run_time=2)
        #
        # self.move_camera(phi=180 * DEGREES, theta=15 * DEGREES, run_time=2)

        self.begin_ambient_camera_rotation(rate=0.5)
        #
        self.wait(5)

        #





# "renderer": "opengl"
with tempconfig({"preview": True, "disable_caching": True,"quality":"fourk_quality", "renderer": "opengl"}):
    WorldDemo().render()
    exit(1)
