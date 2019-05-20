import SudokuGenerator

def isCorrectSolved(sudoku):
    """Recibe un Sudoku completo y retorna si es correcto o no"""
    for n in range(0,81):
        nfila = n // 9
        ncolumna = n % 9
        columna = SudokuGenerator.Column(sudoku, ncolumna)
        fila = SudokuGenerator.Line(sudoku, nfila)
        caja = SudokuGenerator.Box(sudoku, ncolumna, nfila)
        if sudoku[nfila][ncolumna] == "X":
            return False
        if (columna.count(sudoku[nfila][ncolumna]) != 1):
            return False
        if (fila.count(sudoku[nfila][ncolumna]) != 1):
            return False
        if (caja.count(sudoku[nfila][ncolumna]) != 1):
            return False
    return True

def isCorrectUnsolved(usudoku):
    """Recibe un sudoku incompleto y retorna si es posible resolverlo o no"""
    for n in range(0,81):
        nfila = n // 9
        ncolumna = n % 9
        if usudoku[nfila][ncolumna] != "X":
            columna = SudokuGenerator.Column(usudoku, ncolumna)
            fila = SudokuGenerator.Line(usudoku, nfila)
            caja = SudokuGenerator.Box(usudoku, ncolumna, nfila)
            if (columna.count(usudoku[nfila][ncolumna]) != 1):
                return False
            if (fila.count(usudoku[nfila][ncolumna]) != 1):
                return False
            if (caja.count(usudoku[nfila][ncolumna]) != 1):
                return False
    return True   


def checkSudoku(sudoku):
    """Verifica si el Sudoku ya esta solucionado"""
    for line in sudoku:
        for number in line:
            if number == "X":
                return False
    return True

def isSafe(sudoku, colu, lin, number):
    """Verifica si el numero no se repite ni en la fila, columna y caja de 3x3"""
    box = SudokuGenerator.Box(sudoku, colu, lin)
    line = SudokuGenerator.Line(sudoku, lin)
    column = SudokuGenerator.Column(sudoku, colu)
    if number not in box:
        if number not in line:
            if number not in column:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
   
def Backtracking(sudoku):
    """Funcion recursiva que soluciona el Sudoku"""
    for n in range(81):
        fila = n // 9
        col = n % 9
        if sudoku[fila][col] == "X":
            for c in range (1,10):
                if isSafe(sudoku, col, fila, c):
                    sudoku[fila][col] = c
                    if checkSudoku(sudoku):
                        print("Sudoku terminado")
                        return True
                    if Backtracking(sudoku):
                        return True
                    sudoku[fila][col] = "X"
            return False
                        

            
                        
                        



                                
        
                    
                    
                
                        

            


