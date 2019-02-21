def abs_transform_to_3sim(number):
    """ Функция перевода числа из десятичной системы счисления
    в троичносимметричную (по модулю).

    Число переводится из десятичной системы в троичносимметричную
    посредством последовательного деления десятичного числа на
    основание новой СС (3). Результат деления записывается
    записывается в список, который потом реверсится для получения
    итогового числа.

    Передаваемые параметры:
    * number - число в десятичной СС

    Возвращаемые значения:
    * result_number - список из знаков полученного числа (в обратном
    порядке)

    """

    result_number = list()
    number = abs(int(number))

    while number > 0:
        if number % 3 == 0:
            result_number.append("0")
            number //= 3
        elif number % 3 == 1:
            result_number.append("+")
            number //= 3
        elif number % 3 == 2:
            result_number.append("-")
            number = number // 3 + 1

    result_number.reverse()

    return result_number


def transform_to_3sim(number):
    """ Функция перевода числа из десятичной системы счисления
    в троичносимметричную (с учётом знака).

    Число переводится из десятичной системы в троичносимметричную
    посредством по модулю функции abs_transform_to_3sim.
    Знак учитывается после перевода по модулю при проверке
    исходного десятичного числа.

    Передаваемые параметры:
    * number - число в десятичной СС

    Возвращаемые значения:
    * result_number - список из знаков полученного числа (в обратном
    порядке)

    """
    result_number = abs_transform_to_3sim(number)
    if int(number) > 0:

        return "".join(result_number)

    elif int(number) < 0:
        for i in range(len(result_number)):
            if result_number[i] == "-":
                result_number[i] = "+"
            elif result_number[i] == "+":
                result_number[i] = "-"

        return "".join(result_number)

    else:

        return 0


def transform_to_dec(number):
    """ Функция перевода числа из троичносимметричной системы счисления
    в десятичную.

    Последовательность знаков троичносимметричного числа переводится по
    правилу перевода из любой n-ричной системы в десятичную.

    Передаваемые параметры:
    * number - число в десятичной СС

    Возвращаемые значения:
    * result_number - полученное число в десятичной СС

    Промежуточные значения:
    * digits_set - множество допустимых знаков в передаваемом параметре
    * number_digits_list - список знаков в записи передаваемого параметра

    """

    digits_set = ("-", "+", "0")

    """ Проверка на правильность ввода троичносимметричного числа.
    В случае некорректно введенного числа вызывается исключение. """
    for dig in number:
        if dig not in digits_set:
            raise ValueError

    number_digits_list = list(number)

    for i in range(len(number_digits_list)):
        if number_digits_list[i] == "-":
            number_digits_list[i] = -1
        elif number_digits_list[i] == "+":
            number_digits_list[i] = 1
        else:
            number_digits_list[i] = 0

    k = len(number_digits_list) - 1
    i = 0
    result_number = 0

    while k >= 0:
        result_number += 3**k * number_digits_list[i]
        k -= 1
        i += 1

    return result_number


def transform(number):
    """ Функция перевода числа в троичносимметричную систему счисления из
    десятичной или обратно в зависимости от введенных данных.

    На основе полученного параметра number функция определяет, какой перевод
    необходимо выполнить. Перевод осуществляется при помощи функций
    transform_to_3sim и transform_to_dec.

    Передаваемые параметры:
    * number - число в десятичной СС

    Возвращаемые значения:
    * result_number - полученное число в десятичной или троичносимметричной СС

    Промежуточные значения:
    * pm_set - множество знаков, которые могут быть на первом месте в
    десятичных числах

    """

    pm_set = ("+", "-")

    if number.isdigit() or number[1:].isdigit() and number[0] in pm_set:
        result_number = transform_to_3sim(number)

    else:  # docstring коммент не работает. Перевод из 3sim в 10-чную СС
        result_number = transform_to_dec(number)

    return result_number
