import numpy
import numpy as np


class Ras:
    
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2

    
    #instance method 
    def calc(self):
        y = 20 + (self.x1**2) + (self.x2**2) - 10*(np.cos((2*np.pi*self.x1)) + np.cos((2*np.pi*self.x2)))
        print("calc was called!")
        return y


point = Ras(1,3)
ans = point.calc()
print(ans)