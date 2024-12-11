def cantidad_carne (n, m, k):
    gallinas = n * 6
    gallos = m * 7
    pollitos = k * 1
    return gallinas, gallos, pollitos

if __name__ == "__main__":
    n = int(input("Ingresa la cantidad de gallinas: "))
    m = int(input("Ingresa la cantidad de gallos: "))
    k = int(input("Ingresa la cantidad de pollitos: "))

    kilos_carne = cantidad_carne (n, m, k)

    gallinas, gallos, pollitos = kilos_carne

    print("Hay " + str(gallinas) + " kilos de carne de gallina")
    print("Hay " + str(gallos) + " kilos de carne de gallo")
    print("Hay " + str(pollitos) + " kilos de carne de pollitos")