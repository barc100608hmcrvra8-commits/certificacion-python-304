#sin manejo de exepciones
try:
    n1=float(input("ingresa el numero 1: "))
    n2=float(input("ingresa el numero 2: "))
    r=n1/n2
    print(r)
except ValueError:
    print("no puedes introducir letras")
except ZeroDivisionError:
    print("Error: no se puede dividir entre 0")
