import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from math import exp

#Constants
h = 6.626e-34
hbar = h / 2*np.pi
m = 9.11e-31
#Values for L and x
x_list = np.linspace(0,1,100)
L = 1

def psi(n, L, x, t):
    time_dependent_bit = np.exp(-1j * (n/hbar) * t)

    total_func = (np.sqrt(2/L)*np.sin(n*np.pi*x/L) ) * (time_dependent_bit)
    return total_func

def psi_2(n, L, x, t):
    return np.conj(psi(n,L,x, t)) * psi(n,L,x, t)


fig = plt.figure(figsize=(15,10))
plt.suptitle("Wave Function Modulus Squared", fontsize=18)
ims = []

for t in np.linspace(0, 10, 1000):
    psi_2_list = [0]*100
    for n in range(3):
        temp_list = []
        for x in np.linspace(0, L, 100):
            temp_list.append(psi_2(n, L, x, t))
        psi_2_list = [psi_2_list[i] + temp_list[i] for i in range(len(temp_list))] 
        
    
    ims.append(plt.plot(x_list, psi_2_list))

plt.xticks(np.arange(0, L, step=0.5))
plt.xlabel("L", fontsize=13)
plt.ylabel("Ψ*Ψ", fontsize=13)
plt.title("n="+str(1), fontsize=16)
plt.grid()

im_ani = animation.ArtistAnimation(fig, ims, interval=50, repeat_delay=3000,
                                   blit=True)

plt.show()