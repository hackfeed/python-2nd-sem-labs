from tkinter import *
from tkinter import messagebox
from BMSTUlab1_3sim_module import *


def clean_field(*entries):
    """ Функция очистки полей ввода/вывода.

    Данная функция очищает поля ввода/вывода данных.
    Очистка может производиться как одного, так и сразу
    всех полей.

    Передаваемые параметры:
    * *entries - поля ввода/вывода, которые надо очистить

    """

    for entry in entries:
        entry.config(state="normal")
        entry.delete(0, END)


def calculate(entry_in, entry_out):
    """ Функция перевода числа между системами счисления.

    Данная функция, ссылаясь на функцию transform из модуля,
    переводит числа между СС (автодетект необходимого перевода)
    и подготавливает поля ввода/вывода для соответственной записи
    полученного числа.

    Передаваемые параметры:
    * entry_in, entry_out - поле ввода, поле вывода

    """

    number = entry_in.get().strip()
    entry_out.config(state="normal")
    entry_out.delete(0, END)
    try:
        entry_out.insert(0, transform(number))
        entry_out.config(state="readonly")
    except ValueError:
        messagebox.showerror("Ошибка ввода данных", "Данные введены "
                                                    "некорректно, проверьте "
                                                    "правильность ввода!")


def about():
    """" Вывод окна "О программе" """
    about_window = Toplevel(root)
    about_window.grab_set()
    about_window.iconbitmap("icon.ico")
    about_window.geometry("250x150+425+250")
    about_window.resizable(False, False)
    about_window.title("О 3Transform")
    about_window.config(bg="#000080")

    about_label1 = Label(about_window,
                         text="\nПеревод чисел в десятичной\n "
                              "и троичносимметричной СС"
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


def bind_calculate(event):
    """ Перевод при нажатии на клавишу Enter. """
    calculate(entry_in, entry_out)


def bind_cleaner(event):
    """ Очистка поля вывода при нажатии любой клавиши. """
    clean_field(entry_out)
    entry_out.config(state="readonly")


""" Создание каскада окна программы. """
root = Tk()
root.iconbitmap("icon.ico")
root.geometry("300x350+400+200")
root.resizable(False, False)
root.title("3Transform")

""" Создание меню. """
main_menu = Menu(root)
root.config(menu=main_menu, bg="#000080")

clean_menu = Menu(main_menu, tearoff=0)
clean_menu.add_command(label="Очистить поле ввода",
                       command=lambda: (clean_field(entry_in),
                                        entry_out.config(state="readonly")))
clean_menu.add_command(label="Очистить поле вывода",
                       command=lambda: (clean_field(entry_out),
                                        entry_out.config(state="readonly")))
clean_menu.add_separator()
clean_menu.add_command(label="Очистить оба поля",
                       command=lambda: (clean_field(entry_in, entry_out),
                                        entry_out.config(state="readonly")))

calculate_menu = Menu(main_menu, tearoff=0)
calculate_menu.add_command(label="Перевести",
                           command=lambda: calculate(entry_in, entry_out))

about_menu = Menu(main_menu, tearoff=0)
about_menu.add_command(label="О программе", command=lambda: about())

main_menu.add_cascade(label="Перевод", menu=calculate_menu)
main_menu.add_cascade(label="Очистка", menu=clean_menu)
main_menu.add_cascade(label="Справка", menu=about_menu)

welcome_label = Label(text="\nВведите число в десятичной или\n"
                           "троичносимметричной СС:",
                      bg="#000080",
                      fg="white",
                      font="consolas 10 bold")
welcome_label.pack()

entry_in = Entry(root, width=40)
entry_in.pack()

result_label = Label(text="\nРезультат:",
                     bg="#000080",
                     fg="white",
                     font="consolas 10 bold")
result_label.pack()

entry_out = Entry(root, width=40, state="readonly")
entry_out.pack()

entry_in.focus_set()
entry_in.bind("<Return>", bind_calculate)
entry_in.bind("<Key>", bind_cleaner)

""" Создание наэкранной клавиатуры. """
button_labels_list = ["1", "2", "3", "4", "5", "6",
                      "7", "8", "9", "-", "0", "+"]
button_list = list()

for i in range(len(button_labels_list)):
    button_list.append(Button(text=button_labels_list[i],
                              width=4,
                              height=2,
                              font="consolas 10 bold",
                              bg="white",
                              fg="#000080",
                              command=lambda i=i:
                              (entry_in.insert(END, button_labels_list[i]),
                               entry_out.config(state="normal"),
                               entry_out.delete(0, END),
                               entry_out.config(state="readonly"))))
    if i < 3:
        button_list[i].place(anchor="c", x=110 + i % 3 * 40, y=170)
    elif i < 6:
        button_list[i].place(anchor="c", x=110 + i % 3 * 40, y=212)
    elif i < 9:
        button_list[i].place(anchor="c", x=110 + i % 3 * 40, y=254)
    else:
        button_list[i].place(anchor="c", x=110 + i % 3 * 40, y=296)

exit_btn = Button(text="Выйти",
                  width=7,
                  height=2,
                  font="consolas 10 bold",
                  bg="white",
                  fg="#ff0000",
                  command=lambda: exit_run(root))
exit_btn.place(anchor="c", x=250, y=233)

calculate_btn = Button(text="Перевод",
                       width=7,
                       height=2,
                       font="consolas 10 bold",
                       bg="white",
                       fg="#0ad325",
                       command=lambda: calculate(entry_in, entry_out))
calculate_btn.place(anchor="c", x=50, y=233)

clear_btn = Button(text="C",
                   width=4,
                   height=2,
                   font="consolas 10 bold",
                   bg="white",
                   fg="#000080",
                   command=lambda:
                   (entry_in.delete(len(entry_in.get())-1, END),
                    entry_out.config(state="normal"),
                    entry_out.delete(0, END),
                    entry_out.config(state="readonly")))
clear_btn.place(anchor="c", x=230, y=296)

root.mainloop()
