nome = "Piero"
cognome = "Bullo"

#slicing -> posso prendere un elemento stringa e sezionarlo come se fosse ogni lettera un valore di una lista
iniziali = nome[0] + cognome[0]

# print (iniziali)

a = []
#aggiungo alla lista a il primo valore (a[0] = "Mannaggia")
a.append("Mannaggia")
b = a[0][:3]
c = a[0][1:2]
#b = stampa "Man" (dall'inizio prendi 3 valori)
#print (b)
#c = stampa "a" (dal 1 (a) al secondo valore (a))
print (c)


a = [4,7,12,45]
print (a) # stampa [4,7,12,45]
print (*a) # stampa 4 7 12 45

dict = {"b": 4, "a" : 8, "c" : "Ciao"}
print (dict)
print (*dict) #stampa solo le chiavi del dict

def Test (a, b, c): #stesse chiavi del dizionario
    
    print (a, b, c)


Test(**dict) #stampa i solo i valori legati alla chiave



# DATABASE - RENDERE PERSISTENTE I DATI

""" 1 utente = + portfoli

    1 portfoli = 1 solo utente

    utente è primario perchè non dipende da nulla, portfolio dipende da utente. """

""" PKesempio = chiave primaria
    
    FKesempio = chiave ereditata 
     
    Portfolio avrà una sua chiave primaria PKcodportfolio + una chiave ereditata da utente che sarà FKcodutente.

    Utente avrà una sola chiave primaria PKcodutente """

""" DA CMD =

C:\Users\Utente>ipconfig

Configurazione IP di Windows


Scheda Ethernet Ethernet:

   Stato supporto. . . . . . . . . . . . : Supporto disconnesso
   Suffisso DNS specifico per connessione: fortechance.local

Scheda LAN wireless Connessione alla rete locale (LAN)* 1:

   Stato supporto. . . . . . . . . . . . : Supporto disconnesso
   Suffisso DNS specifico per connessione:

Scheda LAN wireless Connessione alla rete locale (LAN)* 2:

   Stato supporto. . . . . . . . . . . . : Supporto disconnesso
   Suffisso DNS specifico per connessione:

Scheda LAN wireless Wi-Fi:

   Suffisso DNS specifico per connessione: fortechance.it
   Indirizzo IPv6 locale rispetto al collegamento . : fe80::b4c8:6b4c:98ba:c06c%12
   Indirizzo IPv4. . . . . . . . . . . . : 192.168.10.157
   Subnet mask . . . . . . . . . . . . . : 255.255.255.0
   Gateway predefinito . . . . . . . . . : 192.168.10.1

C:\Users\Utente>nslookup
Server predefinito:  firewall-studenti.fortechance.it
Address:  192.168.10.1

> ansa.it
Server:  firewall-studenti.fortechance.it
Address:  192.168.10.1

Risposta da un server non autorevole:
Nome:    ansa.it
Addresses:  95.216.36.96
          176.9.41.37
          78.46.16.208
          176.9.41.68
          46.4.22.185
          188.40.102.169
          144.76.223.21

> tracert www.ansa.it
Server:  ansa.it
Addresses:  78.46.16.208
          176.9.41.68
          46.4.22.185
          188.40.102.169
          144.76.223.21
          95.216.36.96
          176.9.41.37
Aliases:  www.ansa.it

DNS request timed out.
    timeout was 2 seconds.
DNS request timed out.
    timeout was 2 seconds.
*** Tempo scaduto per la richiesta a www.ansa.it """


# IPV4 esempio 192.168.10.254

""" 192.168.10.254 ----> python.hostingstudenti.fortechance.com 
    
    Nome:    python.hostingstudenti.fortechance.com
    Address:  192.168.10.16 ----> mia rete """

# DAtI ACCESSO : host: python.hostingstudenti.fortechance.com   schema: c73db   user: c73db    password: ocGB@QkcA8    porta: 3309

""" Connection = ("python........")
    
    CURSOR=connection.execute(sql)  """

""" SQL  """