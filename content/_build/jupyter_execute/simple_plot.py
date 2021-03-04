# A simple matplotlib chart

Demonstrating a simple MatPlotLib using the preferred method.

import numpy as np
import matplotlib.pyplot as plt

# Set up empty figure and add one subplot
fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot()

# Create x and y
x = np.arange(11)
y = x ** 3

# Plot and add titles
ax.plot(x,y)
ax.set_xlabel('x')
ax.set_ylabel('x^3')
ax.set_title('Plot of x cubed')
ax.grid()

# Show plot
plt.show()