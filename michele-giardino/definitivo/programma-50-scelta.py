import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, filedialog
import os
import subprocess

# Ottieni il percorso assoluto della cartella corrente
current_dir = os.path.dirname(os.path.abspath(__file__))
img = 'banner.png'
image_path = os.path.join(current_dir, img)

def open_pageCliente():
    root.destroy()
    subprocess.run(["python", "programma-50-cliente.py"])

def open_pageAdmin():
    root.destroy()
    subprocess.run(["python", "programma-50-amministratore.py"])

def main():
    global root
    root = tk.Tk()
    root.title("Distributore del Sorriso")
    root.geometry("512x512")

    # Carica l'immagine
    image = tk.PhotoImage(file=image_path)

    # Mostra l'immagine in un Label
    image_label = tk.Label(root, image=image)
    image_label.pack()

    ttk.Label(root, text="Chi sei?").pack()

    # Frame per la riga
    row_frame = tk.Frame(root)
    row_frame.pack()

    # Prima colonna
    column1 = tk.Frame(row_frame)
    column1.pack(side=tk.LEFT, padx=10, pady=5)

    button1 = tk.Button(column1, text="Cliente", width=10, command=open_pageCliente)
    button1.pack()

    # Seconda colonna
    column2 = tk.Frame(row_frame)
    column2.pack(side=tk.RIGHT, padx=10, pady=5)

    button2 = tk.Button(column2, text="Amministratore", width=12, command=open_pageAdmin)
    button2.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
