Python 3.9.5 (v3.9.5:0a7dcbdb13, May  3 2021, 13:17:02) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # объявление функции
def draw_box():
    print("**********")
    for i in range(12):
        print("*        *")
    print("**********")

# основная программа
draw_box()  # вызов функции