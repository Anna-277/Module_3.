# Функция с параметрами по умолчанию:
def print_params(a = 1, b = 'строка', c = True):
    a = str(a)
    print(print_params)
    return


print_params()
print_params(1, "строка", True)
print_params(b = 25)
print_params(c = [1,2,3])

# Распаковка параметров:
values_list = [17, "мухомор", True]
values_dict = {print_params()}
print(values_dict)