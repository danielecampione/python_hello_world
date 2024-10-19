import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

def close_window():
    root.destroy()

def show_about():
    about_window = tk.Toplevel(root)
    about_window.title("Informazioni su...")
    about_window.geometry("300x200")
    center_window(about_window)
    
    # Effetto di dissolvenza
    for i in range(0, 101, 5):
        about_window.attributes("-alpha", i/100)
        about_window.update()
        about_window.after(10)
    
    label = ttk.Label(about_window, text="D. Campione", font=("Helvetica", 16))
    label.pack(expand=True)
    
    # Effetto di dissolvenza in uscita
    about_window.after(2000, lambda: fade_out(about_window))

def fade_out(window):
    for i in range(100, -1, -5):
        window.attributes("-alpha", i/100)
        window.update()
        window.after(10)
    window.destroy()

# Creazione della finestra principale
root = tk.Tk()
root.title("Finestra di esempio")

# Aggiunta di uno sfondo
bg_image = Image.open("background.jpg")  # Assicurati di avere un'immagine di sfondo
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# Creazione di un'etichetta con il messaggio "Ciao mondo"
label = ttk.Label(root, text="Ciao mondo", font=("Helvetica", 24), background="white")
label.pack(padx=20, pady=20)

# Creazione del pulsante "Chiudi"
close_button = ttk.Button(root, text="Chiudi", command=close_window)
close_button.pack(pady=10)

# Creazione del pulsante "Informazioni su..."
about_button = ttk.Button(root, text="Informazioni su...", command=show_about)
about_button.pack(pady=10)

# Posizionamento della finestra al centro del desktop
center_window(root)

# Avvio del loop principale della finestra
root.mainloop()
