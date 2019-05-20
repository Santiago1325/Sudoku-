import pygame,sys,SudokuBacktracking,SudokuGenerator,ChangeNumber
from pygame.locals import *

"""Creacion de colores y ventana"""

c_aguamarina = pygame.Color(0,128,128)
c_negro = pygame.Color(0,0,0)
c_blanco = pygame.Color(255,255,255)

pygame.init()

sx = 700
sy = 700

ventana = pygame.display.set_mode((sx,sy))
pygame.display.set_caption("Sudoku Melo")


def drawSudoku(sudo):
    """Dibuja el Sudoku en la pantalla"""
    fuente3 = pygame.font.SysFont("Franklin Gothic Medium",50)
    for line in range(9):
        for col in range(9):
            if sudo[line][col] != "X":
                integer = fuente3.render(str(sudo[line][col]),1, c_negro)
                ventana.blit(integer,((100 + col * 52),(100 + line *50)))

def defaultNumbers(sudo):
    ogs = []
    for line in range(9):
        for col in range(9):
            if sudo[line][col] != "X":
                ogs.append((100+col*52,100+line*50))
    return ogs
                

def main():
    """Definicion de variables importantes"""
    Svacio = SudokuGenerator.resetGrid()
    Svacio2 = SudokuGenerator.resetGrid()
    r1 = 0
    c1 = 0
    ac = "X"
    terminado = "Presione ESPACIO para resolver."
    dif = "Dificultad: "
    Inicio = True
    Menu = False
    Jugar = False
    Resolver = False
    Instrucciones = False
    while True:           
        """Game Loop"""
        while Inicio:
            """Ventana de inicio"""
            ventana.fill(c_aguamarina) 
            fuente1 = pygame.font.SysFont("Franklin Gothic Medium",80)
            texto1 = fuente1.render("SUDOKU MELO", True, c_negro, None)
            fuente2 = pygame.font.SysFont("Lucida Console", 25)
            texto2 = fuente2.render("Presione SPACE para empezar", True, c_negro, None)  
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == K_SPACE:
                        Inicio = False
                        Menu = True
            ventana.blit(texto1,(100,250))
            ventana.blit(texto2,(160,400))
            pygame.display.flip()   
        while Menu:
            """Ventana del menu"""
            ventana.fill(c_aguamarina)
            texto3 = fuente1.render("MENU", True, c_negro, None)
            texto4 = fuente2.render("F1 - Jugar", True, c_negro, None)
            texto5 = fuente2.render("TAB - Instrucciones", True, c_negro, None)
            texto6 = fuente2.render("F3 - Resolver", True, c_negro, None)
            texto7 = fuente2.render("ESCAPE - Salir", True, c_negro, None)       
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == K_TAB:
                        Menu = False
                        Instrucciones = True
                    if event.key == K_F3:
                        Menu = False
                        Resolver = True
                    if event.key == K_F1:
                        Menu = False
                        Jugar = True
            ventana.blit(texto3,(260,150))
            ventana.blit(texto4,(200,300))
            ventana.blit(texto5,(200,350))
            ventana.blit(texto6,(200,400))
            ventana.blit(texto7,(200,450))
            pygame.display.flip()           
        while Instrucciones:
            """Ventana de instrucciones"""
            ventana.fill(c_aguamarina)
            fuente3 = pygame.font.SysFont("Franklin Gothic Medium",60)
            fuente4 = pygame.font.SysFont("Lucida Console", 30)
            fuente5 = pygame.font.SysFont("Lucida Console", 15)
            texto8 = fuente3.render("INSTRUCCIONES", True, c_negro, None)
            texto9 = fuente4.render("JUEGO:", True, c_negro, None)
            texto10 = fuente5.render("· Presione F-M-D dependiendo de la dificultad deseada", True, c_negro, None)
            texto16 = fuente5.render("· De click en los recuadros para reemplazar por el numero seleccionado", True, c_negro, None)
            texto17 = fuente5.render("· Use los numeros para seleccionar el numero a poner", True, c_negro, None)
            texto14 = fuente5.render("· Presione BACKSPACE para ir a Menu", True, c_negro, None)
            texto18 = fuente5.render("· Presione ESPACIO para verificar", True, c_negro, None)
            texto19 = fuente5.render("· Presione ESPACIO para resolver", True, c_negro, None)
            texto20 = fuente5.render("· Presione R para resolver", True, c_negro, None)
            texto21 = fuente5.render(". Presione X para resetear", True, c_negro, None)
            texto11 = fuente4.render("RESOLVER:", True, c_negro, None)
            texto15 = fuente5.render("· Presione BACKSPACE para ir a Menu", True, c_negro, None)
            texto12 = fuente4.render("SALIR:", True, c_negro, None)
            texto13 = fuente5.render("· Presione en cualquier ventana ESCAPE para salir", True, c_negro, None)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_BACKSPACE:
                        Instrucciones = False
                        Menu = True
            ventana.blit(texto8,(150,50))
            ventana.blit(texto9,(50,120))
            ventana.blit(texto10,(60,160))
            ventana.blit(texto14,(60,270))
            ventana.blit(texto11,(50,300))
            ventana.blit(texto15,(60,340))
            ventana.blit(texto12,(50,500))
            ventana.blit(texto13,(60,540))
            ventana.blit(texto16,(60,180))
            ventana.blit(texto17,(60,205))
            ventana.blit(texto18,(60,230))
            ventana.blit(texto20,(60,250))
            ventana.blit(texto19,(60,370))
            ventana.blit(texto16,(60,400))
            ventana.blit(texto17,(60,430))
            ventana.blit(texto21,(60,460))
            pygame.display.flip()    
        while Resolver:
            """Ventana para resolver un Sudoku"""
            ventana.fill(c_aguamarina)
            fuente3 = pygame.font.SysFont("Franklin Gothic Medium",50)
            Instr = fuente3.render("Ingrese el Sudoku a resolver.",True, c_negro, None)
            actnumber = fuente3.render(str(ac), True, c_negro, None)
            finish = fuente3.render(terminado, True, c_negro, None)
            pygame.draw.line(ventana, c_blanco, (100,100), (550,100), 2)
            pygame.draw.line(ventana, c_blanco, (100,150), (550,150), 2)
            pygame.draw.line(ventana, c_blanco, (100,200), (550,200), 2)
            pygame.draw.line(ventana, c_blanco, (100,250), (550,250), 6)
            pygame.draw.line(ventana, c_blanco, (100,300), (550,300), 2)
            pygame.draw.line(ventana, c_blanco, (100,350), (550,350), 2)
            pygame.draw.line(ventana, c_blanco, (100,400), (550,400), 6)
            pygame.draw.line(ventana, c_blanco, (100,450), (550,450), 2)
            pygame.draw.line(ventana, c_blanco, (100,500), (550,500), 2)
            pygame.draw.line(ventana, c_blanco, (100,550), (550,550), 2)   
            pygame.draw.line(ventana, c_blanco, (100,100), (100,550), 2)
            pygame.draw.line(ventana, c_blanco, (150,100), (150,550), 2)
            pygame.draw.line(ventana, c_blanco, (200,100), (200,550), 2)
            pygame.draw.line(ventana, c_blanco, (250,100), (250,550), 6)
            pygame.draw.line(ventana, c_blanco, (300,100), (300,550), 2)
            pygame.draw.line(ventana, c_blanco, (350,100), (350,550), 2)
            pygame.draw.line(ventana, c_blanco, (400,100), (400,550), 6)
            pygame.draw.line(ventana, c_blanco, (450,100), (450,550), 2)
            pygame.draw.line(ventana, c_blanco, (500,100), (500,550), 2)
            pygame.draw.line(ventana, c_blanco, (550,100), (550,550), 2)
            ventana.blit(Instr,(5,10))
            ventana.blit(actnumber,(40,100))
            ventana.blit(finish,(5,600))
            drawSudoku(Svacio)                        
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_BACKSPACE:
                        Resolver = False
                        Menu = True
                if event.type == KEYDOWN:
                    if event.key == K_0:
                        ac = "X"
                        terminado = "Presione ESPACIO para resolver."
                if event.type == KEYDOWN:                        
                    if event.key == K_1:
                        ac = 1
                if event.type == KEYDOWN:
                    if event.key == K_2:
                        ac = 2
                if event.type == KEYDOWN:
                    if event.key == K_3:
                        ac = 3
                if event.type == KEYDOWN:
                    if event.key == K_4:
                        ac = 4
                if event.type == KEYDOWN:
                    if event.key == K_5:
                        ac = 5
                if event.type == KEYDOWN:
                    if event.key == K_6:
                        ac = 6
                if event.type == KEYDOWN:
                    if event.key == K_7:
                        ac = 7
                if event.type == KEYDOWN:
                    if event.key == K_8:
                        ac = 8
                if event.type == KEYDOWN:
                    if event.key == K_9:
                        ac = 9 
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        if SudokuBacktracking.isCorrectUnsolved(Svacio):
                            SudokuBacktracking.Backtracking(Svacio)
                            terminado = "Sudoku terminado."
                        else:
                            terminado = "Ingrese un Sudoku valido"                            
                if event.type == KEYDOWN:
                    if event.key == K_x:
                        Svacio = SudokuGenerator.resetGrid()
                if event.type == MOUSEBUTTONDOWN:
                    c1,r1 = pygame.mouse.get_pos()
                    if not SudokuBacktracking.isCorrectSolved(Svacio):
                        ChangeNumber.changeNum(Svacio, c1, r1, ac)
            pygame.display.flip()
            
        while Jugar:
            """Ventana para jugar"""
            ventana.fill(c_aguamarina)
            fuente3 = pygame.font.SysFont("Franklin Gothic Medium",50)
            pygame.draw.line(ventana, c_blanco, (100,100), (550,100), 2)
            pygame.draw.line(ventana, c_blanco, (100,150), (550,150), 2)
            pygame.draw.line(ventana, c_blanco, (100,200), (550,200), 2)
            pygame.draw.line(ventana, c_blanco, (100,250), (550,250), 6)
            pygame.draw.line(ventana, c_blanco, (100,300), (550,300), 2)
            pygame.draw.line(ventana, c_blanco, (100,350), (550,350), 2)
            pygame.draw.line(ventana, c_blanco, (100,400), (550,400), 6)
            pygame.draw.line(ventana, c_blanco, (100,450), (550,450), 2)
            pygame.draw.line(ventana, c_blanco, (100,500), (550,500), 2)
            pygame.draw.line(ventana, c_blanco, (100,550), (550,550), 2)   
            pygame.draw.line(ventana, c_blanco, (100,100), (100,550), 2)
            pygame.draw.line(ventana, c_blanco, (150,100), (150,550), 2)
            pygame.draw.line(ventana, c_blanco, (200,100), (200,550), 2)
            pygame.draw.line(ventana, c_blanco, (250,100), (250,550), 6)
            pygame.draw.line(ventana, c_blanco, (300,100), (300,550), 2)
            pygame.draw.line(ventana, c_blanco, (350,100), (350,550), 2)
            pygame.draw.line(ventana, c_blanco, (400,100), (400,550), 6)
            pygame.draw.line(ventana, c_blanco, (450,100), (450,550), 2)
            pygame.draw.line(ventana, c_blanco, (500,100), (500,550), 2)
            pygame.draw.line(ventana, c_blanco, (550,100), (550,550), 2)     
            dif2 = fuente3.render(dif,True, c_negro, None)
            actnumber = fuente3.render(str(ac), True, c_negro, None)
            ventana.blit(dif2,(5,600))
            ventana.blit(actnumber,(40,100))    
            drawSudoku(Svacio2)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_BACKSPACE:
                        Jugar = False
                        Menu = True
                if event.type == KEYDOWN:
                    if event.key == K_f:
                        Svacio2 = SudokuGenerator.fullSudoku(1)
                        dif = "Dificultad: Facil"
                        default = defaultNumbers(Svacio2)
                    if event.key == K_m:
                        Svacio2 = SudokuGenerator.fullSudoku(2)
                        dif = "Dificultad: Intermedia"   
                        default = defaultNumbers(Svacio2)
                    if event.key == K_d:
                        Svacio2 = SudokuGenerator.fullSudoku(3)
                        dif = "Dificultad: Dificil"
                        default = defaultNumbers(Svacio2)

                if event.type == KEYDOWN:
                    if event.key == K_0:
                        ac = "X"
                if event.type == KEYDOWN:                        
                    if event.key == K_1:
                        ac = 1
                if event.type == KEYDOWN:
                    if event.key == K_2:
                        ac = 2
                if event.type == KEYDOWN:
                    if event.key == K_3:
                        ac = 3
                if event.type == KEYDOWN:
                    if event.key == K_4:
                        ac = 4
                if event.type == KEYDOWN:
                    if event.key == K_5:
                        ac = 5
                if event.type == KEYDOWN:
                    if event.key == K_6:
                        ac = 6
                if event.type == KEYDOWN:
                    if event.key == K_7:
                        ac = 7
                if event.type == KEYDOWN:
                    if event.key == K_8:
                        ac = 8
                if event.type == KEYDOWN:
                    if event.key == K_9:
                        ac = 9
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        if SudokuBacktracking.isCorrectSolved(Svacio2):
                            dif = "Sudoku Completado"
                        else:
                            dif = "Sudoku Incompleto/Incorrecto"
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        SudokuBacktracking.Backtracking(Svacio2)
                        dif = "Sudoku Resuelto"
                            
                if event.type == MOUSEBUTTONDOWN:
                    c1,r1 = pygame.mouse.get_pos()
                    tup = (c1,r1)
                    if not SudokuBacktracking.isCorrectSolved(Svacio2):
                        ChangeNumber.changeNum(Svacio2, c1, r1, ac)
                        
            pygame.display.flip()

#BEG OF EXE

main()
