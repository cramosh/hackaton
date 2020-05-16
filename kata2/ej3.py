edad_cliente = int(input("¿Cual es tu edad? "))

if edad_cliente < 4:
    print("Entrada Gratuita")
elif 4 <= edad_cliente <= 18:#Equivale a edad_cliente >= 4 and edad_cliente <=18 
    print("Precio Entrada es 5€")
else:
    print("Precio Entrada es 10€")