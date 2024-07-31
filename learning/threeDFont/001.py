import random
import time

from manim import *
from manim.mobject.opengl.opengl_cylinder import OpenGLCylinder
from manim.mobject.opengl.opengl_image_mobject import OpenGLImageMobject
from manim.mobject.opengl.opengl_point_image_mobject import ImagePixelMobject
from manim.mobject.opengl.opengl_shpere import OpenGLSphere
from manim.mobject.opengl.opengl_something import OpenGLCone, OpenGLLine3D
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface, OpenGLSurface
import numpy as np
import sympy as sp
from manim.typing import Image
from PIL import Image
import json
import re

# 假设 JSON 数据存储在一个字符串中
json_data = '''{  
    "ο": {  
        "x_min": 0,  
        "x_max": 712,  
        "ha": 815,  
        "o": "m 906 0 l 756 0 l 648 303 l 251 303 l 142 0 l 0 0 l 376 1013 l 529 1013 l 906 0 m 610 421 l 452 867 l 293 421 l 610 421 "  
    }  
}'''

data = json.loads(json_data)
letter_o = data['ο']
path_data = letter_o['o']


def parse_path_data(path_data):
    commands = re.findall(r'[a-z][^a-z]*', path_data, re.IGNORECASE)
    vertices = []
    for command in commands:
        cmd = command[0]
        args = list(map(float, command[1:].strip().split()))
        if cmd == 'm':
            vertices.append([args[0], args[1], 0])
        elif cmd == 'q':
            vertices.append([args[0], args[1], 0])
            vertices.append([args[2], args[3], 0])
    return vertices


class demo01(ThreeDScene):
    def construct(self):
        # 解析 JSON 文件中的路径数据
        vertices_2d = parse_path_data(path_data)

        # 将二维顶点转换为三维顶点（添加 z 轴）
        depth = 100  # 深度
        vertices_3d_front = [[x, y, 0] for x, y, _ in vertices_2d]
        vertices_3d_back = [[x, y, depth] for x, y, _ in vertices_2d]
        vertices_3d = vertices_3d_front + vertices_3d_back

        # 生成面
        faces = []
        n = len(vertices_2d)
        for i in range(n):
            faces.append([i, (i + 1) % n, (i + 1) % n + n, i + n])

        vertices_3d=np.array(vertices_3d)/200
        # 创建 Polyhedron
        glyph = Polyhedron(
            vertex_coords=vertices_3d,
            faces_list=faces
        )
        self.add(glyph)
        glyph.set_color(RED)
        # self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)






class SquarePyramidScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        vertex_coords = [
            [1, 1, 0],
            [1, -1, 0],
            [-1, -1, 0],
            [-1, 1, 0],
            [0, 0, 2]
        ]
        faces_list = [
            [0, 1, 4],
            [1, 2, 4],
            [2, 3, 4],
            [3, 0, 4],
            [0, 1, 2, 3]
        ]
        pyramid = Polyhedron(vertex_coords, faces_list)
        self.add(pyramid)

        obj = Tetrahedron()
        self.add(obj.to_corner(UP))




with tempconfig({"preview": True, }):
    demo01().render()
    exit(1)
