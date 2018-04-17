
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)


matplotlib.rcParams['axes.unicode_minus'] = False
fig, ax = plt.subplots()

for x in range(30):
  for y in range(30):
    ax.plot(x, y, 'o', color='r')
ax.set_title('Using hyphen instead of Unicode minus')
plt.show()