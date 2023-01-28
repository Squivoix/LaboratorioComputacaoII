#A = 3  5  1  6
#    6  2  0  9
#    7  3  5  4
#    10 4  2  1

#B = 6  2  8  3
#    9  1  3  4
#    3  3  4  4
#    8  7  0  6

#Escreva um programa em Python que realize a
#operação de multiplicação e soma de matrizes 4x4, e que seja capaz de calcular a seguinte equação:
#C = A * B + 2 * A

def Q_2() :
    A = [[3, 5, 1, 6],
         [6, 2, 0, 9],
         [7, 3, 5, 4],
         [10, 4, 2, 1]]

    B = [[6, 2, 8, 3],
         [9, 1, 3, 4],  
         [3, 3, 4, 4],
         [8, 7, 0, 6]]

    C = [[0, 0, 0, 0],
         [0, 0, 0, 0],  
         [0, 0, 0, 0],
         [0, 0, 0, 0]]
    
    D = [[0, 0, 0, 0],
         [0, 0, 0, 0],  
         [0, 0, 0, 0],
         [0, 0, 0, 0]]
    
    E = [[0, 0, 0, 0],
         [0, 0, 0, 0],  
         [0, 0, 0, 0],
         [0, 0, 0, 0]]

    # Multiplicação primeira parte C = (A * B)
    for line in range(4) :
        for column in range(4) :
            for i in range(4) :
                C[line][column] += A[line][i] * B[i][column]
    
    # Multiplicação primeira parte D = (2 * A)
    for line in range(4) :
        for column in range(4) :
            D[line][column] = A[line][column] * 2

    # Soma das duas matrizes E = (C + D)
    for line in range(4) :
        for column in range(4) :
            E[line][column] = C[line][column] + D[line][column]

    print("------- C = (A * B) -------\n")
    for i in range(4) :
        for j in range(4) :
            print(C[i][j], end='\t')
        print('\n')

    print("------- D = (2 * A) -------\n")
    for i in range(4) :
        for j in range(4) :
            print(D[i][j], end='\t')
        print('\n')

    print("------- E = (C + D) -------\n")
    for i in range(4) :
        for j in range(4) :
            print(E[i][j], end='\t')
        print('\n')
    