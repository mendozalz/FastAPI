# num_list = [1,2,3,4,5,6,7,8,9,0]

# par_lambda = lambda x:x%2==0

# return_par = list(filter(par_lambda, num_list))

# print(return_par)

nombres = ["Alice", "Bob", "Anna", "David", "Amelia", "Charlie" ]

# def retunr_nom_a(nombre):
#     return nombre[1][0]

retunr_nom_a = lambda x:x[0][0] == "A"

return_filter = list(filter(retunr_nom_a, nombres))

#print(return_nom_a(nombres))
print(return_filter)