Cont = 0
Positivo = 0
Negativo = 0
Cero = 0
while Cont < 3:
    print("Ingrese un numero: ");
    numero = float(input())
    if numero > 0:
        Positivo += 1
    elif numero < 0:
        Negativo += 1
    else:
        Cero += 1
    Cont += 1
print("Cantidad de numeros positivos:", Positivo)
print("Cantidad de numeros negativos:", Negativo)
print("Cantidad de ceros:", Cero)