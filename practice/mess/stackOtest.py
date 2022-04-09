import math 

import numpy as np
import matplotlib.pyplot as plt
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter



def surface_map(func, xmin=0, xmax=1, ymin=0, ymax=1, step_size=0.05, maxz=25000):
    X, Y = meshgrid(
        np.arange(xmin, xmax, step_size),
        np.arange(ymin, ymax, step_size))
    Z = np.zeros(X.shape)

    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            Z[i, j] = min(func(X[i, j], Y[i, j]), maxz)

    return X, Y, Z


def plot_surface(X, Y, Z, xlabel, ylabel, zlabel, title, point=None, size=25):
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    surf = ax.plot_surface(X, Y, Z, 
        rstride=1, cstride=1, vmin=0, vmax=20*1000,
        cmap=cm.RdBu, linewidth=0, antialiased=True)

    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.set_title(title)

    fig.colorbar(surf, shrink=0.5, aspect=5)
    if point:
        ax.hold(True)
        func, fpr, recall = point
        ax.scatter([fpr], [recall], [
            func(fpr, recall)
        ], s=size, c='b', marker='.', zorder=10)
    plt.show()

    # create mesh 
R, FPR, FuncValue = surface_map(my_function, xmin=0, xmax=1, ymin=0, ymax=1, step_size=0.05, maxz=20*1000)

# plot it
plot_surface(R, FPR, FuncValue, 
        xlabel="Recall", 
        ylabel="FPR", 
        zlabel="Function Value", 
        title="Recall Settings Payout Function",
        point=(my_function, 0.5, 0.5))