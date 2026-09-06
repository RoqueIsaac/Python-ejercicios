import tkinter as tk
#widgets modernos y mejorados, es un submodulo de tkinter y se tiene que importar por separado
from tkinter import ttk
from tkinter import messagebox

window = tk.Tk()
window.title("Mile to Km Converter")

window.minsize(width=300, height=170)
# geometry crea una ventana del tamaño especificado, sin embargo minsize establece un tamaño minimo,
# se puede hacer mas grande, pero no mas pequeño a minsize.
#window.geometry("400x200")
window.config(padx=20, pady=20)

L1 = tk.Label(window, text="Miles")
L1.grid(row=0, column=2)

L2 = tk.Label(window, text="Km")
L2.grid(row=1, column=2)

L3 = tk.Label(window, text="is equal to")
L3.grid(row=1, column=0)

L4 = tk.Label(window, text="0")
L4.grid(row=1, column=1)

entry = ttk.Entry(width=15)
entry.grid(row=0, column=1)

def calculate():
    try:
        miles = float(entry.get())
        km = 1.609 * miles
        L4.config(text=f"{km:,.3f} ", font="bold")
    except ValueError:
        messagebox.showerror("Error", "Please enter a number")

bt = ttk.Button(text="Calculate", command=calculate)
bt.grid(row=2, column=1)

#agregar padding a todos los widgets
for widget in window.winfo_children():
    #print(widget)
    widget.grid_configure(padx=10, pady=10)

window.mainloop()