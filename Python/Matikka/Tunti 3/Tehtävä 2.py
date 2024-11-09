import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-3*np.pi, 3*np.pi, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)

plt.figure(figsize=(19.2, 4.8))

plt.plot(X,C, color="red", linestyle="--", label="cos(x)")
plt.plot(X,S, color="blue", linestyle=":", label="sin(x)")

xticks=[-3*np.pi, -2.5*np.pi, -2*np.pi, -1.5*np.pi, -np.pi, -0.5*np.pi, 0,
        0.5*np.pi, np.pi, 1.5*np.pi, 2*np.pi, 2.5*np.pi, 3*np.pi]
xlabels=[r'$-3\pi$', r'$-\frac{5\pi}{2}$', r'$-2\pi$', r'$-\frac{3\pi}{2}$', r'$-\pi$', r'$-\frac{\pi}{2}$', r'$0$',
    r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$', r'$\frac{5\pi}{2}$', r'$3\pi$']

plt.xticks(xticks, xlabels)

plt.yticks(
    ticks=[-1, -0.5, 0, 0.5, 1],
    labels=[r'$-1$', r'$-0.5$', r'$0$', r'$0.5$', r'$1$']
)


plt.legend(loc="upper right")
plt.show()

#monke