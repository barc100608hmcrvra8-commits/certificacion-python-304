#cadenas y concanetacion con (+)
c1='hola '
c2='mundo '
m="""Esto es una cadena 
de varias lineas"""
print(c1+c2+m)
#cadenas y repiticion
e='ja'*3
print(e)
#cambiar la cadena de m a M
n='yoe'
print(n.upper())
#cambiar la cadena de M a m
print(n.lower())
#remplazar texto en una cadena
f='me gusta programacion'
print(f.replace('programacion','matematicas'))
#formato de cadena (f-strng)
edad = 16
nombre ='yoe'
mensaje = f"""hola, me llamo 
{nombre}
tengo {edad} años"""
print(mensaje)
#contar caracteres
t='¡felicidades por aun continuar en el CECY!!!                       '
cc=len(t)
print(cc)
#comprobar si untexto tien una palabra 
oracion= "aprender pyrhon es divertido"
if "hola" in oracion:
    print("encontrado")
else:
    print("no esta")
#olviar esta cadena
nl = "2"

print(nl.isalpha())
print(nl.isdigit())
