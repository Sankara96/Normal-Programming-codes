import math
from sympy import *

r = Symbol('r')
a = solve(-10000*(1+r)**3+3000*(1+r)**2+4000*(1+r)+5000,r)
print a


#for i in range(len(pow(10,100))):
   # current_value = previous_value+0+
