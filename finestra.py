import tkinter as tk

# Creazione della finestra principale
root = tk.Tk()
root.title("Finestra di esempio")

# Creazione di un'etichetta con il messaggio "Ciao mondo"
label = tk.Label(root, text="Ciao mondo")
label.pack(padx=20, pady=20)

# Avvio del loop principale della finestra
root.mainloop()
