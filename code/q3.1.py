import numpy as np
import matplotlib.pyplot as plt
import scipy
import math
x = np.linspace(-10,10,50) #points on the x axis

def logi(x):
    if x<0:
        return 0
    else:
        return 1-(math.exp(-x/2))
logcdf=scipy.vectorize(logi,otypes=['double'])


simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
randvar = np.loadtxt('unit.dat',dtype='double')
#randvar = np.loadtxt('gau.dat',dtype='double')
for i in range(0,50):
    err_ind = np.nonzero(randvar < x[i]) #checking probability condition
    err_n = np.size(err_ind) #computing the probability
    err.append(err_n/simlen) #storing the probability values in a list

plt.grid()
plt.plot(x.T,err,"o")
plt.plot(x,logcdf(x),color="orange")


plt.xlabel('$v$')
plt.ylabel('$F_V(v)$')
plt.legend(["Numerical","Theory"])
plt.show()
