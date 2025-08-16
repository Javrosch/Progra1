Cadena = ""
Lista_Binario = []
print("Ingrese un numero entereo positivo")
Numero = int(input())
while Numero > 0:
    Comodin = Numero % 2
    Lista_Binario.append(Comodin)
    Numero = Numero // 2
i = len(Lista_Binario) - 1
while i >= 0:
    Cadena += str(Lista_Binario[i])
    i -= 1
print("El numero en binario es:", Cadena)