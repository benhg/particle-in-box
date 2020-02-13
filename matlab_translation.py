import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# Define constants and variables
n = 3;
Lx = 1;
hbar = 1;
m = 1;

def k(n):
	return n*np.pi/Lx;

w = hbar*k(n)**2/2*m;
A = np.sqrt(2/Lx);
t = np.linspace(0,10,50);

# Define the position and time functions
def psi(x, n):
	return A*np.sin(k(n)*x)

def phi(t):
    return np.exp(-1j*w*t)

def Psi(x, n, t):
	return psi(x, n) * phi(t)

def Psi_square(x, n, t):
	psi = Psi(x, n, t)
	return np.conj(psi) * psi

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, Lx), ylim=(-2, 2))
line, = ax.plot([], [], lw=2)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,


# animation function.  This is called sequentially
def animate(i):
    x = np.linspace(0,Lx,200)
    y = Psi(x, n, i)
    line.set_data(x, y)
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=100, blit=True)

plt.show()