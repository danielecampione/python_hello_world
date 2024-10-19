import tkinter as tk

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

def close_window():
    root.destroy()

# Creazione della finestra principale
root = tk.Tk()
root.title("Finestra di esempio")

# Creazione di un'etichetta con il messaggio "Ciao mondo"
label = tk.Label(root, text="Ciao mondo")
label.pack(padx=20, pady=20)

# Creazione del pulsante "Chiudi"
close_button = tk.Button(root, text="Chiudi", command=close_window)
close_button.pack(pady=10)

# Posizionamento della finestra al centro del desktop
center_window(root)

# Avvio del loop principale della finestra
root.mainloop()
