def calculator(dias,hora,minutos,segundos):
    global resultado
    hora += dias * 24
    minutos += hora * 60
    segundos += minutos * 60
    resultado = segundos
    return resultado
resultado = 0
a = int(input("Introduzca un nº de días "))
b = int(input("Introduzca un nº de horas "))
c = int(input("Introduzca un nº de minutos "))
d = int(input("Introduzca un nº de segundos "))
calculator(a,b,c,d)
print(f"{a} días, {b} horas, {c} minutos, y {d} segundos, es igual a {resultado}")