import numpy as np
A = np.matrix('2 3 4 1; 1 2 3 4; 3 4 1 2; 4 1 2 3')
print(A)
A_det = np.linalg.det(A)
print(format(A_det, '.9g'))
