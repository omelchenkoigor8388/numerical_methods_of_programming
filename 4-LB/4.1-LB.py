# заповнення матриці
from random import random
N = 4
matrix = []
for i in range(N):
    row = []
    for j in range(N):
        row.append(int(random()*10))
        matrix.append(row)

# виведення матриці на екран
for row in matrix:
    print(row)

# сума елементів головної діагоналі
sumMain = 0
# сума елементів побічної діагоналі
sumSecondary = 0
# Кількість ітерацій циклу відповідає
# розмірності квадратної матриці
for i in range(N):
    # У елементів головної діагоналі індекси однакові.
    # Із матрицівибирається елемент і додається до суми.
    sumMain += matrix[i][i]
    # У елементів побічної діагоналі другий індекс
    # відлічується з кінця
    sumSecondary += matrix[i][N-i-1]
    
# виведення сум
print(sumMain)
print(sumSecondary)
