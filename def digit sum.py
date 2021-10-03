Python 3.9.5 (v3.9.5:0a7dcbdb13, May  3 2021, 13:17:02) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # объявление функции
def print_digit_sum(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    print(sum)

# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)