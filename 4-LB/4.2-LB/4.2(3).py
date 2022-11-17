import numpy as np
A = np.matrix('5 8 -4; 6 9 -5; 4 7 -3')
print(A)
B = np.matrix('3 2 5 ; 4 -1 3 ; 9 6 5')
print(B)
C = A.dot(B)
print(C)
