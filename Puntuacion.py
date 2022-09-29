puntos = float(input("Ingrese su puntuación:"))


if puntos <0.0 or puntos > 1.0:
    print("Fuera de Rango")
else:
    if puntos > 0.9:
        print("Su puntuación es Sobresaliente")
    elif puntos >= 0.8 and puntos < 0.9:
        print("Su puntuación es Notable")
    elif puntos >= 0.7 and puntos < 0.8:
        print("Su puntuación es Buena")
    elif puntos >= 0.6 and puntos < 0.7:
        print("Su puntuación es Satisfactoria")
    else:
        print("Su puntuación es Insuficiente")