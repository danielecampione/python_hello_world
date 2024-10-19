import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import itertools

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

def animate():
    global img_label, img_sequence
    img_label.config(image=next(img_sequence))
    root.after(100, animate)

def move_text():
    global dx, dy
    x, y = text_label.winfo_x(), text_label.winfo_y()
    if x + dx < 0 or x + dx + text_label.winfo_width() > root.winfo_width():
        dx = -dx
    if y + dy < 0 or y + dy + text_label.winfo_height() > root.winfo_height():
        dy = -dy
    text_label.place(x=x+dx, y=y+dy)
    root.after(50, move_text)

def change_style(style_name):
    style.theme_use(style_name)

def show_style_chooser():
    style_chooser = tk.Toplevel(root)
    style_chooser.title("Scegli lo stile")
    style_chooser.geometry("300x200")
    center_window(style_chooser)

    label = ttk.Label(style_chooser, text="Seleziona uno stile:", font=("Helvetica", 12))
    label.pack(pady=10)

    for style_name in style.theme_names():
        button = ttk.Button(style_chooser, text=style_name, command=lambda name=style_name: change_style(name))
        button.pack(pady=5)

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

# Creazione del pulsante "Cambia stile"
style_button = ttk.Button(root, text="Cambia stile", command=show_style_chooser)
style_button.pack(pady=10)

# Caricamento delle immagini per l'animazione
frames = [ImageTk.PhotoImage(file=f"frame_{i}.png") for i in range(1, 6)]  # Assicurati di avere le immagini frame_1.png, frame_2.png, ecc.
img_sequence = itertools.cycle(frames)
img_label = tk.Label(root)
img_label.pack()

# Avvio dell'animazione
animate()

# Creazione della scritta 3D "Benvenuto"
text_label = tk.Label(root, text="Benvenuto", font=("Helvetica", 32, "bold"), fg="blue")
text_label.place(x=50, y=50)

# Variabili per il movimento della scritta
dx, dy = 2, 2

# Avvio del movimento della scritta
move_text()

# Posizionamento della finestra al centro del desktop
center_window(root)

# Creazione dello stile
style = ttk.Style()

# Avvio del loop principale della finestra
root.mainloop()
