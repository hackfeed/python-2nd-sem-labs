from tkinter import *
from tkinter import messagebox
from random import randint
from time import time
from BMSTUlab2_heapsort import *


def int_list_getter(in_entry):
    """ Функция формирования целочисленного списка.

    Данная функция формирует целочисленный список для
    визуализации работы пирамидальной сортировки
    (с условием, что элементов в таком списке должно быть
    не больше 5).

    Передаваемые параметры:
    * in_entry - поле ввода, из которого формируется список

    Возвращаемые значения:
    * int_list - сформированный целочисленный список

    """

    try:
        int_list = [int(x) for x in in_entry.get().strip().split()]

        if len(int_list) == 0 or len(int_list) > 5 or \
                isinstance(int_list, (str, type(None))):
            raise ValueError

        return int_list

    except ValueError:
        messagebox.showerror("Ошибка ввода данных", "Данные введены "
                                                    "некорректно "
                                                    "или введено больше 5 "
                                                    "чисел, проверьте "
                                                    "правильность ввода!")


def int_list_getter_dim(in_entry):
    """ Функция формирования целочисленного списка.

    Данная функция формирует целочисленный список для
    получения интервала формирования чисел в исходном
    для сортировки массиве (таких чисел должно быть 2).

    Передаваемые параметры:
    * in_entry - поле ввода, из которого формируется список

    Возвращаемые значения:
    * int_list - сформированный целочисленный список

    """

    try:
        int_list = [int(x) for x in in_entry.get().strip().split()]

        if len(int_list) == 0 or len(int_list) > 2 or \
                isinstance(int_list, (str, type(None))):
            raise ValueError

        return int_list

    except ValueError:
        messagebox.showerror("Ошибка ввода данных", "Данные введены "
                                                    "некорректно, проверьте "
                                                    "правильность ввода!")


def label_writer(to_write, label_out):
    """ Функция записи в Label.

    Данная функция изменяет содержимое поля text в Label.

    Передаваемые параметры:
    * to_write - что будет записано в Label
    * label_out - Label, в который будет произведена запись

    """

    label_out["text"] = ""
    label_out["text"] += to_write


def clean_entry(*entries):
    """ Функция очистки полей ввода.

    Данная функция очищает поля ввода/вывода данных.
    Очистка может производиться как одного, так и сразу
    нескольких полей.

    Передаваемые параметры:
    * *entries - поля ввода, которые надо очистить

    """

    for entry in entries:
        entry.config(state="normal")
        entry.delete(0, END)


def clean_entry_list(entry_list):
    """ Функция очистки списков полей ввода.

    Данная функция очищает поля ввода/вывода данных.
    Очищаются все поля ввода/вывода, содержащиеся в списке
    entry_list.

    Передаваемые параметры:
    * entry_list - список полей ввода/вывода, которые надо очистить

    """

    for entry in entry_list:
        entry.config(state="normal")
        entry.delete(0, END)
        entry.config(state="readonly")


def clean_label(*labels):
    """ Функция очистки Label'ов.

    Данная функция очищает Label'ы
    (изменяет их поля text на пустую строку "")

    Передаваемые параметры:
    * *labels - Label'ы, которые надо очистить

    """

    for label in labels:
        label["text"] = ""


