from math import *


def f(x):
    return sin(x)


def derivative_f(x):
    return cos(x)


def cas_method(begin, end, step, epsilon, max_iterations):
    magic_offset = 0.0000000001
    
    border_a = begin - magic_offset
    border_b = end
    
    list_temp_a = list()
    list_temp_b = list()
    list_x_approximate = list()
    list_fx = list()
    list_code_error = list()
    
    total_interval = border_b - border_a
    temp_a = border_a
    
    count_roots = 0

    for i in range(ceil(total_interval / step)):
        temp_b = temp_a + step
        code_error = 0
        count_iterations = 1

        if temp_b > border_b:
            temp_b = border_b

        if (f(temp_b) * f(temp_a)) < 0:
            count_roots += 1
            try_search = 1

            while try_search < 3:
                count_iterations = 1
                if try_search == 1:
                    x_o = temp_a
                else:
                    x_o = temp_b

                root_previous = x_o - (f(x_o) / derivative_f(x_o))
                root = root_previous - (f(root_previous) / \
                                        derivative_f(root_previous))

                while abs(root - root_previous) > epsilon and \
                      count_iterations < max_iterations:
                    root_previous = root
                    root = root_previous - (f(root_previous) / \
                                            derivative_f(root_previous))
                    count_iterations += 1

                if temp_a <= root <= temp_b:
                    break

                try_search += 1

            if not (temp_a < root < temp_b):
                code_error = 3

            if max_iterations <= count_iterations:
                code_error = 2

            list_x_approximate.append(root)

            list_code_error.append(code_error)
            list_fx.append(f(root))

            list_temp_a.append(temp_a)
            list_temp_b.append(temp_b)

        temp_a = temp_b + magic_offset

    return list_temp_a, list_temp_b, list_x_approximate, list_fx, list_code_error, count_roots


begin, end = map(float, input("Введите начало и конец отрезка: ").split())
eps = float(input("Введите погрешность: "))
step, max_iter = map(float, input("Введите шаг и максимальное кол-во итераций: ").split())

calculated = cas_method(begin, end, step, eps, max_iter)

if calculated[5] == 0:
    print("Корни не найдены")
else:
    print()
    print("Значения корней")
    for i in range(calculated[5]):
        print("[{0:10f};{1:10f}] | {2:10f} | {3:10.3e} | {4:^3d}".format(calculated[0][i],
                                                                       calculated[1][i],
                                                                       calculated[2][i],
                                                                       calculated[3][i],
                                                                       calculated[4][i]))
