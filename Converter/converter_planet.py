from tkinter.ttk import Label, Scale
import tkinter as tk
from tkinter import ttk



grav_const = 6.6743 * 10 ** -11
g = 9.80665


def calculate():
    a = float(grav_const * (float(m.get()) * list[choose_planet.get()][0] /
                            (list[choose_planet.get()][1] * 1000 + int(scale.get()) * 1000) ** 2) / g)
    res.delete(0, tk.END)
    res.insert(0, str(round(a)))


def on_scale(val):
    v = int(float(val))
    var.set(v)


list = {"Earth": [5973.6 * 10 ** 21, 12742 / 2],
        "Mars": [641.85 * 10 ** 21, 6780 / 2],
        "Venus": [4868.5 * 10 ** 21, 12103.6 / 2],
        "Sun": [1989100000 * 10 ** 21, 1392000 / 2],
        "Jupiter": [1898600 * 10 ** 21, 139822 / 2],
        "Pluto": [13.105 * 10 ** 21, 2376.6 / 2],
        "Uranus": [86832 * 10 ** 21, 50724 / 2],
        "Mercury": [330.2 * 10 ** 21, 4879.4 / 2],
        "Neptune": [102430 * 10 ** 21, 49244 / 2],
        "Moon": [73.5 * 10 ** 21, 3474.2 / 2]
        }
name = ("Earth", "Mars", "Venus", "Sun", "Jupiter", "Pluto", "Uranus", "Mercury", "Neptune", "Moon")

win = tk.Tk()
photo = tk.PhotoImage(file='planet.png')
photo_fon = tk.PhotoImage(file='fon.png')
background_label = Label(win, image=photo_fon)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

win.iconphoto(False, photo)

win.title("Your weight on other planet")
win.geometry("600x250+100+100")
win.resizable(False, False)

weight = tk.Label(win, text='What is your weight(kg):', relief=tk.RAISED, bd=5).grid(row=0, column=0, padx=5, pady=5)
result = tk.Label(win, text='Your weight on other planet(kg):', relief=tk.RAISED, bd=5).grid(row=1, column=0, padx=5,
                                                                                             pady=5)
hight = tk.Label(win, text='Above surface (km)', relief=tk.RAISED, bd=5).grid(row=2, column=0, columnspan=4, padx=5,
                                                                              pady=5)
planets = tk.Label(win, text='Choose another planet', relief=tk.RAISED, bd=5).grid(row=5, column=0, padx=5, pady=5)

scale = Scale(win, from_=0, to=5000, length=500, command=on_scale, value=0)
var = tk.IntVar()
scale_label = Label(win, text=0, textvariable=var)
scale.grid(row=4, column=0, columnspan=5, padx=50, pady=5)
scale_label.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

choose_planet = ttk.Combobox(win, values=name)
choose_planet.current(0)
choose_planet.grid(row=5, column=1, padx=5, pady=5)

m = tk.Entry(win, justify=tk.RIGHT)
m.insert(0, '50')
m.grid(row=0, column=1)

res = tk.Entry(win, justify=tk.RIGHT)
res.insert(0, "0")
res.grid(row=1, column=1)

ttk.Button(win, text='calculate', command=calculate).grid(row=6, column=0, padx=5, pady=5)

win.mainloop()
