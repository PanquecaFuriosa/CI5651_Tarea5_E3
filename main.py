import copy

def estado_ganador(tablero):
    for i in range(3):
        if ((tablero[i] == ['+']*3) or \
            ([tablero[j][i] for j in range(3)] == ['+']*3)):
            return True

    if (([tablero[i][i] for i in range(3)] == ['+']*3) or \
        ([tablero[i][2-i] for i in range(3)] == ['+']*3)):
        return True

    return False

def eval(w, jugador):
    if ((jugador == '-') and (estado_ganador(w))):
        return 10

    if ((jugador == '|') and (estado_ganador(w))):
        return -10

    return 0

def sucesores(w, jugador, ultima_jugada):
    sucesores = []

    for i in range(3):
        for j in range(3):
            if (w[i][j] == '' and (i, j) != ultima_jugada):
                sucesor = copy.deepcopy(w)
                sucesor[i][j] = jugador
                sucesores.append((sucesor, (i, j)))
            if (jugador == '|' and w[i][j] == '-' and (i, j) != ultima_jugada):
                sucesor = copy.deepcopy(w)
                sucesor[i][j] = '+'
                sucesores.append((sucesor, (i, j)))
            if (jugador == '-' and w[i][j] == '|' and (i, j) != ultima_jugada):
                sucesor = copy.deepcopy(w)
                sucesor[i][j] = '+'
                sucesores.append((sucesor, (i, j)))

    return sucesores

def primero(w, n, ultima_jugada):
    if ((n == 0) or (not sucesores(w, '-', ultima_jugada))):
        return eval(w, '-')

    mejor = float('-inf')
    for x, jugada in sucesores(w, '-', ultima_jugada):
        mejor = max(mejor, segundo(x, n - 1, jugada))

    return mejor

def segundo(w, n, ultima_jugada):
    if ((n == 0) or (not sucesores(w, '|', ultima_jugada))):
        return eval(w, '|')

    mejor = float('inf')
    for x, jugada in sucesores(w, '|', ultima_jugada):
        mejor = min(mejor, primero(x, n - 1, jugada))
        
    return mejor
