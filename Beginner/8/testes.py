# Dedicado a testes

# Trocando caracteres em strings
comida = "comida"
objeto = "objeto"

# Método 1
# comida2 = list(comida)
# comida2[0] = objeto[2]
# comida = ''.join(comida2)
# print(comida)

# Método 2
# comida = comida.replace(comida[0], objeto[2])
# print(comida)

for i in comida:
    print(i)