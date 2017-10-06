# Demo animate 2.py
import salabim as sim


class AnimateWaitSquare(sim.Animate):
    def __init__(self, i):
        self.i = i
        super().__init__(
            rectangle0=(-10, -10, 10, 10), x0=300 - 30*i, y0=100, fillcolor0='red', linewidth0=0)
        
    def visible(self, t):
        return q[self.i] is not None
    
    
class AnimateWaitText(sim.Animate):
    def __init__(self, i):
        self.i = i
        super().__init__(text='', x0=300-30*i, y0=100, textcolor0='white')
        
    def text(self, t):
        component_i = q[self.i]
        
        if component_i is None:
            return ''
        else:
            return component_i.name()


def do_animation():
    env.animation_parameters()
    for i in range(10):
        AnimateWaitSquare(i)
        AnimateWaitText(i)
    show_length=sim.Animate(text='',x0=330,y0=100,textcolor0='black',anchor='w')
    show_length.text = lambda t: 'Length= ' + str(len(q))
    

class Person(sim.Component):
    def process(self):
        self.enter(q)
        yield self.hold(15)
        self.leave(q)

env = sim.Environment(trace=True)

q = sim.Queue('q')
for i in range(15):
    Person(name='{:02d}'.format(i), at=i*1)
    

do_animation()

env.run()
