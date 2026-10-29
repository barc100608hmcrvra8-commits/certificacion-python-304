#realizar un programa que calcule
#la compra total de 4 productos, si la compra total es
#mayor a 2000 me haga un descuento 
#del 10%
#datos de entradaa 
p1 = float(input("introduce el precio del producto 1: "))
p2 = float(input("introduce el precio del producto 2: "))
p3 = float(input("introduce el precio del producto 3: "))
p4 = float(input("introduce el precio del producto 4: "))
#proceso 
t = p1+p2+p3+p4
if t > 2000:
    d = t-(t*0.10)
    print("TIENES DESCUENTO")
    print("tu total final es de:",d)
else:
    print("no tienes descuento")
    print("tu total final es:",t)