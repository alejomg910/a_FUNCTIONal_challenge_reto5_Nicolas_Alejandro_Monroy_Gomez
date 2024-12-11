import math

def calculo_esfera (r1):
    volumen_es = (4 / 3) * math.pi * r1 ** 3
    area_superficial_es = 4 * math.pi * r1 ** 2
    return volumen_es, area_superficial_es

def calculo_cono (r2, h):
    volumen_co = (1 / 3) * math.pi * r2**2 * h
    area_superficial_co = math.pi * r2**2 + math.pi * r2 * (math.sqrt (r2**2 + h**2)) # aqui se halla la generatriz por el teorema de Pitagoras.
    return volumen_co, area_superficial_co

if __name__ == "__main__":
    r1 = float(input("Ingrese el radio de la esfera: "))
    r2 = float(input("Ingrese el radio del cono: "))
    h = float(input("Ingresa la altura del cono: "))
    
    resultado_esfera = calculo_esfera (r1)
    resultado_cono = calculo_cono (r2, h)
    
    volumen_es, area_superficial_es = resultado_esfera
    volumen_co, area_superficial_co = resultado_cono
    
    print(f"El volumen de la esfera es: {volumen_es:.3f}")
    print(f"El area superficial de la esfera es: {area_superficial_es:.3f}")
    print(f"El volumen del cono es: {volumen_co:.3f}")
    print(f"El area superficial del cono es: {area_superficial_co:.3f}")