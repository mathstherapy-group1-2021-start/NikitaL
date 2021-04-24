class FlippaFloppa:
    def __init__ (self, a1, a2):
        self.a = a1
        self.b = a2

    def test(self, x):
        a = x % self.a
        b = x % self.b
        if (a == 0 and b == 0): 
            return "FlipFlop"  
        if (a == 0): 
            return "Flip"    
        if (b == 0): 
            return "Flop"  
        return str (x)
    
    def prnt(self, x):
        print(self.test(x))

ff57 = FlippaFloppa(5, 7)
ff57.prnt(35) # FlipFlop
ff57.prnt(7) # Flop

ff32 = FlippaFloppa(3, 2)
ff32.prnt(6) # FlipFlop
ff32.prnt(9) # Flip