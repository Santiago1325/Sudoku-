import SudokuGenerator
import SudokuBacktracking

def askSudoku():
    grid = [[0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]]
    for l in range(9):
        for c in range(9):
            x = input("Ingrese el numero para la fila {0}, columna {1}: ".format(l+1,c+1))
            try:
                n = int(x)
                if 0 < n and n < 10:
                    grid[l][c] = n
                else:
                    grid[l][c] = "X"
            except:
                grid[l][c] = "X"
    return grid


sudo = askSudoku()
SudokuGenerator.printSudoku(sudo)
SudokuBacktracking.Backtracking(sudo)
print()
SudokuGenerator.printSudoku(sudo)
