#creando un diccionario 
p={
    "nombre":"yoe",
    "edad":16,
    "profecion":"localizador",
    "estudiante":True
}
print(p)
#accediendo a un vaor especifico
print(p["nombre"])
#se puede usar el metodo get()
#no marca error si no existe el valor
print(p.get("edad"))
#odificar un valor existente 
p["nombre"]="yoerengues"
print(p["nombre"])
p["dnd vivo"]="en mi puente"
print(p)