def sort_visual():
    """ Функция вызова окна с визуализацие сортировки.

    Данная функция реализует визуализацию алгоритма
    пирамидальной сортировки (сортировка кучей).

    """
    def bind_visual_sort(event):
        """ Сортировка при нажатии на клавишу Enter. """
        label_writer(
            step_by_step_heapsort(int_list_getter(s_v_w_entry)),
            s_v_w_result_label
        )

    def bind_visual_clean(event):
        """ Очистка при нажатии любой клавиши. """
        clean_label(s_v_w_result_label)

    sort_visual_window = Toplevel(root)
    sort_visual_window.grab_set()
    sort_visual_window.iconbitmap("icon.ico")
    sort_visual_window.geometry("300x500+425+250")
    sort_visual_window.resizable(False, False)
    sort_visual_window.title("Визуализация сортировки кучей (heapsort)")
    sort_visual_window.config(bg="#000080")

    s_v_w_welcome_label = Label(sort_visual_window,
                                text="\nВведите массив малой размерности\n"
                                     "(до 5 элементов):",
                                font="consolas 10",
                                bg="#000080",
                                fg="white")
    s_v_w_welcome_label.pack()

    s_v_w_entry = Entry(sort_visual_window, width=30)
    s_v_w_entry.pack()

    s_v_w_entry.focus_set()

    s_v_w_separate_label = Label(sort_visual_window,
                                 text="",
                                 bg="#000080")
    s_v_w_separate_label.pack()

    sort_visual_button = Button(sort_visual_window, text="Отсортировать",
                                width=16,
                                height=2,
                                font="consolas 10 bold",
                                bg="white",
                                fg="#0ad325",
                                command=lambda:
                                label_writer(step_by_step_heapsort(
                                    int_list_getter(s_v_w_entry)),
                                    s_v_w_result_label))
    sort_visual_button.pack()

    s_v_w_separate_label = Label(sort_visual_window,
                                 text="",
                                 bg="#000080")
    s_v_w_separate_label.pack()

    s_v_w_result_label = Label(sort_visual_window, text="",
                               width=32,
                               height=19,
                               bg="#000080",
                               fg="white",
                               font="consolas 10 bold")
    s_v_w_result_label.pack()

    exit_visual_button = Button(sort_visual_window, text="Выйти",
                                width=16,
                                height=2,
                                font="consolas 10 bold",
                                bg="white",
                                fg="#ff0000",
                                command=lambda: exit_run(sort_visual_window))
    exit_visual_button.pack()

    s_v_w_entry.bind("<Return>", bind_visual_sort)
    s_v_w_entry.bind("<Key>", bind_visual_clean)


def about():
    """" Вывод окна "О программе" """
    about_window = Toplevel(root)
    about_window.grab_set()
    about_window.iconbitmap("icon.ico")
    about_window.geometry("330x200+425+250")
    about_window.resizable(False, False)
    about_window.title("О HeapSorter")
    about_window.config(bg="#000080")

    about_label1 = Label(about_window,
                         text="\nВизуализация пирамидальной\n "
                              "сортировки и сравнение времени, отведенного\n"
                              "на сортировку массивов различного\n"
                              "типа этим способом"
                              "\n\n"
                              "Kononenko Sergey ICS7-23B",
                         font="consolas 10",
                         bg="#000080",
                         fg="white")
    about_label1.pack()

    about_label2 = Label(about_window,
                         text="@hackfeed",
                         font="consolas 10 bold",
                         bg="white",
                         fg="#000080")
    about_label2.pack()

    exit_about = Button(about_window, text="Выйти",
                        width=6,
                        height=2,
                        font="consolas 10 bold",
                        bg="#000080",
                        fg="white",
                        relief="flat",
                        command=lambda: exit_run(about_window))
    exit_about.pack()


def sort_timingly(size, dim_list):
    """ Функция сортировки четырху типов массивов с замером времени,
    затраченного на сортировку.

    Данная функция формирует случайный список с заданными параметрами,
    затем сортирует его в соответствии с условием и замеряет время
    затраченное на проделанную операцию.

    Передаваемые параметры:
    * size - размер массива
    * dim_list - границы чисел, которые будут использованы в массиве

    Возвращаемые значения:
    * time_list - список с полученными значениями времени

    """

    try:
        if size < 1 or dim_list[0] >= dim_list[1]:
            messagebox.showerror("Ошибка ввода данных", "Данные введены "
                                                        "некорректно, проверьте "
                                                        "правильность ввода!")
        else:
            random_list = list()
            time_list = list()

            for i in range(size):
                random_list.append(randint(dim_list[0], dim_list[1]))

            """ Массив, упорядоченный по возрастанию. """
            ascending_sorted_list = random_list[:]
            heapsort(ascending_sorted_list)
            start_time = time()
            heapsort(ascending_sorted_list)
            end_time = time()

            res_str = "{0:.5f}".format(end_time - start_time) + " c."
            time_list.append(res_str)

            """ Случайно заданный массив. """
            random_sorted_list = random_list[:]
            heapsort(random_sorted_list)
            start_time = time()
            heapsort(random_sorted_list)
            end_time = time()

            res_str = "{0:.5f}".format(end_time - start_time) + " c."
            time_list.append(res_str)

            """ Массив, упорядоченный по убыванию. """
            descending_sorted_list = random_list[:]
            heapsort(descending_sorted_list)
            descending_sorted_list.reverse()
            start_time = time()
            heapsort(descending_sorted_list)
            end_time = time()

            res_str = "{0:.5f}".format(end_time - start_time) + " c."
            time_list.append(res_str)

            """ Массив, отсортированный встроенной функцией sort. """
            sort_sorted_list = random_list[:]
            start_time = time()
            sort_sorted_list.sort()
            end_time = time()

            res_str = "{0:.5f}".format(end_time - start_time) + " c."
            time_list.append(res_str)

            return time_list

    except TypeError:
        pass

    except IndexError:
        messagebox.showinfo("Неполные данные", "Данные введены "
                                               "некорректно. Пожалуйста, "
                                               "введите диапазон в формате "
                                               "<левая_граница правая_граница>!")


