print("Ingrese cualquier numero real:")
x = float(input())
if x < 0:
    f = x ** 2
elif x >= 0 and x <= 10:
    f = 2 * x + 1
else:
    f = 3 * x - 1
print("El resultado de la funcion es:", f)