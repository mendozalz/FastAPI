lista_frutas = ['guineo', 'manzana', 'uva']
sufix = '----fruta***'

# def add_sufix(fruta):
#     return f"{fruta}{sufix}"

agregar_sufix = lambda x:f"{sufix}{x}"

#lista_frutas_sufix = list(map(add_sufix,lista_frutas))

lista_frutas_sufix = list(map(agregar_sufix,lista_frutas))

print(lista_frutas_sufix)