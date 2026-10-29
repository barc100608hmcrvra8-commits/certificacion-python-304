#creando una matriz
n = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
#numero de filas 
#f = len(n)#filas = 3
#numero de columnas 
#c = len(n[0])
#ciclo externo para los indicecs de las filas 
for i in range(0,3):
    #ciclo interno para los indices de las columnas()
    for j in range(0,3):
        print(f"[{i}][{j}]={n[i][j]}")