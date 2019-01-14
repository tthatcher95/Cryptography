import numpy as np

a = np.matrix([[1, 0, 0, 0, 1, 1, 1, 1],
               [1, 1, 0, 0, 0, 1, 1, 1],
               [1, 1, 1, 0, 0, 0, 1, 1],
               [1, 1, 1, 1, 0, 0, 0, 1],
               [1, 1, 1, 1, 1, 0, 0, 0],
               [0, 1, 1, 1, 1, 1, 0, 0],
               [0, 0, 1, 1, 1, 1, 1, 0],
               [0, 0, 0, 1, 1, 1, 1, 1]])

# inp = list(input("Enter array: "))


def column_stuff(list):
    matrix = []

    a = np.matrix([[1, 0, 0, 0, 1, 1, 1, 1],
                   [1, 1, 0, 0, 0, 1, 1, 1],
                   [1, 1, 1, 0, 0, 0, 1, 1],
                   [1, 1, 1, 1, 0, 0, 0, 1],
                   [1, 1, 1, 1, 1, 0, 0, 0],
                   [0, 1, 1, 1, 1, 1, 0, 0],
                   [0, 0, 1, 1, 1, 1, 1, 0],
                   [0, 0, 0, 1, 1, 1, 1, 1]])

    for x in list:
        matrix.append(int(x))

    b = np.matrix(matrix).T

    matrix = a * b
    new_matrix = []
    final_matrix = []
    for val in matrix:
        if val % 2 == 0:
            new_matrix.append(0)
        else:
            new_matrix.append(1)
    new_matrix = np.matrix(new_matrix) + np.matrix([1, 1, 0, 0, 0, 1, 1, 0])

    new_matrix = new_matrix % 2
    return np.matrix(new_matrix)

one = list("10000001")
two = list("10100111")
three = list("01001100")
four = list("01101101")
five = list("01001111")

print("'5' '8': {}".format(column_stuff(one)))
print("'d' '1': {}".format(column_stuff(two)))
print("'d' 'a': {}".format(column_stuff(three)))
print("'e' '3': {}".format(column_stuff(four)))
print("'6' '8': {}".format(column_stuff(five)))

print(column_stuff(two))
print(column_stuff(three))
print(column_stuff(four))
print(column_stuff(five))
