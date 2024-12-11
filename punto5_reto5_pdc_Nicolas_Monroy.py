import math


def inicio_promedio (val_1, val_2, val_3, val_4, val_5):
    total_prom = (val_1 + val_2 + val_3 + val_4 + val_5) / 5
    return total_prom

def inicio_promedio_mult (val_1, val_2, val_3, val_4, val_5):
    total_prom_mult = (val_1 * val_2 * val_3 * val_4 * val_5) ** (1 / 5)
    return total_prom_mult

def inicio_potencia (val_1, val_2, val_3, val_4, val_5):
    mayor = max (val_1, val_2, val_3, val_4, val_5)
    menor = min (val_1, val_2, val_3, val_4, val_5)
    total_potencia = mayor ** menor
    return total_potencia
    
def inicio_raiz (val_1, val_2, val_3, val_4, val_5):
    menor_r = min (val_1, val_2, val_3, val_4, val_5)
    total_raiz = math.cbrt (menor_r)
    return total_raiz

if __name__ == "__main__":
    val_1 = float(input("Ingresa el primer numero: "))
    val_2 = float(input("Ingresa el segundo numero: "))
    val_3 = float(input("Ingresa el tercer numero: "))
    val_4 = float(input("Ingresa el cuarto numero: "))
    val_5 = float(input("Ingresa el quinto numero: "))
    
    promedio = inicio_promedio (val_1, val_2, val_3, val_4, val_5)
    prom_mult = inicio_promedio_mult (val_1, val_2, val_3, val_4, val_5)
    potencia = inicio_potencia (val_1, val_2, val_3, val_4, val_5)
    raiz = inicio_raiz (val_1, val_2, val_3, val_4, val_5)

    print (f"El promedio de los 5 numeros es: {promedio}")
    print (f"El promedio multiplicativo de los 5 numeros es: {prom_mult:.2f}")
    print (f"La potencia del mayor elevado al menor numero es: {potencia}")
    print (f"La raiz cubica del menor numero es: {raiz}")