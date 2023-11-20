def palíndromos():
    print("Detector de palíndromos")
    print("Para escriba 'end'")

    while True:
        texto = input("Ingrese la palabra: ")
        if texto.lower() == "salir":
            break
        else:
            def es_palindromo(texto):
                texto = texto.replace(" ", "").lower()
                return texto == texto[::-1]
            if es_palindromo(texto):
                print(f"{texto} es un palíndromo.")
            else:
                print(f"{texto} no es un palíndromo")