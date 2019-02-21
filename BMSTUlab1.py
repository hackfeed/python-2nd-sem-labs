from tkinter import *
from tkinter import messagebox
from BMSTUlab1_3sim_module import *


def clean_field(*entries):
    for entry in entries:
        entry.delete(0, END)


def calculate(entry_in, entry_out):
    number = entry_in.get()
    entry_out.delete(0, END)
    try:
        entry_out.insert(0, transform(number))
    except ValueError:
        messagebox.showerror("Ошибка ввода данных", "Данные введены некорректно, проверьте "
                                                    "правильность ввода!")


def bind_calculate(event):
    calculate(entry_in, entry_out)


def about():
    about_window = Toplevel(root)
    about_window.iconbitmap("icon.ico")
    about_window.geometry("250x150+425+250")
    about_window.resizable(False, False)
    about_window.title("About 3Calc")
    about_window.config(bg="white")

    about_label1 = Label(about_window,
                         text="\nПеревод чисел в десятичной\n "
                              "и троичносимметричной СС"
                              "\n\n Made By\n"
                              "Kononenko Sergey\n IU7-23B",
                         font="consolas 10",
                         bg="white")
    about_label1.pack()

    about_label2 = Label(about_window,
                         text="@hackfeed",
                         font="consolas 10 bold",
                         bg="white")
    about_label2.pack()


root = Tk()
root.iconbitmap("icon.ico")
root.geometry("300x350+400+200")
root.resizable(False, False)
root.title("3Transform")


main_menu = Menu(root)
root.config(menu=main_menu, bg="#F0FFF0")

clean_menu = Menu(main_menu, tearoff=0)
clean_menu.add_command(label="Очистить поле ввода", command=lambda: clean_field(entry_in))
clean_menu.add_command(label="Очистить поле вывода", command=lambda: clean_field(entry_out))
clean_menu.add_separator()
clean_menu.add_command(label="Очистить оба поля", command=lambda: clean_field(entry_in, entry_out))

main_menu.add_command(label="Перевести", command=lambda: calculate(entry_in, entry_out))
main_menu.add_cascade(label="Очистка", menu=clean_menu)
main_menu.add_command(label="О программе", command=about)

welcome_label = Label(text="\nВведите число в десятичной или\n"
                           "троичносимметричной СС:",
                      bg="#F0FFF0",
                      font="consolas 10 bold")
welcome_label.pack()

entry_in = Entry(root, width=40)
entry_in.pack()

splash_label = Label(text="\nРезультат:",
                     bg="#F0FFF0",
                     font="consolas 10 bold")
splash_label.pack()

entry_out = Entry(root, width=40)
entry_out.pack()

entry_in.focus_set()
entry_in.bind("<Return>", bind_calculate)


button_labels_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "-", "0", "+"]
button_list = list()

# for i in range(len(button_list)):

root.mainloop()

