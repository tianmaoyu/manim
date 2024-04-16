
from manim import *


class Demo002(Scene):
    def construct(self):
        text= Text("不要送礼物")
        self.add(text)
        def move(obj,dt):
            print(f"-{dt}-"*20)
        text.add_updater(move)
        self.wait(2)


# "renderer": "opengl"
with tempconfig({"preview": True, "disable_caching": True}):
    Demo002().render()
    exit(1)