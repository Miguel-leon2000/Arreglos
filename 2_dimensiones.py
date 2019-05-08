Matriz = [

    [1, 2, 3, 4, 5, 6, 7],
    [8, 9, 10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19, 20, 21],
    [22, 23, 24, 25, 26, 27, 28],
    [29, 30, 31, 32, 33, 34, 35],
    [36, 37, 38, 39, 40, 41, 42],
    [43, 44, 45, 46, 47, 48, 49]

    ]

# print(len(Matriz))
# print(len(Matriz[0]))
# print(len(Matriz[0][0]))

print("-----------Arriba-Abajo / Izquierda-Derecha--------------------------")
for f in range(0, len(Matriz)):
    for c in range(0, len(Matriz[f])):
        print(Matriz[f][c], "\t", end="")
    print("\n")

print("-----------Arriba-Abajo / Derecha-Izquierda---------------------------")
for f in range(0, len(Matriz)):
    for c in range(len(Matriz[f]) - 1, -1, -1):
        print(Matriz[f][c], "\t", end="")
    print("\n")

print("-----------Abajo-Arriba / Izquierda-Derecha---------------------------")
for f in range(len(Matriz) - 1, -1, -1):
    for c in range(len(Matriz[f])):
        print(Matriz[f][c], "\t", end="")
    print("\n")


print("-----------Abajo-Arriba / Derecha-Izquierda---------------------------")
for f in range(len(Matriz) - 1, -1, -1):
    for c in range(len(Matriz[f]) - 1, -1, -1):
        print(Matriz[f][c], "\t", end="")
    print("\n")

print("-----------------------Rotar------------------------------------------")
for f in range(0, len(Matriz)):
    for c in range(0, len(Matriz[f])):
        print(Matriz[c][f], "\t", end="")
    print("\n")
