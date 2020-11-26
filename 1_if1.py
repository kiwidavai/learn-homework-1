"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

age = int(input('Enter your age: '))


def main():
    if 0 < age < 6:
        return('kindergarden')
    elif 6 <= age <= 17:
        return('school')
    elif 18 <= age < 23:
        return('university')
    elif age <= 0:
        return("u're trying to trick me")
    elif age > 65:
        return("u old man")
    else:
        return('you must work')
    
if __name__ == "__main__":
    you_life = main()

print(you_life)

