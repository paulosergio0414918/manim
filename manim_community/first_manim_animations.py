from manim import *
import numpy as np

class DataAssimilation(Scene):
    def construct(self):
        #creating axes
        axes = Axes(x_range=[-1,10], y_range=[-3,2])
        
        #create the graph
        surface = axes.plot(lambda x: 0.05*(2*np.sin(x)*np.sin(0.5*x)*np.sin(x/2.52)*np.cos(x/0.66)+np.cos(x*2) + np.sin(3*x/25))+1, color = BLUE)
        bathymetry = axes.plot(lambda x:np.cos(np.sin( x*np.sin(x*0.25))*np.cos(x))-3, color = RED)
        t = ValueTracker(-4)#estabelece o ínicio da aimação da onda
        #n = DecimalNumber(t.get_value())
        wave = always_redraw(lambda:(axes.plot(lambda x: np.exp(-((x-t.get_value())**2)/2)+1, color = BLUE)))
        g = VGroup(axes, surface, bathymetry)
        
        
        # inserting the animation
        self.play(Create(surface)) #constroe a animação da superfície
        self.wait(1) #gera um tempo entre as animações
        self.play(Create(bathymetry)) # constroe a animação da batmetria
        self.wait(1)
        self.play(Create(axes))# constroe a animação para o eixos 
        self.play(ReplacementTransform(surface, wave)) #substitui a superfície pela onda
        self.play(t.animate.set_value(15), run_time = 10) #cria a animação da onda
        self.wait(3)#cria um tempo para encerrar a apresentação.