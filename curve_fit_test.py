import numpy as np
from scipy.optimize import curve_fit, minimize
import matplotlib.pyplot as plt

def func(x, a, b, c):
    return a * np.exp(-b * x) + c
    
    
#50 values in [0, 4] 
xdata = np.linspace(0, 4, 50)
print "xdata=", xdata
y = func(xdata, 2.5, 1.3, 0.5)
print "y=", y
ydata = y + 0.2 * np.random.normal(size=len(xdata))
print "ydata=", ydata

plt.plot( xdata, y, 'bs', label = "function")
plt.plot( xdata, ydata, 'g--', label = "function")
plt.xlabel('time')
plt.title("y")
plt.ylabel('x')
plt.legend()
plt.savefig('curve_fit_test.png')
plt.close()

popt, pcov = curve_fit(func, xdata, ydata)

print popt

res = minimize( func, ( 1., 1., 1. ), method = 'SLSQP', bounds = ((0., None), (0., None), (0., None)) )
print res