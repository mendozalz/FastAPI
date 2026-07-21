# Uso de funciones normales vs lambda

# FUNCIONES NORMALES
# def retornar_edad(programadores):
#     return programadores[1]

# lista_programadores = [
#     ("Lenin", 46),
#     ("Victor", 41),
#     ("Che", 18)
# ]

# lista_ordenada = sorted(lista_programadores,key=retornar_edad, reverse=False)

# print(lista_ordenada)
#print(lista_programadores[2])

#/*********************************/

# FURNCIONES LAMBDA O ANONIMAS


lista_programadores = [
    ("Lenin", 46),
    ("Victor", 41),
    ("Che", 18)
]

# def retornar_edad(programadores):
#     return programadores[1]

var_lambda = lambda programadores:programadores[1]

lista_ordenada = sorted(lista_programadores,key=var_lambda, reverse=True)

print(lista_ordenada)