import tkinter as tk

def mix_colors():
    red = red_slider.get()
    green = green_slider.get()
    blue = blue_slider.get()

    mixed_color = "#%02x%02x%02x" % (red, green, blue)
    canvas.config(bg=mixed_color)

def main():
    window = tk.Tk()
    window.geometry("800x600")
    window.title("Miscelatore di Colori Primari")

    global red_slider, green_slider, blue_slider, canvas

    red_label = tk.Label(window, text="Rosso")
    red_label.pack()
    red_slider = tk.Scale(window, from_=0, to=255, orient=tk.HORIZONTAL, command=mix_colors)
    red_slider.pack()

    green_label = tk.Label(window, text="Verde")
    green_label.pack()
    green_slider = tk.Scale(window, from_=0, to=255, orient=tk.HORIZONTAL, command=mix_colors)
    green_slider.pack()

    blue_label = tk.Label(window, text="Blu")
    blue_label.pack()
    blue_slider = tk.Scale(window, from_=0, to=255, orient=tk.HORIZONTAL, command=mix_colors)
    blue_slider.pack()

    canvas = tk.Canvas(window, width=300, height=200)
    canvas.pack()

    mix_colors()  # Inizializza il colore miscelato in base ai valori iniziali degli slider

    

if __name__ == "__main__":
    window.mainloop()
