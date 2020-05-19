import numpy as np


# Differential equation solvers

# Euler forward
def EulerF(f,f0,h,ti,tf):
    t=np.arange(ti,tf+h,h)
    sol=np.empty(np.size(t))
    sol[0]=f0
    for i in range(1,np.size(t)):
        sol[i]=sol[i-1]+(h*f(t[i-1],sol[i-1]))
    return t,sol
