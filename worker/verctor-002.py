
from manim import *


class VectoDemo002(Scene):
    def construct(self):
        vec= Vector([2,3])
        label= vec.coordinate_label(color=YELLOW)
        vec.add(label)
        self.add(vec)


# "renderer": "opengl"
with tempconfig({"preview": True, "disable_caching": True}):
    VectoDemo002().render()
    exit(1)