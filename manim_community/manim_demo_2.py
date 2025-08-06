from manim import *

class demo(Scene):
    def construct(self):
       c = Circle(radius = 0.5, stroke_width = 10, color = RED, fill_opacity = 0.3)
       r = SurroundingRectangle(c, color = BLUE, corner_radius = 0.1)
       t = Tex("Manim").next_to(r, UP, buff = 0.5)
         
       
       cr = VGroup(c, r)
       
       self.play(Write(c), DrawBorderThenFill(r), Write(t))
       self.play(t.animate.move_to([-4,0,0]), cr.animate.move_to([4,0,0]))

       #arrow = Arrow(start=[-4, 3.5, 0], end=[2, 3.5, 0], color=YELLOW)
       arrow = always_redraw(lambda: Line(buff = 0.5, start = cr.get_left(), end = t.get_right()).add_tip(tip_shape = StealthTip).add_tip(at_start = True, tip_shape = StealthTip))
       self.play(Write(arrow))
       self.play(Indicate(t, 1.5, color = ORANGE))
       self.play(Rotate(r, angle = PI/2), ScaleInPlace(c, 2))
       self.play(cr.animate.move_to([0,0,0]))
       self.play(FadeOut(t,arrow), run_time = 0.25)
       self.play(ShrinkToCenter(r), ScaleInPlace(c, 30))
       self.play(FadeOut(c))
       self.wait(2) 



#comentários de ajustes
#stroke_width-> coloca uma linha mais grossa en torno do círculo.
#c = Circle(radius = 0.5, stroke_width = 10).set_color("#ffffff") <--- outra forma de configurar a cor de objeto.
#buff <--- gera um espaço entre dois objetos.
#objeto.animate.move_to([x,y,z]) <-- cria uma animação que move o objeto em questão para o ponto (x,y,z).