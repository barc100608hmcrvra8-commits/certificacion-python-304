try:
    n1=float(input("ingresa el primer numero: "))
    n2=float(input("ingresa el segundo numero: "))
    r=n1/n2
except ValueError:
    print("solo introduce numeros")
except ZeroDivisionError:
    print("no se puede dividir entre cero")
else:
    print("el resultado es: ",r)
finally:
    print("programa finalizadao")