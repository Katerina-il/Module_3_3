def print_params(a = 1, b = 'строка', c = True):

    print(a, b, c) #функцию print_params(a = 1, b = 'строка', c = True), которая принимает три параметра со значениями по умолчанию (например сейчас это: 1, 'строка', True).


print_params()

print_params(b=25)

print_params(c = [1,2,3])



values_list = [5, "list number one", 4.34]

print_params(*values_list)

values_dict ={'a': 34, 'b':'beta', 'c': 56.8}

print_params(**values_dict) #Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря).

values_list_2 = ["example", 23]

print_params(*values_list_2, 42) # Проверьте, работает ли print_params(*values_list_2, 42)