import scipy as sp 
import numpy as np
import matplotlib.pyplot as plt

Grupo = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8]

print(sp.stats.fit(sp.stats.norm, Grupo))


