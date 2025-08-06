from manim import *
import numpy as np

def f(x):
    return 0.05*(2*np.sin(x)*np.sin(0.5*x)*np.sin(x/2.52)*np.cos(x/0.66)+np.cos(x*2)+np.sin(3*x/25))+1

def h(x):
    return np.cos(np.sin(x*np.sin(x*0.25))*np.cos(x))-3

class DataAssimilation(Scene):
    def construct(self):
        #creating axes
        axes = Axes(x_range=[-1,10], y_range=[-3,2])
        
        #create the objects
        surface = axes.plot(lambda x: f(x), color = BLUE)
        bathymetry = axes.plot(lambda x: h(x), color = RED)
        t = ValueTracker(-4)#estabelece o ínicio da aimação da onda 
        wave = always_redraw(lambda:(axes.plot(lambda x: np.exp(-((x-t.get_value())**2)/2)+1, color = BLUE)))
        
                
        text_1 = Tex("Superfície").shift(RIGHT*4, UP*2.5)#.next_to(surface, UP, buff = 0.1)
        text_2 = Tex("Batimetria").shift(DOWN*2.5, RIGHT*4)#.next_to(bathymetry, DOWN, buff = 0.1)
        
      
        arrow1 = Line(start = [-2, f(-2)+0.8, 0], end = [-2, h(-2)-0.2, 0]).add_tip(tip_shape = StealthTip).add_tip(at_start = True, tip_shape = StealthTip)
        arrow2 = Line(start = [0, f(0)+0.6, 0], end = [0, h(0)+0.2, 0]).add_tip(tip_shape = StealthTip).add_tip(at_start = True, tip_shape = StealthTip)
        arrow3 = Line(start = [-5, f(-5)+0.8, 0], end = [-5, h(-5)+0.3, 0]).add_tip(tip_shape = StealthTip).add_tip(at_start = True,tip_shape = StealthTip)
        arrow4 = Line(start = [5, f(5)+0.9, 0], end = [5, h(5)+0, 0]).add_tip(tip_shape = StealthTip).add_tip(at_start = True, tip_shape = StealthTip)
        arrow_group = VGroup(arrow1,arrow2, arrow3, arrow4)

        text_3 = Text("H_1",).next_to(arrow1)
        text_4 = Text("H_2").next_to(arrow2)
        text_5 = Text("H_3").next_to(arrow3)
        text_6 = Text("H_4").next_to(arrow4)

        text_group = VGroup(text_3, text_4, text_5, text_6)


        # animate the objects
        self.add(NumberPlane())
        self.play(Create(surface), Write(text_1)) #constroe a animação da superfície
        self.wait(1) #gera um tempo entre as animações
        self.play(Create(bathymetry), Write(text_2)) # constroe a animação da batmetria
        self.wait(1)
        #self.play(Create(axes))# constroe a animação para o eixos 
        self.play(Unwrite(text_1), Unwrite(text_2))
        self.play(Write(arrow_group), Write(text_group))
        self.play(ReplacementTransform(surface, wave)) #substitui a superfície pela onda
        self.play(t.animate.set_value(15), run_time = 10) #cria a animação da onda
        self.wait(3)#cria um tempo para encerrar a apresentação.