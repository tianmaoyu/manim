from manim import *


class VectoDemo001(Scene):
    def construct(self):
        number_plane = NumberPlane(background_line_style={
            "stroke_color": TEAL,
            "stroke_width": 2,
            "stroke_opacity": 0.5
        })
        vec = Vector().set_color(BLUE)
        self.add(number_plane, vec)
        self.wait(1)
        self.play(ApplyMethod(vec.put_start_and_end_on, vec.get_start(), [5, 4, 0]))
        self.wait(1)

# "renderer": "opengl"
with tempconfig({"preview": True, "disable_caching": True}):
    VectoDemo001().render()
    exit(1)
