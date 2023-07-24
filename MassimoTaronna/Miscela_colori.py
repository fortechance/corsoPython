def mix_colors(colors, quantities):
    if len(colors) != len(quantities):
        raise ValueError("La lista dei colori e delle quantità devono avere la stessa lunghezza.")
    
    total_quantity = sum(quantities)
    mixed_color = [0, 0, 0]  # Inizializzo il colore risultante come nero (0, 0, 0)

    for color, quantity in zip(colors, quantities):
        weight = quantity / total_quantity
        for i in range(3):
            mixed_color[i] += color[i] * weight
    
    return mixed_color

def main():
    colors = []
    quantities = []
    num_colors = int(input("Quanti colori vuoi miscelare? "))

    for i in range(num_colors):
        r = int(input(f"Inserisci la quantità di rosso (0-255) per il colore {i+1}: "))
        g = int(input(f"Inserisci la quantità di verde (0-255) per il colore {i+1}: "))
        b = int(input(f"Inserisci la quantità di blu (0-255) per il colore {i+1}: "))
        quantity = int(input(f"Inserisci la quantità (in ml) per il colore {i+1}: "))

        colors.append((r, g, b))
        quantities.append(quantity)

    mixed_color = mix_colors(colors, quantities)
    print("\nIl colore risultante della miscelazione è:")
    print(f"Rosso: {mixed_color[0]}, Verde: {mixed_color[1]}, Blu: {mixed_color[2]}")

if __name__ == "__main__":
    main()
