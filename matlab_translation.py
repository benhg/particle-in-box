import numpy as np
from scipy.integrate import quad as integrate
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import quadpy
from math import sin
# Define constants and variables
n = 7;
Lx = 1;
hbar = 1;
m = 1;

def k(n):
	return n*np.pi/Lx;

w = hbar*k(n)**2/2*m;
A_const = np.sqrt(2/Lx);
t = np.linspace(0,10,50);

# Define the position and time functions
def psi(x, n):
	return A_const*np.sin(k(n)*x)

def phi(t):
    return np.exp(-1j*w*t)

def Psi(x, n, t):
	return psi(x, n) * phi(t)

def Psi_square(x, n, t):
	psi = Psi(x, n, t)
	return np.conj(psi) * psi

def A(n, f):

    def integrate_func(x):
        psi_res = psi(x, n) 
        fx = f(x)
        return fx * psi_res

    return integrate(integrate_func, 0, Lx)

def Psi_fourier(f_init, n_a, x, t):
    A_list = np.zeros(n_a, dtype=np.complex128)

    for i in range(n_a):
        A_list[i] = A(i, f_init)[0]

    psi_res = 0
    for i in range(n_a):
        psi_res += A_list[i]*Psi(x, n, t)

    return psi_res

def Psi_square_fourier(f, n_a, x, t):
    psi_res = Psi_fourier(f, n_a, x, t)
    return np.conj(psi_res) * psi_res


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
    x = np.linspace(0, Lx, 200)
    y = [Psi_fourier(lambda z: -7*np.exp(-1*z), n, x_c, i) for x_c in x] 
    line.set_data(x, y)
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=100, blit=True)

plt.show()