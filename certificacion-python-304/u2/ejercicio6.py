t = [
    ["nombre","edad","[calificacion]"],
    ["emily",16,9.0],
    ["leonel",15,6.7],
    ["america",15,6.7],
    ["michel",16,6.0],
    ["sdana",16,8.0],
    ["brian",16,6.7],
    ["kimberli",16,8.5]
]
n = input("ingresa un nombre: ")
f = len(t)
c = len(t[0])

for i in range(f): 
    for j in range(c):
        if t[i][j]== n :
            print(f"nombre en la posicion la pocicion [{i}][{j}]")
            