"""
CREAR UN PROGRAMA DONDE PASAR UN NUMERO Y DEVUELVA TU TABLA DE MULTIPLICAR
"""

num = int(input("Indica un numero "))
cont = 1
for i in range(10):
    print("%s * %s = %s" % (str(num), str(cont) ,str(num*cont)))
    cont+=1