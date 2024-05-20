
from manim import *
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface, OpenGLSurface
import numpy as np

class WorldToCylinder(ThreeDScene):
    """
    world -> cylinder
    """
    def construct(self):
        self.set_camera_orientation(phi=90 * DEGREES, theta=15 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.5)
        # self.camera.light_source.animate.move_to()
        def uv_func(u, v):
            return 2 * np.array([
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

        # 替换为你的纹理图片的路径 dark_image_file="world-night.jpg"
        texture = OpenGLTexturedSurface(uv_surface=sphere, image_file="world-daytime.jpg")
        self.add(texture)
        # self.wait(1)
        points=texture.get_all_points()

        texture.get_num_points()

        #[r,phi,theta]
        spherical_points= np.apply_along_axis(cartesian_to_spherical,axis=1,arr=points)


        print(len(spherical_points))
        r=2
        # 球面到 柱面
        spherical_points[:,0]  = r* spherical_points[:, 2]
        spherical_points[:, 1] = r *np.sin(spherical_points[:, 1])
        spherical_points[:, 2] = 1

        #texture.points=spherical_points
        self.set_camera_orientation(phi=45 * DEGREES, theta=15 * DEGREES)
        self.wait(1)
        texture.get_num_points()
        print("")
        #theta 不变
        # spherical_points[:, 2] =





# "renderer": "opengl"
with tempconfig({"preview": True, "disable_caching": True,"quality":"fourk_quality", "renderer": "opengl"}):
    WorldToCylinder().render()
    exit(1)
