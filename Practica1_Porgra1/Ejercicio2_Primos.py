Primo = 0
print("Ingrese un numero: ")
Numero = int(input())
Digitos = []
while Numero > 0:
    Digitos.append(Numero % 10)
    Numero = Numero // 10
for i in range(len(Digitos)):
    match Digitos[i]:
        case 0 | 1: Primo += 0
        case 2 | 3 | 5 | 7: Primo += 1 
        case _: Primo += 0
print("Cantidad de digitos primos:", Primo)