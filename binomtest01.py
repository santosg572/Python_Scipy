import scipy as sp 
import numpy as np
import matplotlib.pyplot as plt

x = '''
We roll a 6-sided die 24 times and it lands on the number “3” exactly 6 times. Perform a binomial test to 
determine if the die is biased towards the number “3.”
'''

print(x)

print(sp.stats.binom_test(x=6, n=24, p=1/6, alternative='greater'))



