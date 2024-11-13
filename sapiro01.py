import scipy as sp 
import numpy as np
import matplotlib.pyplot as plt

Grupo = [15, 12, 11, 18, 15, 15, 9, 19, 14, 13, 11, 12, 18, 15, 16, 14, 16, 17, 15, 17, 13, 14, 13, 15, 17, 
19, 17, 18, 16, 14]

print(sp.stats.shapiro(Grupo))


