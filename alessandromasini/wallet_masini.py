
import PySimpleGUI as ps


    
   

   

layout = [
        [ps.Text("Tipo Wallet",size=(10,1)),ps.Combo(["Scelta 1","Scelta 2"],size=(40,1))],
        [ps.Text("Codice",size=(10,1)),ps.Input(size=(40,1))],
        [ps.Text("Descrizione",size=(10,1)),ps.Input(size=(40,1))],
        [ps.Ok(),ps.Cancel()]
        ]

window = ps.Window('Tipo Wallet',layout,size = (640,480))

while True:

    event, values = window.read()

    if event == ps.WIN_CLOSED:
            break    
    
window.Close()

   
