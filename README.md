Código del ejercicio 3 de la tarea 5 de la materia CI5651 - Diseño de algoritmos I

Considere un modificación del clásico juego de la vieja, en donde:
• El primer jugador juega con – y el segundo juega con |.
• Cada casilla puede tener alguno de estos símbolos, ninguno o ambos (en cuyo caso se forma un +).
• En cada turno, el jugador no puede jugar en la misma casilla que el jugador anterior.
• Gana aquel jugador que logre formar tres + en una misma fila, columna o diagonal.
Por ejemplo, la siguiente es una configuración ganadora (donde la última jugada fue de |):

+ + +
| – +
–   |

Diga si hay una estrategia ganadora para alguno de los jugadores involucrados.
Para resolver este problema, utilice el método minmax.
