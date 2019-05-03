import random

def Sudoku():
    """Inicializa el Sudoku con un sodoku valido ya establecido"""
    grid = [[1,2,3,4,5,6,7,8,9],
            [4,5,6,7,8,9,1,2,3],
            [7,8,9,1,2,3,4,5,6],
            [2,3,4,5,6,7,8,9,1],
            [5,6,7,8,9,1,2,3,4],
            [8,9,1,2,3,4,5,6,7],
            [3,4,5,6,7,8,9,1,2],
            [6,7,8,9,1,2,3,4,5],
            [9,1,2,3,4,5,6,7,8]]
    return grid

def Line(sudoku, position):
    """Retorna la linea del Sudoku"""
    return sudoku[position]

def Column(sudoku, position):
    """Retorna la columna del Sudoku"""
    return [line[position] for line in sudoku]

def Box(sudoku, col, fil):
    """Retorna la celda de 3x3 de acuerdo a la posicion del numero"""
    celda = []
    if col == 0 or col == 1 or col == 2:
        if fil == 0 or fil == 1 or fil == 2:
            celda = sudoku[0][0:3] + sudoku[1][0:3] + sudoku[2][0:3]
        elif fil == 3 or fil == 4 or fil == 5:
            celda = sudoku[3][0:3] + sudoku[4][0:3] + sudoku[5][0:3]
        elif fil == 6 or fil == 7 or fil == 8:
            celda = sudoku[6][0:3] + sudoku[7][0:3] + sudoku[8][0:3]
    if col == 3 or col == 4 or col == 5:
        if fil == 0 or fil == 1 or fil == 2:
            celda = sudoku[0][3:6] + sudoku[1][3:6] + sudoku[2][3:6]
        elif fil == 3 or fil == 4 or fil == 5:
            celda = sudoku[3][3:6] + sudoku[4][3:6] + sudoku[5][3:6]
        elif fil == 6 or fil == 7 or fil == 8:
            celda = sudoku[6][3:6] + sudoku[7][3:6] + sudoku[8][3:6]
    if col == 6 or col == 7 or col == 8:
        if fil == 0 or fil == 1 or fil == 2:
            celda = sudoku[0][6:9] + sudoku[1][6:9] + sudoku[2][6:9]
        elif fil == 3 or fil == 4 or fil == 5:
            celda = sudoku[3][6:9] + sudoku[4][6:9] + sudoku[5][6:9]
        elif fil == 6 or fil == 7 or fil == 8:
            celda = sudoku[6][6:9] + sudoku[7][6:9] + sudoku[8][6:9]
    return celda        
    
            
             
        


def swapLines(sudoku):
    """Intercambia las filas del sudoku entre ellas"""
    swap = random.randint(0,20)
    for x in range(swap):
        line = random.randint(0,2)
        line2 = random.randint(0,2)
        if sudoku[line] != sudoku[line2]:
            (sudoku[line],sudoku[line2]) = (sudoku[line2],sudoku[line])
    for x in range(swap):
        line = random.randint(3,5)
        line2 = random.randint(3,5)
        if sudoku[line] != sudoku[line2]:
            (sudoku[line],sudoku[line2]) = (sudoku[line2],sudoku[line])
    for x in range(swap):
        line = random.randint(6,8)
        line2 = random.randint(6,8)
        if sudoku[line] != sudoku[line2]:
            (sudoku[line],sudoku[line2]) = (sudoku[line2],sudoku[line])
    
def swapColumns(sudoku):
    """Intercambia las columnas del sudoku entre ellas"""
    swapLines(sudoku)
    gridver = []
    for x in range(9):
        columna = Column(sudoku, x)
        gridver.append(columna)
    swapLines(gridver)
    return gridver
    
        
def removeNumbers(sudoku,diff):
    """Remueve numeros aleatorios segun la dificultad seleccionada"""
    #1 = Facil
    #2 = Intermedio
    #3 = Dificil
    if diff == 1:
        print("Dificultad: Facil")
        print()
    if diff == 2:
        print("Dificultad: Intermedia")
        print()
    if diff == 3:
        print("Dificultad: Dificil")
        print()
    if 0 >= diff or diff > 3:
        myError = ValueError("{0} no es una dificultad valida. (Dificultades de 1 a 3)".format(diff))
        raise myError
        return 0
    clue = 0
    if diff == 1:
        nc = random.randint(32,42)
        print("N° de pistas:",81 - nc)
        print()
        while clue < nc:    
            n1 = random.randint(0,8)
            n2 = random.randint(0,8)
            if sudoku[n1][n2] == "X":
                continue
            elif sudoku[n1][n2] != "X" or sudoku[n1][n2] == 0:
                sudoku[n1][n2] = "X"
                clue += 1
    elif diff == 2:
        nc = random.randint(43,53)
        print("N° de pistas:",81 - nc)
        print()
        while clue < nc:    
            n1 = random.randint(0,8)
            n2 = random.randint(0,8)
            if sudoku[n1][n2] == "X":
                continue
            elif sudoku[n1][n2] != "X" or sudoku[n1][n2] == 0:
                sudoku[n1][n2] = "X"
                clue += 1
    elif diff == 3:
        nc = random.randint(54,64)
        print("N° de pistas:",81 - nc)
        print()
        while clue < nc:    
            n1 = random.randint(0,8)
            n2 = random.randint(0,8)
            if sudoku[n1][n2] == "X":
                continue
            elif sudoku[n1][n2] != "X" or sudoku[n1][n2] == 0:
                sudoku[n1][n2] = "X"
                clue += 1
    for l in range(9):
        for n in range(9):
            if sudoku[l][n] == 0:
                sudoku[l][n] = "X"
        
def printSudoku(sudoku):
    """Imprime el Sudoku"""    
    count2 = 1
    for row in sudoku:
        count = 1
        for number in row:
            if count % 3 != 0:
                print(number,end=" ")
                count += 1
            else:
                print(number,end="  ")
                count += 1
        if count2 % 3 != 0:
            print()
            count2 += 1
        else:
            print()
            print()
            count2 += 1
            
def fullSudoku():
    diff = int(input("Ingrese la dificultad: "))
    print()
    sudoku = Sudoku()
    sudoku2 = swapColumns(sudoku)
    removeNumbers(sudoku2, diff)
    return sudoku2
    



        
