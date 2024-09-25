# 1. Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(1, "строка", True)
print_params(b=25)
print_params(c=[1, 2, 3])

# 2. Распаковка параметров:
def function_print_key_value(**my_dict):
    for key, value in my_dict.items():  # проходим ключом и значением по распакованному словарю
        print(f'key: {key} value: {value}')

values_list = [17, "мухомор", True]
values_dict = {"a": 1, "b": 2, "c": 3}

function_print_key_value(**values_dict)

print_params(*values_list) # передаем распакованный список в функцию
print_params(**values_dict) # передаем распакованный словарь


# 3. Распаковка + отдельные параметры:
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)
