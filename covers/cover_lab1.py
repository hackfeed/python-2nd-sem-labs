from tkinter import *

def calculate(entry_in, label_out):

    get_list = list(entry_in.get().strip().split())

    average_positive = 0
    count_positive = 0

    average_negative = 0
    count_negative = 0

    for x in get_list:
        if float(x) < 0:
            average_negative += float(x)
            count_negative += 1
        elif float(x) > 0:
            average_positive += float(x)
            count_positive += 1

    if count_negative != 0:
        average_negative /= count_negative

    if count_positive != 0:
        average_positive /= count_positive

    label_out["text"] = ""
    label_out["text"] = ("Среднее арифметическое\n "
                        "положительных чисел = {0:.3f} \n\n"
                        "Среднее арифметическое\n "
                        "отрицательных чисел = {1:.3f}".format(average_positive,
                                                               average_negative))

                        
def clean_field(label_out):
    label_out["text"] = ""


def bind_calculate(event):
    calculate(entry_in, result_label)


def bind_cleaner(event):
    clean_field(result_label)


root = Tk()
root.geometry("300x350+400+200")
root.resizable(False, False)
root.title("ListFinder")
root.config(bg="#000080")

welcome_label = Label(text="\nВведите список чисел:\n",
                      bg="#000080",
                      fg="white",
                      font="consolas 10 bold")
welcome_label.pack()

entry_in = Entry(root, width=40)
entry_in.pack()

strip_label = Label(text="",
                    bg="#000080")
strip_label.pack()

calculate_btn = Button(text="Перевод",
                       width=7,
                       height=2,
                       font="consolas 10 bold",
                       bg="white",
                       fg="#0ad325",
                       command=lambda: calculate(entry_in, result_label))
calculate_btn.pack()

result_label_welcome = Label(text="\nРезультат:\n",
                             bg="#000080",
                             fg="white",
                             font="consolas 10 bold")
result_label_welcome.pack()

result_label = Label(text="",
                     bg="#000080",
                     fg="white",
                     font="consolas 10 bold")
result_label.pack()

entry_in.focus_set()
entry_in.bind("<Return>", bind_calculate)
entry_in.bind("<Key>", bind_cleaner)

root.mainloop()
