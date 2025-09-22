# ------------------------------------------
# Función para calcular el descuento
# ------------------------------------------
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto de descuento a partir del monto total de la compra.

    :param monto_total: float. Total de la compra.
    :param porcentaje_descuento: float. Porcentaje de descuento (por defecto 10%).
    :return: float. Monto del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# ------------------------------------------
# Programa principal
# ------------------------------------------
if __name__ == "__main__":
    # 1️⃣ Llamada usando el porcentaje por defecto (10%)
    monto1 = 100.0
    descuento1 = calcular_descuento(monto1)
    total1 = monto1 - descuento1
    print(f"Compra 1:\n  Monto original: ${monto1:.2f}")
    print(f"  Descuento (10%): ${descuento1:.2f}")
    print(f"  Total a pagar : ${total1:.2f}\n")

    # 2️⃣ Llamada indicando un porcentaje de descuento diferente (por ejemplo 20%)
    monto2 = 250.0
    descuento2 = calcular_descuento(monto2, 20)
    total2 = monto2 - descuento2
    print(f"Compra 2:\n  Monto original: ${monto2:.2f}")
    print(f"  Descuento (20%): ${descuento2:.2f}")
    print(f"  Total a pagar : ${total2:.2f}")
