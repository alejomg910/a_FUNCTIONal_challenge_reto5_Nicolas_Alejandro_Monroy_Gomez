import math

def calculo_rectangulo (b, a):
    area_rect = (b * a)
    perimetro_rect = (2 * b) + (2 * a)
    return area_rect, perimetro_rect

def calculo_circulo (r):
    area_circ = math.pi * r ** 2
    perimetro_circ = 2 * math.pi * r
    return area_circ, perimetro_circ

if __name__ == "__main__":
    b = float(input("Ingresa el largo del rectangulo: "))
    a = float(input("Ingresa el ancho del rectangulo: "))
    r = float(input("Ingresa el radio de la circunferencia: "))
    
    resultado_rectangulo = calculo_rectangulo(b, a)
    resultado_circulo = calculo_circulo (r)

    area_rect, perimetro_rect = resultado_rectangulo
    area_circ, perimetro_circ = resultado_circulo
    
    perimetro_figura = perimetro_rect + (perimetro_circ * 2)
    area_figura = area_rect + (area_circ * 2)

    print(f"El area del rectangulo es: {area_rect:.3f}")
    print(f"El area de un solo circulo es: {area_circ:3f}")
    print(f"El area total de la figura es: {area_figura:.3f}")
    
    print(f"El perimetro del rectangulo es: {perimetro_rect:.3f}")
    print(f"El perimetro de un solo circulo es: {perimetro_circ:3f}")
    print(f"El perimetro total de la figura es: {perimetro_figura:.3f}")