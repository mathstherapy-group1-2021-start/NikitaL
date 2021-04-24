# Никита Леонтьев
def FlipFlop(x):
    if (x % 5 == 0 and x % 7 == 0): 
        return "FlipFlop"  
    if (x % 5 == 0): 
        return "Flip"    
    if (x % 7 == 0): 
        return "Flop"  
    return str (x)
res = FlipFlop(77)
print(res)