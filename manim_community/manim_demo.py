from manim import *

class demo(Scene):
    def construct(self):
       t = Text("hello", color = DARK_BLUE, weight = BOLD, font_size = 48).shift(RIGHT*3, UP*2)
       self.play(Write(t))
       self.wait(1)
       #self.play(Unwrite(t))
       self.wait(1)

       s = Square(side_length = 2).shift(LEFT*2, DOWN*2)
       self.play(Write(s))
       self.wait(1)

       s2 = RoundedRectangle(fill_opacity = 0.2, color = RED, corner_radius = 1)
       T = Triangle(fill_opacity = 0.2, color = BLUE).scale(2)
       self.play(Transform(s,T)) 
       self.wait(2)