#declarando lisita
try:
    materias=["matematicas","filosofia","programacion","ingles"]
    print(materias[int(input("ingresa el indice: "))])
    materias.append("lengua y comunicacion")
    print(materias)
    materias[1]="biologia"
    print(materias)
    materias.remove("ingles")
    print(materias)
except IndexError:
    print(" ese indice no existe no llevas esa materia")
