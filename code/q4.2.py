#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib
matplotlib.rcParams['backend'] = 'GTK3Agg'
import matplotlib.pyplot as plt
import scipy

def tri_cdf(x):
    if (x < 0): return 0
    elif (x < 1): return (x**2)/2
    elif (x < 2): return -(x**2)/2 + 2*x - 1
    else: return 1

tdfunc = scipy.vectorize(tri_cdf, otypes=['double'])


x = np.linspace(-2,4,60)#points on the x axis
#points for analytical cdf
simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
randvar = np.loadtxt('td.dat',dtype='double')
#randvar = np.loadtxt('gau.dat',dtype='double')
for i in range(0,60):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

plt.plot(x,err,'o')#plotting empirical CDF

plt.plot(x,tdfunc(x))#plotting analytical CDF
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_T(x)$')
plt.legend(["Numerical", "Theoretical"])
plt.savefig('../figs/q4.2.png')
