import SudokuGenerator

s = SudokuGenerator.fullSudoku()

def checkSudoku(sudoku):
    for line in sudoku:
        for number in line:
            if number == "X":
                print("Sudoku sin resolver")
                return False
    print("Sudoku completado")
    return True

def isSafe(sudoku, colu, lin, number):
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
    for n in range(81):
        fila = n // 9
        col = n % 9
        print("Fila", fila)
        print("Col", col)
        for c in range (1,10):
            print("Candidato",c)
            if sudoku[fila][col] == "X":
                if isSafe(sudoku, col, fila, c):
                    print("Celda Fila {0} Col {1}, reemplazada por: {2}".format(fila, col, c))
                    sudoku[fila][col] = c
                else:
                    print(c,"No es valido")
                    sudoku[fila][col] = "X"
            else:
                print("Celda llena. Fila {0}, Col {1}".format(fila, col))
                break
                


    return sudoku


SudokuGenerator.printSudoku(s)
sudokures = Backtracking(s)
print("\n")
SudokuGenerator.printSudoku(sudokures)
                                
                                
        
                    
                    
                
                        

            


