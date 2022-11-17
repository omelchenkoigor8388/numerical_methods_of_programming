import numpy as np
A = np.matrix('2 5 7; 6 3 4; 5 -2 -3')
print(A)
A_inv = np.linalg.inv(A)
print(A_inv)
