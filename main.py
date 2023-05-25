import numpy as np
import matplotlib.pyplot as plt

Xs = [0.5]
Rs = []

for r in np.arange(2,4,0.01):
  Rs.append(r)

for r in Rs:
  for i in range(100):
    Xs.append(r * Xs[i] * (1 - Xs[i]))

  rList = r * np.ones_like(Xs[-20:])
  plt.scatter(rList, Xs[-20:], c="blue", s=5)
  Xs = [0.5]

plt.show()
