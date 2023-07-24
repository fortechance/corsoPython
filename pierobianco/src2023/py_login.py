import PySimpleGUI as sg
import subprocess
import os

sg.set_options(font=('Arial Bold', 16))



# Dizionario degli utenti con le relative password ed email
utenti = {
    'utente1': {'password': 'uno', 'email': 'pippo@pippo.it'},
    'utente2': {'password': 'due', 'email': 'pluto@pluto.it'},
    'utente3': {'password': 'tre', 'email': 'pp@pp.it'},
    'utente4': {'password': 'quattro', 'email': 'aa@aa.it'},
    'utente5': {'password': 'cinque', 'email': 'cc@pcc.it'}
}

basepath = os.path.dirname(__file__)
basepath = os.path.join(basepath, '..\\img2023')

#basepath = f'{basepath}\\..\\img2023'
print(basepath)

# Definizione del layout della finestra di accesso
layout = [
    [
        sg.Image(f'{basepath}\\modit32.png', pad=(0, 0), size=(1150, 900)),
        sg.Column([
            [sg.Image(f'{basepath}\\lg_modit.png', pad=((190, 220,), (0, 290)), size=(300, 190))],
            [sg.Text('Username:'), sg.Input(key='-USERNAME-')],
            [sg.Text('Password:'), sg.Input(key='-PASSWORD-', password_char='*')],
            [sg.HorizontalSeparator()],
            [sg.Stretch(), sg.Button('Accedi', button_color=('white', '#FF8DC7'), pad=((0, 5), 10), size=(10, 1))]
        ], justification='center')
    ]
]

# Creazione della finestra di accesso
window = sg.Window('Login', layout, size=(None, None), element_justification='c')

# Loop principale per gestire gli eventi della finestra
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Accedi':
        username = values['-USERNAME-']
        password = values['-PASSWORD-']
        # print(username);
        # print(password);
        if username in utenti and password == utenti[username]['password']:
            sg.popup(f'Accesso consentito! Email: {utenti[username]["email"]}')
            script_dir = os.path.dirname(os.path.abspath(__file__))
            script_path = os.path.join(script_dir, "py_menu.py")
            subprocess.Popen(["python", script_path])
            print(script_path);
            #os.chdir("C:/Users/modit/PycharmProjects/corsopython/venv")
            #subprocess.run(["C:/Users/modit/PycharmProjects/corsopython/venv/vbmenu_22.py"])
            ## os.listdir()
            ## break
        else:
            sg.popup('Accesso negato. Riprova.')

window.close()
