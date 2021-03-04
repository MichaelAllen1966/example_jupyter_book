# A surface plot

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Create a 3D array
# meshgrid produces all combinations of given x and y
x=np.linspace(-3,3,256) # x goes from -3 to 3, with 256 steps
y=np.linspace(-3,3,256) # y goes from -3 to 3, with 256 steps
X,Y=np.meshgrid(x,y) # combine all x with all y

# A function of x and y for demo purposes
Z=np.sinc(np.sqrt(X**2 + Y**2))

fig=plt.figure(figsize=(5,5))
ax=fig.gca(projection='3d')
ax.plot_surface(X,Y,Z,cmap=cm.gray)

plt.show()