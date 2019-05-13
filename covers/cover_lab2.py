from tkinter import *

def bubble_sort(in_list):
    for i in range(len(in_list) - 1):
        for j in range(i + 1, len(in_list)):
            if in_list[j] < in_list[i]:
                in_list[i], in_list[j] = in_list[j], in_list[i]

    return in_list

def sort_tkinter(entry_in, label_out):

    get_list = [int(x) for x in entry_in.get().strip().split()]

    get_list = bubble_sort(get_list)

    label_out["text"] = ""
    label_out["text"] = get_list
                        
def clean_field(label_out):
    label_out["text"] = ""


def bind_sort(event):
    sort_tkinter(entry_in, result_label)


def bind_cleaner(event):
    clean_field(result_label)


root = Tk()
root.geometry("300x350+400+200")
root.resizable(False, False)
root.title("BubbleSort")
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

calculate_btn = Button(text="Сортировка",
                       width=10,
                       height=2,
                       font="consolas 10 bold",
                       bg="white",
                       fg="#0ad325",
                       command=lambda: sort_tkinter(entry_in, result_label))
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
entry_in.bind("<Return>", bind_sort
              )
entry_in.bind("<Key>", bind_cleaner)

root.mainloop()