def sort_comparative(entry_in_n, entry_in_dim, entry_out_list):
    """ Функция записи полученных результатов в поля вывода.

    Принимаемые параметры:
    * entry_in_n - поле, в котором указан размер массива
    * entry_in_dim - поле, в котором указаны границы массива
    * entry_out_list - поля вывода

    """

    try:
        n_value = int(entry_in_n.get().strip())
        if n_value < 1:
            raise ValueError
        else:
            dim_list = int_list_getter_dim(entry_in_dim)
            for entry in entry_out_list:
                entry.config(state="normal")
                entry.delete(0, END)
                entry.config(state="readonly")

            sorted_time_list = sort_timingly(n_value, dim_list)

            k = 0

            for entry in entry_out_list:
                entry.config(state="normal")
                entry.insert(0, sorted_time_list[k])
                entry.config(state="readonly")
                k += 1

    except ValueError:
        for entry in entry_out_list:
            entry.config(state="readonly")
        messagebox.showerror("Ошибка ввода данных", "Данные введены "
                                                    "некорректно, проверьте "
                                                    "правильность ввода!")

    except TypeError:
        pass


def exit_run(root):
    """ Выход из программы. """
    root.destroy()


def bind_sort_n1(event):
    """ Сортировка для N1 при нажатии на клавишу Enter. """
    sort_comparative(n1_count_entry, n1_entry, n1_out_entries)


def bind_sort_n2(event):
    """ Сортировка для N2 при нажатии на клавишу Enter. """
    sort_comparative(n2_count_entry, n2_entry, n2_out_entries)


def bind_sort_n3(event):
    """ Сортировка для N3 при нажатии на клавишу Enter. """
    sort_comparative(n3_count_entry, n3_entry, n3_out_entries)


def bind_cleaner_n1(event):
    """ Очистка полей вывода для N1 при нажатии любой клавиши. """
    clean_entry_list(n1_out_entries)


def bind_cleaner_n2(event):
    """ Очистка полей вывода для N2 при нажатии любой клавиши. """
    clean_entry_list(n2_out_entries)


def bind_cleaner_n3(event):
    """ Очистка полей вывода для N3 при нажатии любой клавиши. """
    clean_entry_list(n3_out_entries)


""" Создание каскада окна программы. """
root = Tk()
root.iconbitmap("icon.ico")
root.geometry("593x335+400+200")
root.resizable(False, False)
root.title("HeapSorter")

""" Создание меню. """
main_menu = Menu(root)
root.config(menu=main_menu, bg="#000080")

clean_menu = Menu(main_menu, tearoff=0)
clean_menu.add_command(label="Очистить поле ввода N1",
                       command=lambda: clean_entry(n1_entry, n1_count_entry))
clean_menu.add_command(label="Очистить поле вывода N1",
                       command=lambda: clean_entry_list(n1_out_entries))
clean_menu.add_separator()
clean_menu.add_command(label="Очистить поле ввода N2",
                       command=lambda: clean_entry(n2_entry, n2_count_entry))
