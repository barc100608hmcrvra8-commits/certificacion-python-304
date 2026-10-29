#mapa fr tesorp
mapa =[
    [".",".",".","."],
    [".",".","x","."],
    [".",".",".","."],
    [".",".",".","."]
]
f = len(mapa)
c = len(mapa)
#recorrriendo las matrices con siclos anidados
#siclo para manejar filas
for i in range(f):
    #ciclo para columnas 
    for j in range(c):
        if mapa [i][j]=="x":
            print(f"mapa en la posicion la pocicion [{i}][{j}]")