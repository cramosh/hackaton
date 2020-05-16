pan_dia = 3.49
desc_perc = 40 
desc = round(pan_dia * ((desc_perc or 0.0) / 100.0))
pan_no_dia = pan_dia - desc
barras = int(input("¿Cuantas barras de pan no frescas?"))
total = round(barras * pan_no_dia, 2)

resultado = "La barra fresca vale %s €, descuento por no ser fresca %s %%. \
Total: %s €" % (pan_dia,desc_perc,total)

print(resultado)