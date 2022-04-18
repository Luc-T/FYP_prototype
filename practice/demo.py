import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np

# Make data.
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Plot the surface.


x2 = [x for x in range(100)]
y2 = [x**2 for x in x2]

for idx, x in enumerate(x2):

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    ax.scatter(x, y2[idx], 0.5, color='red', alpha=1)

    print(x,y2[idx])

    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)

    # Customize the z axis.
    ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    # A StrMethodFormatter is used automatically
    ax.zaxis.set_major_formatter('{x:.02f}')

    plt.show(block=False)

    move = input()

    plt.close()