clean_menu.add_command(label="Очистить поле вывода N2",
                       command=lambda: clean_entry_list(n2_out_entries))
clean_menu.add_separator()
clean_menu.add_command(label="Очистить поле ввода N3",
                       command=lambda: clean_entry(n3_entry, n3_count_entry))
clean_menu.add_command(label="Очистить поле вывода N3",
                       command=lambda: clean_entry_list(n3_out_entries))
clean_menu.add_separator()
clean_menu.add_command(label="Очистить все поля",
                       command=lambda: (clean_entry(n1_entry, n1_count_entry,
                                                    n2_entry, n2_count_entry,
                                                    n3_entry, n3_count_entry
                                                    ),
                                        clean_entry_list(n1_out_entries),
                                        clean_entry_list(n2_out_entries),
                                        clean_entry_list(n3_out_entries)))

workmode_menu = Menu(main_menu, tearoff=0)
workmode_menu.add_command(label="Режим визуализации",
                          command=lambda: sort_visual())
workmode_menu.add_command(label="Режим сравнения",
                          command=lambda: messagebox.showinfo(
                                                    "Необходимый режим",
                                                    "Вы уже в необходимом "
                                                    "режиме!"))


about_menu = Menu(main_menu, tearoff=0)
about_menu.add_command(label="О программе", command=lambda: about())

main_menu.add_cascade(label="Режим работы", menu=workmode_menu)
main_menu.add_cascade(label="Очистка", menu=clean_menu)
main_menu.add_cascade(label="Справка", menu=about_menu)

""" Организация UI. """
welcome_label = Label(root,
                      text="Сравнение времени, затраченного на пирамидальную "
                           "сортировку на различных массивах",
                      font="consolas 10 bold",
                      bg="white",
                      fg="#000080")
welcome_label.grid(row=1, rowspan=2, column=1, columnspan=4)

n1_label = Label(root,
                 text="Введите N1",
                 font="consolas 10",
                 bg="#000080",
                 fg="white")
n1_label.grid(row=3, column=2)

n1_count_entry = Entry(root, width=20)
n1_count_entry.grid(row=4, column=2)

n2_label = Label(root,
                 text="Введите N2",
                 font="consolas 10",
                 bg="#000080",
                 fg="white")
n2_label.grid(row=3, column=3)

n2_count_entry = Entry(root, width=20)
n2_count_entry.grid(row=4, column=3)

n3_label = Label(root,
                 text="Введите N3",
                 font="consolas 10",
                 bg="#000080",
                 fg="white")
n3_label.grid(row=3, column=4)

n3_count_entry = Entry(root, width=20)
n3_count_entry.grid(row=4, column=4)

n1_input_label = Label(root,
                       text="Введите диапазон N1",
                       font="consolas 10",
                       bg="#000080",
                       fg="white")
n1_input_label.grid(row=5, column=2)

n1_entry = Entry(root, width=20)
n1_entry.grid(row=6, column=2)

n1_asc_sorted = Entry(root, width=20)
n1_asc_sorted.grid(row=8, rowspan=2, column=2)
n1_desc_sorted = Entry(root, width=20)
n1_desc_sorted.grid(row=10, rowspan=2, column=2)
n1_rand_sorted = Entry(root, width=20)
n1_rand_sorted.grid(row=12, rowspan=2, column=2)
n1_sort_sorted = Entry(root, width=20)
n1_sort_sorted.grid(row=14, rowspan=2, column=2)
n1_out_entries = [n1_asc_sorted, n1_desc_sorted, n1_rand_sorted, n1_sort_sorted]
for entry in n1_out_entries:
    entry.config(state="readonly")

n2_input_label = Label(root,
                       text="Введите диапазон N2",
                       font="consolas 10",
                       bg="#000080",
                       fg="white")
n2_input_label.grid(row=5, column=3)

n2_entry = Entry(root, width=20)
n2_entry.grid(row=6, column=3)

