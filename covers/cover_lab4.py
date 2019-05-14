from tkinter import *
from tkinter import messagebox
from itertools import *


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


def get_int_list(in_entry):
    """ Функция формирования целочисленного списка.

    Передаваемые параметры:
    * in_entry - поле ввода, из которого формируется список

    Возвращаемые значения:
    * int_list - сформированный целочисленный список

    """

    try:
        int_list = [int(x) for x in in_entry.get().strip().split()]

        if len(int_list) == 0 or isinstance(int_list, (str, type(None))):
            raise ValueError

        return int_list

    except ValueError:
        messagebox.showerror("Ошибка ввода данных", "Данные введены "
                                                    "некорректно, проверьте "
                                                    "правильность ввода!")


def draw_triangle(first_dot_set_entry, second_dot_set_entry):
    first_dot_set = get_int_list(first_dot_set_entry)
    second_dot_set = get_int_list(second_dot_set_entry)

    if first_dot_set and second_dot_set:
        if len(second_dot_set) % 3:
            messagebox.showinfo("Неполнота данных", "Координаты точек введены "
                                                    "не полностью, проверьте "
                                                    "правильность ввода!")

            return False

        first_dot_set_x = first_dot_set[::2]
        first_dot_set_y = first_dot_set[1::2]

        second_dot_set_x = second_dot_set[::2]
        second_dot_set_y = second_dot_set[1::2]

        all_dot_set_x = first_dot_set_x + second_dot_set_x
        all_dot_set_y = first_dot_set_y + second_dot_set_y

        first_dot_tuple_set = [(first_dot_set_x[i], first_dot_set_y[i]) for i in range(len(first_dot_set_x))]

        triangle_dot_tuple_set = [(second_dot_set_x[i], second_dot_set_y[i],
                                   second_dot_set_x[i + 1], second_dot_set_y[i + 1],
                                   second_dot_set_x[i + 2], second_dot_set_y[i + 2])
                                  for i in range(0, len(second_dot_set_x), 3)]

        result_set = None
        final_triangle_cross_count = 0

        for dot_pair in combinations(first_dot_tuple_set, 2):
            triangle_cross_count = 0

            def line_fx(x, A, B):
                return A * x + B

            def line_kx(x1, x2, y1, y2):
                if x2 - x1 == 0:
                    return (y2 - y1) / (x2 - (x1 + 0.000001)), -(x1 * (y2 - y1)) / (x2 - (x1 + 0.000001)) + y1
                else:
                    return (y2 - y1) / (x2 - x1), -(x1 * (y2 - y1)) / (x2 - x1) + y1

            def find_cross(A, B, x1, y1, x2, y2):
                if (y1 - line_fx(x1, A, B)) * (y2 - line_fx(x2, A, B)) <= 0:
                    return True
                else:
                    return False

            coef_tuple = line_kx(dot_pair[0][0], dot_pair[1][0], dot_pair[0][1], dot_pair[1][1])

            for i in range(len(triangle_dot_tuple_set)):
                if find_cross(coef_tuple[0], coef_tuple[1], triangle_dot_tuple_set[i][0], triangle_dot_tuple_set[i][1],
                              triangle_dot_tuple_set[i][2], triangle_dot_tuple_set[i][3]):
                    triangle_cross_count += 1
                    continue
                if find_cross(coef_tuple[0], coef_tuple[1], triangle_dot_tuple_set[i][2], triangle_dot_tuple_set[i][3],
                              triangle_dot_tuple_set[i][4], triangle_dot_tuple_set[i][5]):
                    triangle_cross_count += 1
                    continue
                if find_cross(coef_tuple[0], coef_tuple[1], triangle_dot_tuple_set[i][0], triangle_dot_tuple_set[i][1],
                              triangle_dot_tuple_set[i][4], triangle_dot_tuple_set[i][5]):
                    triangle_cross_count += 1
                    continue

            if triangle_cross_count > final_triangle_cross_count:
                final_triangle_cross_count = triangle_cross_count
                result_set = dot_pair

        if result_set is None:
            messagebox.showinfo("Что-то пошло не так", "Прямая не найдена, "
                                                       "попробуйте другие точки!")

            return False

        messagebox.showinfo("О фигурах", "Красные точки - точки из первого множества\n"
                                         "Синие треугольники - треугольники из второго множества")

        """ Организация визуализации магического треугольника. """
        draw_window = Toplevel(root)
        draw_window.grab_set()
        draw_window.geometry("800x600+425+250")
        draw_window.resizable(False, False)
        draw_window.title("TriangleDots")
        draw_window.config(bg="white")

        draw_canvas = Canvas(draw_window, width=800, height=600, bg="white")
        draw_canvas.focus_set()
        draw_canvas.pack()

        """ Масштабирование графика. """
        winx = 800
        winy = 600

        xmax = all_dot_set_x[0]
        xmin = all_dot_set_x[0]

        ymax = all_dot_set_y[0]
        ymin = all_dot_set_y[0]

        for i in range(len(all_dot_set_x)):
            if all_dot_set_x[i] > xmax:
                xmax = all_dot_set_x[i]
            if all_dot_set_x[i] < xmin:
                xmin = all_dot_set_x[i]
            if all_dot_set_y[i] > ymax:
                ymax = all_dot_set_y[i]
            if all_dot_set_y[i] < ymin:
                ymin = all_dot_set_y[i]

        scalex = (winx - 20) / (xmax - xmin)
        scaley = (winy - 20) / (ymax - ymin)

        offsetx = -xmin * scalex + 10
        offsety = -ymin * scaley + 10

        """ Отрисовка точек второго множества. """
        for i in range(len(triangle_dot_tuple_set)):
            x_new = triangle_dot_tuple_set[i][0] * scalex + offsetx
            y_new = winy - (triangle_dot_tuple_set[i][1] * scaley + offsety)

            x1_new = triangle_dot_tuple_set[i][2] * scalex + offsetx
            y1_new = winy - (triangle_dot_tuple_set[i][3] * scaley + offsety)

            draw_canvas.create_line(x_new, y_new, x1_new, y1_new, width=4, fill="blue")

            x_new = triangle_dot_tuple_set[i][2] * scalex + offsetx
            y_new = winy - (triangle_dot_tuple_set[i][3] * scaley + offsety)

            x1_new = triangle_dot_tuple_set[i][4] * scalex + offsetx
            y1_new = winy - (triangle_dot_tuple_set[i][5] * scaley + offsety)

            draw_canvas.create_line(x_new, y_new, x1_new, y1_new, width=4, fill="blue")

            x_new = triangle_dot_tuple_set[i][4] * scalex + offsetx
            y_new = winy - (triangle_dot_tuple_set[i][5] * scaley + offsety)

            x1_new = triangle_dot_tuple_set[i][0] * scalex + offsetx
            y1_new = winy - (triangle_dot_tuple_set[i][1] * scaley + offsety)

            draw_canvas.create_line(x_new, y_new, x1_new, y1_new, width=4, fill="blue")

        x_cord = result_set[0][0] * scalex + offsetx
        y_cord = winy - (result_set[0][1] * scaley + offsety)

        x1_cord = result_set[1][0] * scalex + offsetx
        y1_cord = winy - (result_set[1][1] * scaley + offsety)

        draw_canvas.create_line(x_cord, y_cord, x1_cord, y1_cord, width=4, fill="green")

        """ Отрисовка точек первого множества. """
        for i in range(len(first_dot_set_x)):
            x_new = first_dot_set_x[i] * scalex + offsetx
            y_new = winy - (first_dot_set_y[i] * scaley + offsety)
            draw_canvas.create_oval(x_new - 6, y_new - 6, x_new + 6, y_new + 6, fill="red")


