import tkinter.messagebox as mb
from tkinter import *
from tkinter import colorchooser
from tkinter import ttk

from PIL import ImageGrab


class Example(Frame):
    dict_x = {}
    dict_y = {}
    matrix = [[None] * 3 for _ in range(8)]
    help_matrix = ["Start"]
    collision_lines = []
    collision_blocks = []
    collision_text = []
    colors = {}
    isUsedBlocks = True
    selected_color = "white"

    def __init__(self):
        super().__init__()
        self.init_ui()

    def choose_color(self):
        colors = colorchooser.askcolor(title="Color Chooser")
        if colors[1]:
            self.selected_color = colors[1]
        else:
            self.selected_color = "white"

    def delete(self):
        if self.collision_blocks[-1] is not None and self.collision_text[-1]:
            self.canvas.delete(self.collision_blocks[-1], self.collision_text[-1])
            value = self.help_matrix[-1]
            y, x = self.find(value)
            self.matrix[y][x] = None
            del self.dict_x[value]
            del self.dict_y[value]
            self.help_matrix.pop(-1)
            self.enter_prev['values'] = self.help_matrix
        self.canvas.delete(self.collision_lines[-1])
        self.collision_lines.pop(-1)
        self.collision_blocks.pop(-1)
        self.collision_text.pop(-1)

    def build(self, value, shape):
        x = self.dict_x[value]
        y = self.dict_y[value]
        if shape == "◆":
            width = 200
            height = 75
            x1, y1 = x, y
            x2, y2 = x + width / 2, y + height / 2
            x3, y3 = x, y + height
            x4, y4 = x - width / 2, y + height / 2
            coordinates = [x1 + 100, y1, x2 + 100, y2, x3 + 100, y3, x4 + 100, y4]

            block = self.canvas.create_polygon(coordinates, fill=self.selected_color, outline="black", width=1)
            text = self.canvas.create_text(((x + x + 200) / 2), ((y + y + 75) / 2), text=value, font=("Arial", 20))
            self.help_matrix.append(value)
            self.enter_prev['values'] = self.help_matrix
        elif shape == "⬬":
            block = self.canvas.create_oval(x, y, x + 200, y + 75, fill=self.selected_color, width=1)
            text = self.canvas.create_text(((x + x + 200) / 2), ((y + y + 75) / 2), text=value, font=("Arial", 20))
            self.help_matrix.append(value)
            self.enter_prev['values'] = self.help_matrix
        else:
            block = self.canvas.create_rectangle(x, y, x + 200, y + 75, fill=self.selected_color, width=1)
            text = self.canvas.create_text(((x + x + 200) / 2), ((y + y + 75) / 2), text=value, font=("Arial", 20))
            self.help_matrix.append(value)
            self.enter_prev['values'] = self.help_matrix
        self.collision_blocks.append(block)
        self.collision_text.append(text)
        self.colors[value]=self.selected_color
        print (self.colors)
        self.selected_color = "white"
    def find(self, value):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == value:
                    return i, j

        return None

    def size(self, prev_value, next_value, location, shape):
        if self.find(prev_value) is not None:
            loc_y, loc_x = self.find(prev_value)
            x_prev = self.dict_x.get(prev_value)
            y_prev = self.dict_y.get(prev_value)
            if self.find(next_value) is None:
                if (location == "🡻") and (loc_y + 1 != 8) and (self.matrix[loc_y + 1][loc_x] is None):
                    self.matrix[loc_y + 1][loc_x] = next_value
                    self.dict_x[next_value] = x_prev
                    self.dict_y[next_value] = y_prev + 100
                    line = self.canvas.create_line((x_prev + 200 / 2), y_prev + 75, (x_prev + 200 / 2), y_prev + 100)
                elif (location == "🡸") and (loc_x - 1 != -1) and (self.matrix[loc_y][loc_x - 1] is None):
                    self.matrix[loc_y][loc_x - 1] = next_value
                    self.dict_x[next_value] = x_prev - 250
                    self.dict_y[next_value] = y_prev
                    line = self.canvas.create_line((x_prev, (y_prev + 75 / 2), (x_prev - 50), (y_prev + 75 / 2)))
                elif (location == "🡺") and (loc_x + 1 != 3) and (self.matrix[loc_y][loc_x + 1] is None):
                    self.matrix[loc_y][loc_x + 1] = next_value
                    self.dict_x[next_value] = x_prev + 250
                    self.dict_y[next_value] = y_prev
                    line = self.canvas.create_line((x_prev + 200, (y_prev + 75 / 2), (x_prev + 250), (y_prev + 75 / 2)))
                elif (location == "🡿") and (loc_x - 1 != -1) and (loc_y + 1 != 8) and (
                        self.matrix[loc_y + 1][loc_x - 1] is None):
                    self.matrix[loc_y + 1][loc_x - 1] = next_value
                    self.dict_x[next_value] = x_prev - 250
                    self.dict_y[next_value] = y_prev + 100
                    line = self.canvas.create_line((x_prev, (y_prev + 75 / 2), (x_prev - 50), (y_prev + 100 + 75 / 2)))
                elif (location == "🡾") and (loc_x + 1 != 3) and (loc_y + 1 != 8) and (
                        self.matrix[loc_y + 1][loc_x + 1] is None):
                    self.matrix[loc_y + 1][loc_x + 1] = next_value
                    self.dict_x[next_value] = x_prev + 250
                    self.dict_y[next_value] = y_prev + 100
                    line = self.canvas.create_line(
                        (x_prev + 200, (y_prev + 75 / 2), (x_prev + 250), (y_prev + 100 + 75 / 2)))
                elif (location == "🡹") and (loc_y - 1 != -1) and (self.matrix[loc_y - 1][loc_x] is None):
                    self.matrix[loc_y - 1][loc_x] = next_value
                    self.dict_x[next_value] = x_prev
                    self.dict_y[next_value] = y_prev - 100
                    line = self.canvas.create_line((x_prev + 200 / 2), y_prev - 25, (x_prev + 200 / 2), y_prev)
                elif (location == "🡼") and (loc_x - 1 != -1) and (loc_y - 1 != -1) and (
                        self.matrix[loc_y - 1][loc_x - 1] is None):
                    self.matrix[loc_y - 1][loc_x - 1] = next_value
                    self.dict_x[next_value] = x_prev - 250
                    self.dict_y[next_value] = y_prev - 100
                    line = self.canvas.create_line((x_prev, (y_prev + 75 / 2), (x_prev - 50), (y_prev - 100 + 75 / 2)))
                elif (location == "🡽") and (loc_x + 1 != 3) and (loc_y - 1 != -1) and (
                        self.matrix[loc_y - 1][loc_x + 1] is None):
                    self.matrix[loc_y - 1][loc_x + 1] = next_value
                    self.dict_x[next_value] = x_prev + 250
                    self.dict_y[next_value] = y_prev - 100
                    line = self.canvas.create_line(
                        (x_prev + 200, (y_prev + 75 / 2), (x_prev + 250), (y_prev - 100 + 75 / 2)))
                self.build(next_value, shape)
                self.collision_lines.append(line)
            else:
                x_next = self.dict_x[next_value]
                y_next = self.dict_y[next_value]
                loc_yn, loc_xn = self.find(next_value)
                if loc_yn == loc_y:
                    if x_prev < x_next:
                        line = self.canvas.create_line(x_prev + 200, y_prev + 75 / 2, x_next, y_next + 75 / 2)
                    else:
                        line = self.canvas.create_line(x_prev, y_prev + 75 / 2, x_next + 200, y_next + 75 / 2)
                elif loc_xn == loc_x:
                    if y_prev < y_next:
                        line = self.canvas.create_line(x_prev + 200 / 2, y_prev + 75, x_next + 200 / 2, y_next)
                    else:
                        line = self.canvas.create_line(x_prev + 200 / 2, y_prev, x_next + 200 / 2, y_next + 75)
                else:
                    if x_prev < x_next and y_prev < y_next:
                        line = self.canvas.create_line(x_prev + 200, y_prev + 75 / 2, x_next, y_next + 75 / 2)
                    elif x_prev < x_next and y_prev > y_next:
                        line = self.canvas.create_line(x_prev + 200, y_prev + 75 / 2, x_next, y_next + 75 / 2)
                    elif x_prev > x_next and y_prev < y_next:
                        line = self.canvas.create_line(x_prev, y_prev + 75 / 2, x_next + 200, y_next + 75 / 2)
                    else:
                        line = self.canvas.create_line(x_prev, y_prev + 75 / 2, x_next + 200, y_next + 75 / 2)
                self.collision_lines.append(line)
                self.collision_text.append(None)
                self.collision_blocks.append(None)
        else:
            mb.showinfo("Warning", "Element don't found. Try again.")

    def save(self):
        counter = 0
        for row in self.matrix:
            if not all(value is None for value in row):
                counter += 1
        screenshot = ImageGrab.grab((440, 100, 1440, 200 + 112.5 * counter))  # 440 1440
        screenshot.save("block_diagram.png")

    def init_ui(self):

        self.dict_x["Start"] = 650
        self.dict_y["Start"] = 75
        self.matrix[0][1] = "Start"

        self.master.title("Block diagram")
        self.pack(fill=BOTH, expand=1)

        self.canvas = Canvas(self)

        btn_backspace = Button(text="Undo", font=("Arial", 20), activebackground="#CED3DC", fg="black",
                               command=lambda: self.delete())
        self.canvas.create_window(60, 440, anchor=NW, window=btn_backspace, width=190, height=50)
        btn_color = Button(text='Select a Color', font=("Arial", 20), activebackground="#CED3DC", fg="black",
                           command=self.choose_color)
        self.canvas.create_window(60, 495, anchor=NW, window=btn_color, width=190, height=50)
        btn_create = Button(text="Create", font=("Arial", 20), activebackground="#CED3DC", fg="black",
                            command=lambda: self.size(self.enter_prev.get(), enter_next.get(), direct_var.get(),
                                                      sh_var.get()))
        self.canvas.create_window(60, 550, anchor=NW, window=btn_create, width=190, height=50)
        btn_save = Button(text="Save", font=("Arial", 20), activebackground="#CED3DC", fg="black",
                          command=lambda: self.save())
        self.canvas.create_window(60, 605, anchor=NW, window=btn_save, width=190, height=50)

        prev_text = Label(text="Enter the previous node", font=("Arial", 20))
        self.canvas.create_window(160, 30, window=prev_text)

        shape_text = Label(text="Choose the position", font=("Arial", 20))
        self.canvas.create_window(145, 250, window=shape_text)

        selected_graph = StringVar()
        self.enter_prev = ttk.Combobox(self, textvariable=selected_graph, font=("Arial", 20))
        self.canvas.create_window(165, 80, window=self.enter_prev)
        self.enter_prev['values'] = self.help_matrix

        next_text = Label(text="Enter the next node", font=("Arial", 20))
        self.canvas.create_window(135, 130, window=next_text)

        enter_next = Entry(width=20, font=("Arial", 20))
        self.canvas.create_window(155, 180, window=enter_next)

        self.canvas.pack(fill=BOTH, expand=1)

        self.canvas.create_oval(650, 75, 850, 150, width=1, fill="white")
        self.canvas.create_text(((650 + 850) / 2), ((150 + 75) / 2), text="Start", font=("Arial", 20))

        direct_var = StringVar()
        direct_massive = ["🡸", "🡺", "🡹", "🡻", "🡼", "🡽", "🡾", "🡿"]
        enter_direct = ttk.Combobox(self, textvariable=direct_var, font=("Arial", 20))
        self.canvas.create_window(165, 300, window=enter_direct)
        enter_direct['values'] = direct_massive

        sh_var = StringVar()
        sh_massive = ["⬬", "▬", "◆"]
        shape_text = Label(text="Choose the shape", font=("Arial", 20))
        self.canvas.create_window(135, 350, window=shape_text)
        enter_shape = ttk.Combobox(self, textvariable=sh_var, font=("Arial", 20))
        self.canvas.create_window(165, 400, window=enter_shape)
        enter_shape['values'] = sh_massive


def run_gui():
    root = Tk()
    ex = Example()
    root.geometry("1440x900")
    root.state('zoomed')
    root.mainloop()


if __name__ == '__main__':
    run_gui()
