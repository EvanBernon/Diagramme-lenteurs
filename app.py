import tkinter as tk
from tkinter import ttk
from numpy import cos, sin, tan, min, arccos, abs, linspace, pi
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Vitesses fixes des deux milieux
cl1, ct1 = 6300, 3100  # Aluminium
cl2, ct2 = 4370, 2100  # Laiton

# Fonction de traçage du diagramme des lenteurs
def plot_graph():
    try:
        # Récupération des entrées utilisateur
        angle_degre = float(angle_entry.get())
        incidence = incidence_var.get()

        # Conversion de l'angle en radians
        angle = (90 - angle_degre) * pi / 180

        # Définition de l'indice en fonction de l'onde incidente
        indice = 2 if incidence == "Longitudinale" else 3

        # Définition des vitesses et du tracé
        vitesses = [cl1, ct1, -cl2, -ct2]
        theta = linspace(0, pi, 100)
        pente = tan(angle)
        incident = linspace(-cos(angle) / abs(vitesses[indice]), 0, 50)

        # Nettoyage de l'ancienne figure
        ax.clear()

        # Tracé des courbes de lenteur
        for i in range(len(vitesses)):
            x = (1 / vitesses[i]) * cos(theta)
            y = (1 / vitesses[i]) * sin(theta)
            ax.plot(y, x, 'b' if i % 2 == 0 else 'r')

        ax.set_aspect('equal')
        ax.axvline(x=0, c='black')

        # Annotations
        ax.annotate('Aluminium', xy=(0.25 / min(abs(vitesses)), -1 / min(abs(vitesses))))
        ax.annotate('Laiton', xy=(-0.75 / min(abs(vitesses)), -1 / min(abs(vitesses))))

        # Tracé des ondes réfléchies et transmises
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
        ax.set_title(f"Diagramme des lenteurs \n Onde incidente : {incidence} \n Angle : {angle_degre}°")

        canvas.draw()
    except ValueError:
        print("Veuillez entrer un angle valide.")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Interface Ondes et Lenteurs")

# Saisie de l'angle
tk.Label(root, text="Angle d'incidence (°):").pack()
angle_entry = tk.Entry(root)
angle_entry.insert(0, "60")
angle_entry.pack()

# Sélection du type d'onde
tk.Label(root, text="Type d'onde incidente :").pack()
incidence_var = tk.StringVar(value="Transverse")
incidence_menu = ttk.Combobox(root, textvariable=incidence_var, values=["Longitudinale", "Transverse"])
incidence_menu.pack()

# Bouton pour tracer
plot_button = ttk.Button(root, text="Tracer", command=plot_graph)
plot_button.pack()

# Création de la figure matplotlib
fig, ax = plt.subplots(figsize=(5, 5))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Lancement de l'interface Tkinter
root.mainloop()
