a = [
    ["a","b","c","d","e","f","g",],
    ["h","i","j","k","l","ll","m"],
    ["n","ñ","o","p","q","r","s"],
    ["t","u","v","w","x","y","z"]
]
for i in range(0,4):
    #ciclo interno para los indices de las columnas()
    for j in range(0,7):
        print(f"[{i}][{j}]={a[i][j]}")
