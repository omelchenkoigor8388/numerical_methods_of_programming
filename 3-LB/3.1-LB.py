from scipy.misc import derivative 
a = -2. 
b = -1/2 
eps = 0.001 
def f(x): 
    return 3*x**4 - x**3 + 10*x**2 - 5*x -3 
def nuton(a,b,eps): 
    df2 = derivative(f, b, n = 2) 
    if (f(b)*df2>0): 
        xi = b 
    else: 
        xi = a 
    df = derivative(f,xi, n= 1) 
    xi_1 = xi - f(xi)/df 
    while (abs(xi_1 - xi)>eps): 
        xi = xi_1 
        xi_1 = xi - f(xi)/df 
    return print ('Solving the equation by Newton*s method x = ', xi_1) 
nuton (a,b,eps) 
