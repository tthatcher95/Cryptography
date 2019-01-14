import numpy as np
matrix_num = input('Please enter the table for what you want to generate: ')
mod_num = input('Please enter number you want to mod by: ')
modulo_matrix = []

for x in range(1, int(matrix_num)):
    row = []
    for y in range(1, int(matrix_num)):
        row.append((y*x) % int(mod_num))
    modulo_matrix.append(row)

np_matrix = np.matrix(modulo_matrix)

print(np_matrix)
