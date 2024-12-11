def interes_c (p, i, n,):
    prestamo = p * (1 + ((i/100) / 12)) ** (n)
    return prestamo

if __name__ =="__main__":
    p = float(input("Ingrese el valor del prestamo: "))
    i = float(input("Ingrese la tasa de interes: "))
    n = float(input("Ingresa la cantidad de meses proyectada para el pago del prestamo: "))

    total = interes_c(p, i, n)

    print(f"El valor final del prestamo sera de {total:.2f}")