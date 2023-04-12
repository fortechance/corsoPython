#ordine per far funzionare un input: prima definisci la variabile che si compila tramite input, poi metti il test e infine il print con la variabile

nome = input("come ti chiami?")

test = input("sei sicuro?")
if (test=="no"):
	nome = input("ripeti")
else: 
	print("nome verificato")

print(f"il tuo nome è {nome}")