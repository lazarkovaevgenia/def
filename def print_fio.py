Python 3.9.5 (v3.9.5:0a7dcbdb13, May  3 2021, 13:17:02) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # объявление функции
def print_fio(name, surname, patronymic):
    print(''.join([surname[0], name[0], patronymic[0]]).upper())

# считываем данные
name, surname, patronymic = input(), input(), input()

# вызываем функцию
print_fio(name, surname, patronymic)