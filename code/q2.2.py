import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt

x = np.linspace(-4,4,30) #points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list


randvar = np.loadtxt('gau.dat',dtype='double')
for i in range(0,30):
    err_ind = np.nonzero(randvar < x[i]) #checking probability condition
    err_n = np.size(err_ind) #computing the probability
    err.append(err_n/simlen) #storing the probability values in a list

def f(x):
    return (1-mp.erf(x/mp.sqrt(2)))/2

def g(x):
    return 1-f(x)

cdf = np.vectorize(g)

plt.plot(x.T,cdf(x))
plt.plot(x[0:30].T,err,"o")
plt.grid() 
plt.xlabel('$x$')
plt.legend(["Theory","Numercial"])
plt.ylabel('$F_X(x)$')
plt.show()

