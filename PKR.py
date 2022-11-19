# %%
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate as interp

# %%
speed = [25, 35, 45, 30, 60, 120, 100, 100, 70, 75, 80, 65]
time = np.linspace(0, 11, 12)

# %%
print('Вектор часу: ', time)

# %%
plt.plot(time, speed)
plt.xlabel('Час (год)')
plt.ylabel('Швидкысть (км/год)')
plt.xticks(time)
plt.yticks(np.arange(0, 140, 10))
plt.grid()
plt.show()

# %%
f = interp.interp1d(time, speed, kind='cubic')
time_new = np.linspace(0, 11, 10000)
speed_new = f(time_new)

plt.plot(time_new, speed_new)
plt.plot(time, speed, 'o')
plt.xlabel('Час (год)')
plt.ylabel('Швидкість (км/год)')
plt.xticks(time)
plt.yticks(np.arange(0, 140, 10))
plt.grid()
plt.show()

# %%
distance = np.trapz(speed_new, time_new)
print(f'Шлях: {distance:.3f} км')

# %%
f = interp.interp1d(time, speed, kind='quadratic')
time_new = np.linspace(0, 11, 10_000)
speed_new = f(time_new)

plt.plot(time_new, speed_new)
plt.plot(time, speed, 'o')
plt.xlabel('Час (год)')
plt.ylabel('Швидкість (км/год)')
plt.xticks(time)
plt.yticks(np.arange(0, 140, 10))
plt.grid()
plt.show()

distance = np.trapz(speed_new, time_new)
print(f'Шлях: {distance:.3f} км')

# %%
alpha = 0.5
beta = 0.3
N = 1000000
S_0 = 990000
I_0 = 7000
R_0 = 3000
t0 = 0
tf = 25
t = np.linspace(t0, tf, 25)
S = []
S.append(S_0)
I = []
I.append(I_0)
R = []
R.append(R_0)

for i in range(1, 25):
    S.append(S[-1] - alpha * S[-1])
    I.append(I[-1] + alpha * S[-1] - beta * I[-1])
    R.append(R[-1] + beta  * I[-1])

# %%
plt.plot(t, S, 'b', marker = '^')
plt.xlabel('Час (діб)')
plt.ylabel('Вразливе населення')
plt.grid()
plt.show()

# %%
plt.plot(t, I, 'r', marker = 'o')
plt.xlabel('Час (діб)')
plt.ylabel('Інфіковане населення')
plt.grid()
plt.show()


# %%
plt.plot(t, R, 'g', marker = 's')
plt.xlabel('Час (діб)')
plt.ylabel('Одужавше населення')
plt.grid()
plt.show()

# %%
f_S = interp.interp1d(t, S, kind='cubic')
f_I = interp.interp1d(t, I, kind='cubic')
f_R = interp.interp1d(t, R, kind='cubic')

t_new = np.linspace(t0, tf, 100000)
S_new = f_S(t_new)
I_new = f_I(t_new)
R_new = f_R(t_new)


plt.plot(t_new, S_new, 'b', label = 'Вразливе')
plt.plot(t_new, I_new, 'r', label = 'Інфіковане')
plt.plot(t_new, R_new, 'g', label = 'Одужавше')
plt.xlabel('Час (діб)')
plt.ylabel('Населення')
plt.yticks(np.arange(0, 1100000, 100000))
plt.grid()
plt.legend()
plt.show()


