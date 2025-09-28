# Tarea: Trabajando con Diccionarios en Python
# Este script crea un diccionario con información personal ficticia,
# realiza varias operaciones solicitadas (acceder/modificar/añadir/verificar/eliminar)
# y finalmente imprime el diccionario resultante.
# Comentarios en español explicando cada paso.

# 1) Crear el diccionario con las claves requeridas.
informacion_personal = {
    "nombre": "Ana López",
    "edad": 28,
    "ciudad": "Guayaquil",
    # Incluimos 'profesion' inicialmente como un valor temporal para cumplir la instrucción.
    "profesion": "Por asignar"
}

print("Diccionario inicial:")
print(informacion_personal)
print()

# 2) Acceder y modificar el valor asociado con la clave 'ciudad'.
ciudad_actual = informacion_personal["ciudad"]
print(f"Ciudad actual: {ciudad_actual}")

# Modificamos 'ciudad' a otra ciudad (por ejemplo, Quito).
informacion_personal["ciudad"] = "Quito"
print("Se ha modificado la clave 'ciudad' a:", informacion_personal["ciudad"])
print()

# 3) Agregar (o actualizar) la clave-valor que represente la 'profesion'.
# Observación: si 'profesion' ya existe, asignarle un valor nuevo actualiza el registro.
informacion_personal["profesion"] = "Profesor(a) de Matemáticas"
print("Se agregó/actualizó la clave 'profesion':", informacion_personal["profesion"])
print()

# 4) Verificar si la clave 'telefono' existe. Si no, agregarla con un número ficticio.
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "+593 99 123 4567"
    print("Clave 'telefono' no existía; se añadió con el valor:", informacion_personal["telefono"])
else:
    print("La clave 'telefono' ya existe:", informacion_personal["telefono"])
print()

# 5) Eliminar la clave 'edad' (no necesitamos esa información).
# Usamos pop para eliminar y obtener el valor eliminado si se desea.
edad_eliminada = informacion_personal.pop("edad", None)
print("Se eliminó la clave 'edad' con valor:", edad_eliminada)
print()

# 6) Imprimir el diccionario final.
print("Diccionario final:")
print(informacion_personal)
