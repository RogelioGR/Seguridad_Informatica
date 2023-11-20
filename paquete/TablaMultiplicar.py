def TablaMultiplicar():
    inicio_rango = int(input ("ingresa un numero de inicio"))
    final_rango  = int(input ("ingresa un numero de final"))
    inicio_tabla = int(input ("ingresa un numero de inicio tabla"))
    final_tabla = int(input ("ingresa un numero de final tabla"))

    for i in range(inicio_rango,final_rango + 1):
        print()
        for b in range (inicio_tabla,final_tabla + 1,1):
            resultado= i * b
            
            print(i,"x",b,"=",resultado)