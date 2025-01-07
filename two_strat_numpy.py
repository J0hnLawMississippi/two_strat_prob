#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

strat1_capital = [5000]
strat2_capital = [5000]

n_sim = 1000000
strat1 = np.random.randint(2, size=(52, n_sim)).astype(float)
strat2 = np.random.randint(2, size=(52, n_sim)).astype(float)

strat1[strat1 == 1] = 1.02
strat1[strat1 == 0] = 0.99
strat2[strat2 == 1] = 1.01
strat2[strat2 == 0] = 0.98
                     
res1 = np.prod(strat1, axis=0)
res2 = np.prod(strat2, axis=0)
restot = (res1 + res2)/2

expectation = (0.5*100 - 0.5*50) + (0.5*50 - 0.5*100)
print(f"Weekly Expectation: {expectation}")
print(f"Probability of at least 10% profit: {sum(restot > 1.1) /n_sim}")
