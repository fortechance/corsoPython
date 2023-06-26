
import PySimpleGUI as ps
from myTables import *

def doDashboard():

    ps.theme("green")


    layout = [
            [ps.Text('Benvenuto'),ps.Text("user"),ps.Text("password")],
            
        ]
    
    windows = ps.Window('Daskboard',layout)

    while True:

        event, values = windows.read()

        if event == ps.WIN_CLOSED or event == 'Exit':
            
            break

        elif event == 'Login':
            pass
            

    windows.close()

doDashboard()
    
     

    
            
    

        
            
 
    