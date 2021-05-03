import PySimpleGUI as sg
import PrimerCSV
import SegundoCSV

sg.theme('NeutralBlue')

layout = [
    [sg.Text("Elija uno de estos archivos CSV y "
            "\naccederá a varias opciones para " +
            "\ngenerar archivos JSON",justification='center',text_color='Black',font=("Arial",13))],
    [sg.Button("VENTAS DE VIDEO JUEGOS",key="-CSV1-",size=(30,3))],
    [sg.Button("PREMIOS NOBEL",key="-CSV2-",size=(30,3))],
    [sg.Button("SALIR",key='-EXIT-',size=(30,3),pad=(0,30))]
    ]

window = sg.Window("Actividad 1 por PythonPlus",layout=layout,disable_close=True,disable_minimize=True,
        element_justification='c',size=(350,350))

while True:
    event,values = window.read()
    if event in ("-EXIT-"):
        break
    if event in ("-CSV1-"):
        window.hide()
        PrimerCSV.start()
        window.un_hide()
    elif event in ("-CSV2-"):
        window.hide()
        SegundoCSV.start()
        window.un_hide()

window.close()