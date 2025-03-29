import tkinter as tk
from tkinter import ttk
from numpy import cos, sin, tan, min, arccos, abs, linspace, pi
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_graph():
    try:
        cl1, ct1 = float(cl1_entry.get()), float(ct1_entry.get())
        cl2, ct2 = float(cl2_entry.get()), float(ct2_entry.get())
        angle_degre = float(angle_entry.get())
        incidence = incidence_var.get()

        angle = (90 - angle_degre) * pi / 180

        indice = 2 if incidence == "Longitudinale" else 3

        vitesses = [cl1, ct1, -cl2, -ct2]
        theta = linspace(0, pi, 100)
        pente = tan(angle)
        incident = linspace(-cos(angle) / abs(vitesses[indice]), 0, 50)

        ax.clear()

        for i in range(len(vitesses)):
            x = (1 / vitesses[i]) * cos(theta)
            y = (1 / vitesses[i]) * sin(theta)
            ax.plot(y, x, 'b' if i % 2 == 0 else 'r')

        ax.set_aspect('equal')
        ax.axvline(x=0, c='black')

        ax.annotate('Milieu 1', xy=(0.25 / min(abs(vitesses)), -1 / min(abs(vitesses))))
        ax.annotate('Milieu 2', xy=(-0.75 / min(abs(vitesses)), -1 / min(abs(vitesses))))

        ax.plot(incident * pente, incident)
        ax.axhline(-cos(angle) / abs(vitesses[indice]), linestyle='--', color="gray")
        ax.axhline(cos(angle) / abs(vitesses[indice]), linestyle='--', color="gray")

        ax.plot(incident * tan(arccos(cos(angle) / abs(vitesses[indice]) * ct2)), -incident)
        ax.plot(-incident * tan(arccos(cos(angle) / abs(vitesses[indice]) * ct1)), -incident)
        ax.plot(incident * tan(arccos(cos(angle) / abs(vitesses[indice]) * cl2)), -incident)
        ax.plot(-incident * tan(arccos(cos(angle) / abs(vitesses[indice]) * cl1)), -incident)

        ax.invert_yaxis()
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title(f"Onde incidente : {incidence} \n Angle : {angle_degre}°")

        canvas.draw()
    except ValueError:
        print("Veuillez entrer des valeurs valides.")

root = tk.Tk()
root.title("Interface Ondes et Lenteurs")

tk.Label(root, text="Célérité du milieu 1 (Longitudinale, Transverse):").pack()
cl1_entry = tk.Entry(root)
cl1_entry.insert(0, "6300")
cl1_entry.pack()
ct1_entry = tk.Entry(root)
ct1_entry.insert(0, "3100")
ct1_entry.pack()

tk.Label(root, text="Célérité du milieu 2 (Longitudinale, Transverse):").pack()
cl2_entry = tk.Entry(root)
cl2_entry.insert(0, "4370")
cl2_entry.pack()
ct2_entry = tk.Entry(root)
ct2_entry.insert(0, "2100")
ct2_entry.pack()

tk.Label(root, text="Angle d'incidence (°):").pack()
angle_entry = tk.Entry(root)
angle_entry.insert(0, "60")
angle_entry.pack()

tk.Label(root, text="Type d'onde incidente :").pack()
incidence_var = tk.StringVar(value="Transverse")
incidence_menu = ttk.Combobox(root, textvariable=incidence_var, values=["Longitudinale", "Transverse"])
incidence_menu.pack()

plot_button = ttk.Button(root, text="Tracer", command=plot_graph)
plot_button.pack()

fig, ax = plt.subplots(figsize=(5, 5))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

root.mainloop()