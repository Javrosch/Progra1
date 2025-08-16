Suma = 0
contador_lista = 0
cuadrados = 0
contador_mayor = 0
Lista_Sueldos = []
Cont = 0
print("Ingrese el sueldo de los empleados (0 para terminar):")
while Cont == 0:
    Sueldo = float(input())
    if Sueldo == 0:
        Cont = 1
    else:
        Lista_Sueldos.append(Sueldo)
for i in range(len(Lista_Sueldos)):
    Suma += Lista_Sueldos[i]
    contador_lista += 1    
Promedio = Suma / contador_lista
for i in range(len(Lista_Sueldos)):
    if Lista_Sueldos[i] > Promedio:
        contador_mayor += 1
for i in range(len(Lista_Sueldos)):
    Resta = Lista_Sueldos[i] - Promedio
    cuadrado = Resta ** 2
    cuadrados += cuadrado
Varianza = cuadrados / contador_lista
Desviacion = Varianza ** 0.5
print("El promedio de los sueldos es:", Promedio)
print("Cantidad de sueldos mayores al promedio:", contador_mayor)
print("La desviacion estandar es:", Desviacion)