# 1. Создайте пустой словарь my_dict.
my_dict = dict()

# 2. Добавьте ключи и значения в словарь.
my_dict['name'] = "John"
my_dict['age'] = 25
my_dict['city'] = "New York"

# 3. Выведите содержимое словаря.
print(f'''Содержимое словаря my_dict:
    {my_dict}
''')


# 4. Измените возраст на 26.
my_dict['age'] = 26
print(my_dict['age'])

# 5. Добавьте ключ "email" в словарь.
my_dict['email'] = "john@example.com"

# 6. Проверьте наличие ключа "country" и выведите сообщение.
if 'country' in my_dict:
    print("Ключ 'country' есть в словаре.")
else:
    print("Ключ 'country' отсутствует в словаре.")

for key, val in my_dict.items():
    print(f'Ключ \'{key}\':Знач-ие \'{val}\'')
