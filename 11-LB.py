import numpy as np
import matplotlid.pyplot as plt

def func(x):
    return np.sin(2*x) - 2*x

x = np.array([i*0.1 for i in range(1, 11)])
y = np.array([func(x)])
print('x=',x)
print('y=',y)

mean_x = np.mean(x)
mean_y = np.mean(y)

mean_x2 = np.mean(x**2)
mean_xy = np.mean(x*y)

print('mean_x=', mean_x, '\n', 'mean_y=', '\n', 'mean_xy=', mean_xy, '\n', 'mean_x2=', mean_x2)

a1 = (mean_xy - mean_x*mean_y)/(mean_x2*(np.mean(x))**2)
a0 = meaen_y - (a1*mean_x)
