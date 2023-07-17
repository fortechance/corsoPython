try: import Tkinter as tk                   # Py2
except ImportError: import tkinter as tk    # Py3

class Applicazione:

    def __init__ (self):

        self.form1 = tk.Tk()
        self.form1.geometry('1000x750+500+20')
        self.form1.resizable(width=False, height=False)
        self.form1.title("GESTIONE AUTOSALONE"  )
        # Frame alto con pulsanti ---------------------------------------------
        self.frame1 = tk.Frame(self.form1, bd=1, relief="raised")
        self.frame1.grid(row=0, column=0, sticky="we")
        self.bottone1 = tk.Button(self.frame1, text="Inserisce", bg="#66b3ff", fg="white", font=("Arial",16, "bold") )
        self.bottone1.grid(row=0, column=0,  pady=1)
        self.bottone2 = tk.Button(self.frame1, text="Varia", bg="#66b3ff", fg="white", font=("Arial",16, "bold"))
        self.bottone2.grid(row=0, column=1, pady=1, )
        self.bottone3 = tk.Button(self.frame1, text="Cancella",  bg="#66b3ff", fg="white", font=("Arial",16, "bold")  )
        self.bottone3.grid(row=0, column=2, pady=1, )
        self.bottone4 = tk.Button(self.frame1, text="Stampa",  bg="#66b3ff", fg="white", font=("Arial",16, "bold") )
        self.bottone4.grid(row=0, column=3, pady=1)
        self.bottone5 = tk.Button(self.frame1, text="Uscita", bg="#66b3ff", fg="white", font=("Arial", 16, "bold"))
        self.bottone5.grid(row=0, column=4, pady=5, sticky="w")
        self.bottone6 = tk.Button(self.frame1, text="Ricerca", bg="#66b3ff", fg="white", font=("Arial", 16, "bold"))
        self.bottone6.grid(row=0, column=5, pady=5, padx=50, sticky="w")


        # Frame centrale --------------------------------
        self.frame2 = tk.Frame(
            self.form1, height=700, width=1000,
            bd=1, relief="raised", bg="white")

        # prova gestione dati veicolo

        self.labelcaratteristiche = tk.Label(self.frame2, text=" CARATTERISTICHE ", bg="#66b3ff", fg="white", font=("Arial", 15, "bold"))
        self.labelcaratteristiche.grid(row=0, column=0, padx=10, pady=10)
        self.labeltarga = tk.Label(self.frame2, text=" Targa                     ", bg="#66b3ff", fg="white", font=("Arial", 16, "bold"))
        self.labeltarga.grid(row=1, column=0, padx=10, pady=1)

        '''
        self.entry.labeltarga = Entry(self)
        self.entry.labeltarga.grid(row=1, column=2)
        '''
        ''''
        self.label_nome_utente = Label(self, text="Nome Utente")
        self.entry_nome_utente = Entry(self)
        self.entry_nome_utente.grid(row=0, column=1)
        '''

        self.labelcilindrata = tk.Label(self.frame2, text=" Cilindrata               ", bg="#66b3ff", fg="white", font=("Arial", 16, "bold"))
        self.labelcilindrata.grid(row=2, column=0, padx=10, pady=1)
        self.labelcolore = tk.Label(self.frame2, text=" Colore                    ", bg="#66b3ff", fg="white", font=("Arial", 16, "bold"))
        self.labelcolore.grid(row=3, column=0, padx=10, pady=1)
        self.labelposti = tk.Label(self.frame2, text=" Posti                      ", bg="#66b3ff", fg="white", font=("Arial", 16, "bold"))
        self.labelposti.grid(row=4, column=0, padx=10, pady=1)

        self.labelanno = tk.Label(self.frame2, text=" Anno                      ", bg="#66b3ff", fg="white", font=("Arial", 16, "bold"))
        self.labelanno.grid(row=5, column=0, padx=10, pady=1)
        self.labelalimentazione = tk.Label(self.frame2, text=" Alimentazione       ", bg="#66b3ff", fg="white", font=("Arial", 16, "bold"))
        self.labelalimentazione.grid(row=6, column=0, padx=10, pady=1)
        self.labelconsumo = tk.Label(self.frame2, text=" Consumo (km/l)    ", bg="#66b3ff", fg="white",font=("Arial", 16, "bold"))
        self.labelconsumo.grid(row=7, column=0, padx=10, pady=1)

        self.labeltipologia = tk.Label(self.frame2, text=" Tipologia               ", bg="#66b3ff", fg="white",font=("Arial", 16, "bold"))
        self.labeltipologia.grid(row=8, column=0, padx=10, pady=1)

        self.labelutilizzodisabili = tk.Label(self.frame2, text=" Utilizzo disabili      ", bg="#66b3ff", fg="white", font=("Arial", 16, "bold"))
        self.labelutilizzodisabili.grid(row=9, column=0, padx=10, pady=1)


        self.frame2.grid_propagate(False)
        #self.frame2.grid_rowconfigure(0, weight=2)
        #self.frame2.grid_columnconfigure(0, weight=2)
        self.frame2.grid(row=1, column=0)



        # Frame basso con label -----------------------------------------------
        self.frame3 = tk.Frame(self.form1, bd=1, relief="raised")
        self.frame3.grid(row=2, column=0, sticky="we")
        self.label2 = tk.Label(self.frame3, text="Segnalazioni : ")
        self.label2.grid(row=0, column=0, padx=4, pady=4)

    def start(self):
        self.form1.mainloop()

app = Applicazione()
app.start()
