A = np.matrix('0 2 0; 3 4 5; 6 7 8')
print(A)
A_det = np.linalg.det(A)
print(format(A_det, '.9g'))
