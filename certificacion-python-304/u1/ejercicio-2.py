try:
    alumnos=["leonel","michel","braymr","emily","america"]
    calificaciones=[6.7,6,7,8,9]
    print("alumno:",alumnos[2],"calificacion:",calificaciones[2])
    print("alumno:",alumnos[4],"calificacion:",calificaciones[4])
    
except IndexError:
    print("no se encontro el alumno y/o la calificacion")

