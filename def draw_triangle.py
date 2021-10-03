Python 3.9.5 (v3.9.5:0a7dcbdb13, May  3 2021, 13:17:02) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # объявление функции
def draw_triangle(fill, base):
    l = [i for i in range(1,base//2+2,)]
    l.extend([i for i in range(base//2, 0, -1)])
    for elem in l:
        print(fill * elem)

# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)