n2_asc_sorted = Entry(root, width=20)
n2_asc_sorted.grid(row=8, rowspan=2, column=3)
n2_desc_sorted = Entry(root, width=20)
n2_desc_sorted.grid(row=10, rowspan=2, column=3)
n2_rand_sorted = Entry(root, width=20)
n2_rand_sorted.grid(row=12, rowspan=2, column=3)
n2_sort_sorted = Entry(root, width=20)
n2_sort_sorted.grid(row=14, rowspan=2, column=3)
n2_out_entries = [n2_asc_sorted, n2_desc_sorted, n2_rand_sorted, n2_sort_sorted]
for entry in n2_out_entries:
    entry.config(state="readonly")

n3_input_label = Label(root,
                       text="Введите диапазон N3",
                       font="consolas 10",
                       bg="#000080",
                       fg="white")
n3_input_label.grid(row=5, column=4)

n3_entry = Entry(root, width=20)
n3_entry.grid(row=6, column=4)

n3_asc_sorted = Entry(root, width=20)
n3_asc_sorted.grid(row=8, rowspan=2, column=4)
n3_desc_sorted = Entry(root, width=20)
n3_desc_sorted.grid(row=10, rowspan=2, column=4)
n3_rand_sorted = Entry(root, width=20)
n3_rand_sorted.grid(row=12, rowspan=2, column=4)
n3_sort_sorted = Entry(root, width=20)
n3_sort_sorted.grid(row=14, rowspan=2, column=4)
n3_out_entries = [n3_asc_sorted, n3_desc_sorted, n3_rand_sorted, n3_sort_sorted]
for entry in n3_out_entries:
    entry.config(state="readonly")

pass_label = Label(root, text="", bg="#000080")
pass_label.grid(row=7, columnspan=4)

sorted_ascending_label = Label(root,
                               text="Упорядоченный по\n возрастанию массив",
                               font="consolas 10",
                               bg="#000080",
                               fg="white")
sorted_ascending_label.grid(row=8, rowspan=2, column=1)

sorted_descending_label = Label(root,
                                text="Упорядоченный по\n убыванию массив",
                                font="consolas 10",
                                bg="#000080",
                                fg="white")
sorted_descending_label.grid(row=10, rowspan=2, column=1)

sorted_random_label = Label(root,
                            text="Заданный случайным\n образом массив",
                            font="consolas 10",
                            bg="#000080",
                            fg="white")
sorted_random_label.grid(row=12, rowspan=2, column=1)

sorted_sort_label = Label(root,
                          text="Отсортированный функцией\n sort массив",
                          font="consolas 10",
                          bg="#000080",
                          fg="white")
sorted_sort_label.grid(row=14, rowspan=2, column=1)

sort_all_button = Button(root, text="Отсортировать",
                         width=16,
                         height=2,
                         font="consolas 10 bold",
                         bg="white",
                         fg="#0ad325",
                         command=lambda: (sort_comparative
                                          (n1_count_entry, n1_entry, n1_out_entries),
                                          sort_comparative
                                          (n2_count_entry, n2_entry, n2_out_entries),
                                          sort_comparative
                                          (n3_count_entry, n3_entry, n3_out_entries))
                         )
sort_all_button.grid(row=4, rowspan=2, column=1)

exit_button = Button(root, text="Выйти",
                                width=16,
                                height=2,
                                font="consolas 10 bold",
                                bg="white",
                                fg="#ff0000",
                                command=lambda: exit_run(root))
exit_button.grid(row=16, rowspan=2, column=2, columnspan=2, sticky="N")

n1_count_entry.focus_set()

n1_count_entry.bind("<Return>", bind_sort_n1)
n1_count_entry.bind("<Key>", bind_cleaner_n1)
n1_entry.bind("<Return>", bind_sort_n1)
n1_entry.bind("<Key>", bind_cleaner_n1)

n2_count_entry.bind("<Return>", bind_sort_n2)
n2_count_entry.bind("<Key>", bind_cleaner_n2)
n2_entry.bind("<Return>", bind_sort_n2)
n2_entry.bind("<Key>", bind_cleaner_n2)

n3_count_entry.bind("<Return>", bind_sort_n3)
n3_count_entry.bind("<Key>", bind_cleaner_n3)
n3_entry.bind("<Return>", bind_sort_n3)
n3_entry.bind("<Key>", bind_cleaner_n3)

root.mainloop()
