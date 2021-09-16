num = int(input("Ingrese un número: "))  # Entrada y Salida de Datos E/S
if num > 1:  # Salto Condicional
    cont = 0  # Transferencia de Datos
    for i in range(2, num):  # Salto Incondicional
        resto = num % i  # Aritmético - Lógicas
        # Entrada y Salida de Datos E/S
        print("{} % {} = {} ".format(num, i, resto))
        if resto == 0:  # Salto Condicional
            cont += 1  # Aritmético - Lógicas
    if cont == 0:  # Salto Condicional
        # Entrada y Salida de Datos E/S
        print("El {} es un número primo".format(num))
    else:
        # Entrada y Salida de Datos E/S
        print("El {} no es un número primo".format(num))

else:
    # Entrada y Salida de Datos E/S
    print("El {} no es un número primo".format(num))
