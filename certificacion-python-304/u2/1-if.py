try:

    p=float(input("ingresa el promedio "))

    if p < 0:
        print("ese promedio no exite")   
    elif p <= 5:
        print("tu promedio es muy bajo")
    
    elif p >= 6 and p <= 7:
        print("tu promedio es bajo")
    elif p >7 and p<=9:
        print("tu promedio es bueno ")
    elif p > 10:
        print("ingresa un promedio menor a 10")
    else:
        print("tu pormedio es exelente")
except ValueError:
    print("ingresa solo numeros")