import os
import json
import csv
from collections import Counter

import PySimpleGUI as sg


def display():
    """ Genera y retorna un diseño de pantalla para el menu de archivos de Premios Nobel """
    layout = [
        [sg.Text("Quiere generar un archivo JSON de...", justification='center', text_color='Black',font=('Arial',13))],
        [sg.Button("LAS MUJERES QUE GANARON \n UN PREMIO NOBEL DE LA PAZ",key="-1,mujeres_paz.json-",size=(30,3))],
        [sg.Button("HOMBRES ESTADOUNIDENSES QUE \n GANARON UN NOBEL DE ECONOMIA \n ANTES DE LOS 60 AÑOS",key="-2,hombres_economia.json-",size=(30,3))],
        [sg.Button("LAS 10 CIUDADES CON MAYOR \n CANTIDAD DE PREMIOS NOBEL",key="-3,ciudades_nobel.json-",size=(30,3))],
        [sg.Button("VOLVER",key="-SALIR-",size=(30,3),pad=(0,30))]
    ]
    return layout

def generar_opcion_1(datos):
    """ Genera una estructura con todas las mujeres que ganaron un Nobel de la Paz.
    Devuelve una lista de diccionarios con el nombre completo como clave y el año en el que lo ganaron y el pais donde
    nacio como valores. """
    lista = filter(lambda x: x[11]=='Female' and x[1]=='Peace',datos)
    lista = list(map(lambda x: {x[7]: {'Año':x[0], 'Pais de nacimiento':x[10]}},lista))
    return lista

def menos_60(premio,nacimiento):
    """ Recibe el año en el que se gano el premio y la fecha de nacimiento de una persona, y devuelve si tenia menos de
    70 años o no cuando se lo entregaron """
    a_nacimiento = int(nacimiento[:4]) # Nacimiento se ordena aaaa-mm-dd, por lo tanto solo necesito los primeros 4 digitos de esa cadena
    return ((int(premio) - a_nacimiento) < 60)

def generar_opcion_2(datos):
    """ Genera una estructura con todos los hombres nacidos en Estados Unidos que ganaron un nobel de economia antes de
    los 60 años.
    Retorna lista de diccionarios donde cada clave es el nombre y el valor la ciudad en la que nacio"""
    lista = filter(lambda x: x[11]=='Male' and x[1]=='Economics' and x[10]=='United States of America' and menos_60(x[0],x[8]),datos)
    lista = list(map(lambda x: {x[7]: x[9]},lista))
    return lista

def generar_opcion_3(datos):
    """ Devuelve una estructura con las 10 ciudades en las q mas gente que gano un Nobel nacio """
    lista = list(map(lambda x: x[9] , filter(lambda x: x[9] != '',datos))) # Elimina la posibilidad de que este vacio
    mas_comunes = Counter(lista).most_common(10)
    mas_comunes = list(map(lambda x: {x[0]: x[1]},mas_comunes))
    return mas_comunes

def manejador(evento):
    """ Recibe la key del boton que se apreto en la pantalla
    - Abre el archivo corresponiente al csv seleccionado
    - Consulta cual es el criterio por el que hay que ordenar
    - Se genera el archivo .json
    - Sale un Pop-Up avisando que ya se genero el archivo correspondiente """
    nobel_file_path = os.path.join(os.getcwd(),'TareaPythonPlus','ArchivosCSV','archive.csv')
    boton,file_name = evento.replace('-','').split(',')
    with open(nobel_file_path, 'r', encoding="utf-8") as archivo:
        reader = csv.reader(archivo)
        header = reader.__next__()
        if boton == '1':
            data = generar_opcion_1(reader)
        elif boton == '2':
            data = generar_opcion_2(reader)
        else:
            data = generar_opcion_3(reader)
    with open(os.path.join(os.getcwd(),'TareaPythonPlus','ArchivosJSON',file_name),'w',encoding="utf-8") as archivo_json:
        json.dump(data,archivo_json,indent=4,ensure_ascii=False)

def start():
    window = sg.Window("PREMIOS NOBEL",layout=display(),size=(400,350),disable_minimize=True,
                    disable_close=True,element_justification='c')
    while True:
        event,value = window.read()
        if event == '-SALIR-':
            break
        else: 
            manejador(event)
            sg.popup("Se creo el archivo deseado. Lo puede obervar en la carpeta 'ArchivosJSON'",title='Listo!')
    window.close()