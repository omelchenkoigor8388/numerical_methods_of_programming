import numpy as np
A = np.matrix('2 3 1; -1 1 0; 1 2 -1')
print(A)
B = np.matrix('1 2 1; 0 1 2; 3 1 1')
print(B)
C = A.dot(B)
D = B.dot(A)
F = C-D
print(F)
