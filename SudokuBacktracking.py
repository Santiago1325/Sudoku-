import SudokuGenerator

s = SudokuGenerator.fullSudoku()

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
                        
    
SudokuGenerator.printSudoku(s)
Backtracking(s)
print()
SudokuGenerator.printSudoku(s)
            
            
                        
                        



                                
        
                    
                    
                
                        

            


