def changeNum(Svacio, c1, r1, ac):
    """Funcion que permite cambiar los numeros del Sudoku en pygame"""
    """Cambia los numeros en la primera fila"""
    if (100 < c1 and c1 < 150) and (100 < r1 and r1 < 150):
        Svacio[0][0] = ac
    if (150 < c1 and c1 < 200) and (100 < r1 and r1 < 150):
        Svacio[0][1] = ac
    if (200 < c1 and c1 < 250) and (100 < r1 and r1 < 150):
        Svacio[0][2] = ac
    if (250 < c1 and c1 < 300) and (100 < r1 and r1 < 150):
        Svacio[0][3] = ac
    if (300 < c1 and c1 < 350) and (100 < r1 and r1 < 150):
        Svacio[0][4] = ac
    if (350 < c1 and c1 < 400) and (100 < r1 and r1 < 150):
        Svacio[0][5] = ac
    if (400 < c1 and c1 < 450) and (100 < r1 and r1 < 150):
        Svacio[0][6] = ac
    if (450 < c1 and c1 < 500) and (100 < r1 and r1 < 150):
        Svacio[0][7] = ac
    if (500 < c1 and c1 < 550) and (100 < r1 and r1 < 150):
        Svacio[0][8] = ac
    """Cambia los numeros de la segunda fila"""
    if (100 < c1 and c1 < 150) and (150 < r1 and r1 < 200):
        Svacio[1][0] = ac       
    if (150 < c1 and c1 < 200) and (150 < r1 and r1 < 200):
        Svacio[1][1] = ac
    if (200 < c1 and c1 < 250) and (150 < r1 and r1 < 200):
        Svacio[1][2] = ac
    if (250 < c1 and c1 < 300) and (150 < r1 and r1 < 200):
        Svacio[1][3] = ac
    if (300 < c1 and c1 < 350) and (150 < r1 and r1 < 200):
        Svacio[1][4] = ac
    if (350 < c1 and c1 < 400) and (150 < r1 and r1 < 200):
        Svacio[1][5] = ac
    if (400 < c1 and c1 < 450) and (150 < r1 and r1 < 200):
        Svacio[1][6] = ac
    if (450 < c1 and c1 < 500) and (150 < r1 and r1 < 200):
        Svacio[1][7] = ac
    if (500 < c1 and c1 < 550) and (150 < r1 and r1 < 200):
        Svacio[1][8] = ac
    """Cambia los numeros de la tercera fila"""
    if (100 < c1 and c1 < 150) and (200 < r1 and r1 < 250):
        Svacio[2][0] = ac       
    if (150 < c1 and c1 < 200) and (200 < r1 and r1 < 250):
        Svacio[2][1] = ac
    if (200 < c1 and c1 < 250) and (200 < r1 and r1 < 250):
        Svacio[2][2] = ac
    if (250 < c1 and c1 < 300) and (200 < r1 and r1 < 250):
        Svacio[2][3] = ac
    if (300 < c1 and c1 < 350) and (200 < r1 and r1 < 250):
        Svacio[2][4] = ac
    if (350 < c1 and c1 < 400) and (200 < r1 and r1 < 250):
        Svacio[2][5] = ac
    if (400 < c1 and c1 < 450) and (200 < r1 and r1 < 250):
        Svacio[2][6] = ac
    if (450 < c1 and c1 < 500) and (200 < r1 and r1 < 250):
        Svacio[2][7] = ac
    if (500 < c1 and c1 < 550) and (200 < r1 and r1 < 250):
        Svacio[2][8] = ac
    """Cambia los numeros de la cuarta fila"""
    if (100 < c1 and c1 < 150) and (250 < r1 and r1 < 300):
        Svacio[3][0] = ac       
    if (150 < c1 and c1 < 200) and (250 < r1 and r1 < 300):
        Svacio[3][1] = ac
    if (200 < c1 and c1 < 250) and (250 < r1 and r1 < 300):
        Svacio[3][2] = ac
    if (250 < c1 and c1 < 300) and (250 < r1 and r1 < 300):
        Svacio[3][3] = ac
    if (300 < c1 and c1 < 350) and (250 < r1 and r1 < 300):
        Svacio[3][4] = ac
    if (350 < c1 and c1 < 400) and (250 < r1 and r1 < 300):
        Svacio[3][5] = ac
    if (400 < c1 and c1 < 450) and (250 < r1 and r1 < 300):
        Svacio[3][6] = ac
    if (450 < c1 and c1 < 500) and (250 < r1 and r1 < 300):
        Svacio[3][7] = ac
    if (500 < c1 and c1 < 550) and (250 < r1 and r1 < 300):
        Svacio[3][8] = ac
    """Cambia los numeros de la quinta fila"""
    if (100 < c1 and c1 < 150) and (300 < r1 and r1 < 350):
        Svacio[4][0] = ac       
    if (150 < c1 and c1 < 200) and (300 < r1 and r1 < 350):
        Svacio[4][1] = ac
    if (200 < c1 and c1 < 250) and (300 < r1 and r1 < 350):
        Svacio[4][2] = ac
    if (250 < c1 and c1 < 300) and (300 < r1 and r1 < 350):
        Svacio[4][3] = ac
    if (300 < c1 and c1 < 350) and (300 < r1 and r1 < 350):
        Svacio[4][4] = ac
    if (350 < c1 and c1 < 400) and (300 < r1 and r1 < 350):
        Svacio[4][5] = ac
    if (400 < c1 and c1 < 450) and (300 < r1 and r1 < 350):
        Svacio[4][6] = ac
    if (450 < c1 and c1 < 500) and (300 < r1 and r1 < 350):
        Svacio[4][7] = ac
    if (500 < c1 and c1 < 550) and (300 < r1 and r1 < 350):
        Svacio[4][8] = ac
    """Cambia los numeros de la sexta fila"""
    if (100 < c1 and c1 < 150) and (350 < r1 and r1 < 400):
        Svacio[5][0] = ac       
    if (150 < c1 and c1 < 200) and (350 < r1 and r1 < 400):
        Svacio[5][1] = ac
    if (200 < c1 and c1 < 250) and (350 < r1 and r1 < 400):
        Svacio[5][2] = ac
    if (250 < c1 and c1 < 300) and (350 < r1 and r1 < 400):
        Svacio[5][3] = ac
    if (300 < c1 and c1 < 350) and (350 < r1 and r1 < 400):
        Svacio[5][4] = ac
    if (350 < c1 and c1 < 400) and (350 < r1 and r1 < 400):
        Svacio[5][5] = ac
    if (400 < c1 and c1 < 450) and (350 < r1 and r1 < 400):
        Svacio[5][6] = ac
    if (450 < c1 and c1 < 500) and (350 < r1 and r1 < 400):
        Svacio[5][7] = ac
    if (500 < c1 and c1 < 550) and (350 < r1 and r1 < 400):
        Svacio[5][8] = ac
    """Cambia los numeros de la septima fila"""
    if (100 < c1 and c1 < 150) and (400 < r1 and r1 < 450):
        Svacio[6][0] = ac       
    if (150 < c1 and c1 < 200) and (400 < r1 and r1 < 450):
        Svacio[6][1] = ac
    if (200 < c1 and c1 < 250) and (400 < r1 and r1 < 450):
        Svacio[6][2] = ac
    if (250 < c1 and c1 < 300) and (400 < r1 and r1 < 450):
        Svacio[6][3] = ac
    if (300 < c1 and c1 < 350) and (400 < r1 and r1 < 450):
        Svacio[6][4] = ac
    if (350 < c1 and c1 < 400) and (400 < r1 and r1 < 450):
        Svacio[6][5] = ac
    if (400 < c1 and c1 < 450) and (400 < r1 and r1 < 450):
        Svacio[6][6] = ac
    if (450 < c1 and c1 < 500) and (400 < r1 and r1 < 450):
        Svacio[6][7] = ac
    if (500 < c1 and c1 < 550) and (400 < r1 and r1 < 450):
        Svacio[6][8] = ac
    """Cambia los numeros de la octava fila"""
    if (100 < c1 and c1 < 150) and (450 < r1 and r1 < 500):
        Svacio[7][0] = ac       
    if (150 < c1 and c1 < 200) and (450 < r1 and r1 < 500):
        Svacio[7][1] = ac
    if (200 < c1 and c1 < 250) and (450 < r1 and r1 < 500):
        Svacio[7][2] = ac
    if (250 < c1 and c1 < 300) and (450 < r1 and r1 < 500):
        Svacio[7][3] = ac
    if (300 < c1 and c1 < 350) and (450 < r1 and r1 < 500):
        Svacio[7][4] = ac
    if (350 < c1 and c1 < 400) and (450 < r1 and r1 < 500):
        Svacio[7][5] = ac
    if (400 < c1 and c1 < 450) and (450 < r1 and r1 < 500):
        Svacio[7][6] = ac
    if (450 < c1 and c1 < 500) and (450 < r1 and r1 < 500):
        Svacio[7][7] = ac
    if (500 < c1 and c1 < 550) and (450 < r1 and r1 < 500):
        Svacio[7][8] = ac
    """Cambia los numeros de la novena fila"""
    if (100 < c1 and c1 < 150) and (500 < r1 and r1 < 550):
        Svacio[8][0] = ac       
    if (150 < c1 and c1 < 200) and (500 < r1 and r1 < 550):
        Svacio[8][1] = ac
    if (200 < c1 and c1 < 250) and (500 < r1 and r1 < 550):
        Svacio[8][2] = ac
    if (250 < c1 and c1 < 300) and (500 < r1 and r1 < 550):
        Svacio[8][3] = ac
    if (300 < c1 and c1 < 350) and (500 < r1 and r1 < 550):
        Svacio[8][4] = ac
    if (350 < c1 and c1 < 400) and (500 < r1 and r1 < 550):
        Svacio[8][5] = ac
    if (400 < c1 and c1 < 450) and (500 < r1 and r1 < 550):
        Svacio[8][6] = ac
    if (450 < c1 and c1 < 500) and (500 < r1 and r1 < 550):
        Svacio[8][7] = ac
    if (500 < c1 and c1 < 550) and (500 < r1 and r1 < 550):
        Svacio[8][8] = ac


        
        