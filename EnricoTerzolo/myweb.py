import PySimpleGUIWeb as sg


layout = [
    [sg.button('ok')]
]

window = sg.Window('titolo', layout,web_port = 80, web_ip = '0.0.0.0')

while True:

    events, values = window.read()
