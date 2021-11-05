import numpy as np
import itertools

dim = input('Enter the size of the matrix (the number must be natural): ')
while not dim.isdigit() or dim == '0':
    dim = input('Enter the size of the matrix (the number must be natural): ')

def random_matrix(dim):
    """
    The function generates dim x dim array of integers
    between 0 and 10.
    """
    matrix = np.random.randint(10, size = (dim, dim))
    return matrix

def permutations(matrix):
    """
    The function creates a list with possible permutations and index -1 or 1 according to the rule.
    """
    a = ''
    for i in range(len(matrix)):
        a += str(i+1)
    sao = list(itertools.permutations(a, len(a)))
    multiplier = []
    for i in sao:
        m = 0
        for j in range(int(dim)):
            for k in range(j+1,int(dim)):
                if i[j] > i[k]:
                    m += 1
        if m % 2 == 0:
            index = 1
        else:
            index = -1
        multiplier += [[index] + [matrix[k][int(i[k])-1] for k in range(len(i))]]
    return multiplier

def multiplication(blin):
    """
    The function creates a list of the sum of all permutations.
    """
    terms = []
    for i in blin:
        constant = 1
        for j in i:
            constant *= j
        terms.append(constant)
    return terms

def summ(neverlend):
    """
    The function finds the determinant.
    """
    result = 0
    for i in neverlend:
        result += i
    return result

matrix = random_matrix(int(dim))
print('Determinant: ', summ(multiplication(permutations(matrix))))
print('Determinant by function np.linalg.det() = ', round(np.linalg.det(matrix), 2))