def about():
    """" Вывод окна "О программе" """
    about_window = Toplevel(root)
    about_window.grab_set()
    about_window.geometry("330x200+425+250")
    about_window.resizable(False, False)
    about_window.title("О TriangleDots")
    about_window.config(bg="#000080")

    about_label1 = Label(about_window,
                         text="Kononenko Sergey ICS7-23B",
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
root.geometry("400x200+400+200")
root.resizable(False, False)
root.title("TriangleDots")

""" Создание меню. """
main_menu = Menu(root)
root.config(menu=main_menu, bg="#000080")

clean_menu = Menu(main_menu, tearoff=0)
clean_menu.add_command(label="Очистить поле ввода точек первого множества",
                       command=lambda: clean_entry(first_dot_set_entry))
clean_menu.add_command(label="Очистить поле ввода точек второго множества",
                       command=lambda: clean_entry(second_dot_set_entry))
clean_menu.add_separator()
clean_menu.add_command(label="Очистить поле ввода точек обоих множеств",
                       command=lambda: clean_entry(first_dot_set_entry,
                                                   second_dot_set_entry))

action_menu = Menu(main_menu, tearoff=0)
action_menu.add_command(label="Визуализировать",
                        command=lambda: draw_triangle(first_dot_set_entry,
                                                      second_dot_set_entry))

about_menu = Menu(main_menu, tearoff=0)
about_menu.add_command(label="О программе", command=lambda: about())

main_menu.add_cascade(label="Визуализация", menu=action_menu)
main_menu.add_cascade(label="Очистка", menu=clean_menu)
main_menu.add_cascade(label="Справка", menu=about_menu)

""" Организация UI. """
welcome_label = Label(root,
                      text="Сейчас найдём прямую",
                      font="consolas 10 bold",
                      bg="white",
                      fg="#000080")
welcome_label.place(x=200, y=20, anchor="center")

first_dot_set_label = Label(root,
                            text="Введите координаты точек множества для прямых",
                            font="consolas 10 bold",
                            bg="#000080",
                            fg="white")
first_dot_set_label.place(x=200, y=45, anchor="center")

first_dot_set_start = "x1 y1 ..."
first_dot_set_entry = Entry(root, width=60)
first_dot_set_entry.insert(0, first_dot_set_start)
first_dot_set_entry.place(x=200, y=65, anchor="center")

second_dot_set_label = Label(root,
                             text="Введите координаты точек множества для треугольников",
                             font="consolas 10 bold",
                             bg="#000080",
                             fg="white")
second_dot_set_label.place(x=200, y=85, anchor="center")

second_dot_set_start = "x1 y1 ..."
second_dot_set_entry = Entry(root, width=60)
second_dot_set_entry.insert(0, second_dot_set_start)
second_dot_set_entry.place(x=200, y=105, anchor="center")

draw_button = Button(root, text="Визуализировать",
                     width=16,
                     height=2,
                     font="consolas 10 bold",
                     bg="white",
                     fg="#0ad325",
                     command=lambda: draw_triangle(first_dot_set_entry,
                                                   second_dot_set_entry))
draw_button.place(x=130, y=145, anchor="center")

exit_button = Button(root, text="Выйти",
                     width=16,
                     height=2,
                     font="consolas 10 bold",
                     bg="white",
                     fg="#ff0000",
                     command=lambda: exit_run(root))
exit_button.place(x=270, y=145, anchor="center")

root.mainloop()
