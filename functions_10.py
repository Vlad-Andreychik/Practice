def sayHello():
    print('Привет, Мир!')


def printMax(a, b):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'равно', b)
    else:
        print(b, 'максимально')


def func(x):
    print('x  равен', x)
    x = 2
    print('Замена локального x на', x)


def func_global():
    global x

    print('x равно', x)
    x = 2
    print('Заменяем глобальное значение х на', x)


def func_outer():
    x = 2
    print('х равно', x)

    def func_inner():
        nonlocal x
        x = 5

    func_inner()
    print('Локальное х сменилось на', x)


def say(message, times=1):
    print(message * times)


def func_key(a, b=5, c=10):
    print('а равно', a, ', b равно', b, ', а с равно', c)


def total(a=5, *numbers, **phonebook):
    print('a', a)

    for single_item in numbers:
        print('single_item', single_item)

    for first_part, second_part in phonebook.items():
        print(first_part, second_part)


def total_only(initial=5, *numbers, extra_number):
    count = initial
    for number in numbers:
        count += number
    count += extra_number
    print(count)


def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'Числа равны.'
    else:
        return y


def printMax_desc(x, y):
    """Выводит максимальное из двух чисел.

    Оба значения должны быть целыми числами."""
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'наибольшее')
    else:
        print(y, 'наибольшее')
