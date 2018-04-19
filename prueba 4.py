print("Piense un número del 1 al 4")
print("Responda con Si o No a las sigiuentes preguntas")
uno = input("¿Su número es mayor que 2?")
if uno == "si":
    dos = input("¿Su número es mayor que 3?")
    if dos == "si":
        print("Su número es el 4")
    else:
        print("Su número es el 3")
else:
    tres = input("¿Su número es menor que 2?")
    if tres == "si":
        print("Tu número es el 1")
    else:
        print("Tu número es el 2")
print("Gracias por participar")