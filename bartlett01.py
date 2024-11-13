import scipy as sp 
import numpy as np
import matplotlib.pyplot as plt

m1 = [1,2,3,4,5]
m2 = [1, 3, 5, 7, 9]
m3 = [1,4,7,10,13]
m4 = [1,5,9,13,17]
m5 = [1,6,11,16,21]

print(sp.stats.bartlett(m1, m2, m3, m4, m5))


