"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
a,b = None, None
def main(a,b):
    a, b = input('Enter first row: '), input("Enter second row: ")
    if type(a) is str and type(b) is str and a == b:
        return '1'
    elif type(a) is str and type(b) and a != b and len(a) > len(b):
        return '2'
    elif type(a) is str and type(b) and a != b and b == 'learn':
        return '3'
    else:
        return '0'
    
if __name__ == "__main__":
    print(main(a, b))
