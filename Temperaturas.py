def calcular_media_temperaturas(registro_ciudades):
    """
    Calcula la temperatura media de cada ciudad a partir de sus registros semanales.

    Parámetros:
        registro_ciudades (dict): Diccionario donde las llaves son los nombres de las ciudades
                                  y los valores son listas con temperaturas registradas.
    Retorna:
        dict: Diccionario con la temperatura media de cada ciudad.
    """
    medias_por_ciudad = {}

    # Recorremos cada ciudad para obtener su promedio
    for nombre_ciudad, lista_temperaturas in registro_ciudades.items():
        media = sum(lista_temperaturas) / len(lista_temperaturas)
        medias_por_ciudad[nombre_ciudad] = media

    return medias_por_ciudad


# Diccionario con las ciudades ecuatorianas y sus temperaturas (ejemplo de 4 semanas)
temperaturas_ecuador = {
    "Quito": [18, 19, 20, 17],
    "Guayaquil": [28, 30, 29, 31],
    "Cuenca": [15, 16, 17, 14],
    "Guaranda": [12, 13, 14, 12]
}

# Llamada a la función para obtener la media de cada ciudad
promedios = calcular_media_temperaturas(temperaturas_ecuador)

# Presentación de resultados
print("Promedio de temperaturas por ciudad (°C):")
for ciudad, promedio in promedios.items():
    print(f"{ciudad}: {promedio:.2f} °C")
