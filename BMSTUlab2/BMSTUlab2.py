from tkinter import *
from tkinter import messagebox
from BMSTUlab2_heapsort import *


def label_writer(to_write, label_out):
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


def clean_label(*labels):
    for label in labels:
        label["text"] = ""


def sort_visual():
    sort_visual_window = Toplevel(root)
    sort_visual_window.grab_set()
    sort_visual_window.iconbitmap("icon.ico")
    sort_visual_window.geometry("300x500+425+250")
    sort_visual_window.resizable(False, False)
    sort_visual_window.title("Визуализация сортировки кучей (heapsort)")
    sort_visual_window.config(bg="#000080")

    s_v_w_welcome_label = Label(sort_visual_window,
                                text="\nВведите массив малой размерности:\n",
                                font="consolas 10",
                                bg="#000080",
                                fg="white")
    s_v_w_welcome_label.pack()

    s_v_w_entry = Entry(sort_visual_window, width=30)
    s_v_w_entry.pack()

    s_v_w_separate_label = Label(sort_visual_window,
                                 text="",
                                 bg="#000080")
    s_v_w_separate_label.pack()

    sort_visual_button = Button(sort_visual_window, text="Отсортировать",
                                width=16,
                                height=2,
                                font="consolas 10 bold",
                                bg="white",
                                fg="#000080",
                                command=lambda: label_writer(
                                    step_by_step_heapsort(
                                        [int(x) for x in s_v_w_entry
                                            .get()
                                            .strip()
                                            .split()]), s_v_w_result_label))
    sort_visual_button.pack()

    s_v_w_separate_label = Label(sort_visual_window,
                                 text="",
                                 bg="#000080")
    s_v_w_separate_label.pack()

    s_v_w_result_label = Label(sort_visual_window, text="",
                               bg="#000080",
                               fg="white",
                               font="consolas 10 bold")
    s_v_w_result_label.pack()


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


def exit_run(root):
    """ Выход из программы. """
    root.destroy()


""" Создание каскада окна программы. """
root = Tk()
root.iconbitmap("icon.ico")
root.geometry("600x400+400+200")
root.resizable(False, False)
root.title("HeapSorter")

""" Создание меню. """
main_menu = Menu(root)
root.config(menu=main_menu, bg="#000080")

clean_menu = Menu(main_menu, tearoff=0)
clean_menu.add_command(label="Очистить поле ввода N1",
                       command=lambda: clean_entry(n1_entry, n1_count_entry))
clean_menu.add_command(label="Очистить поле вывода N1",
                       command=lambda: clean_field(label_out_n1))
clean_menu.add_separator()
clean_menu.add_command(label="Очистить поле ввода N2",
                       command=lambda: clean_entry(n2_entry, n2_count_entry))
clean_menu.add_command(label="Очистить поле вывода N2",
                       command=lambda: clean_field(label_out_n2))
clean_menu.add_separator()
clean_menu.add_command(label="Очистить поле ввода N3",
                       command=lambda: clean_entry(n3_entry, n3_count_entry))
clean_menu.add_command(label="Очистить поле вывода N3",
                       command=lambda: clean_field(label_out_n3))
clean_menu.add_separator()
clean_menu.add_command(label="Очистить все поля",
                       command=lambda: clean_field(entry_in, entry_out))

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

n2_input_label = Label(root,
                       text="Введите диапазон N2",
                       font="consolas 10",
                       bg="#000080",
                       fg="white")
n2_input_label.grid(row=5, column=3)

n2_entry = Entry(root, width=20)
n2_entry.grid(row=6, column=3)

n3_input_label = Label(root,
                       text="Введите диапазон N3",
                       font="consolas 10",
                       bg="#000080",
                       fg="white")
n3_input_label.grid(row=5, column=4)

n3_entry = Entry(root, width=20)
n3_entry.grid(row=6, column=4)

sorted_label = Label(root,
                       text="\nУпорядоченный по\n"
                            "возрастанию массив\n\n"
                            "Заданный случайным\n"
                            "образом массив\n\n"
                            "Сортированный в обратном\n"
                            "порядке массив\n\n"
                            "Сортированный функцией\n"
                            "sort массив",
                       font="consolas 10",
                       bg="#000080",
                       fg="white")
sorted_label.grid(row=7, rowspan=11, column=1)

root.mainloop()