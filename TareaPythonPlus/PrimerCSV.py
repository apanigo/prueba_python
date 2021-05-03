import os
import csv
import json
from collections import Counter

import PySimpleGUI as sg

def display():
    """ Genera y devuelve un layout para el analisis del primer archivo """ 
    layout = [
        [sg.Text("Quiere generar un archivo JSON de...",justification='center',text_color='Black',font=("Arial",13))],
        [sg.Button("NOMBRE Y AÑO DE LANZAMIENTO \n DE 20 JUEGOS DE UBISOFT CON \n SOPORTE EN PS4",key="-1,ubisoft_ps4.json-",size=(30,3))],
        [sg.Button("LOS 10 GENEROS CON MAYOR CANTIDAD DE JUEGOS",key="-2,10_generos.json-",size=(30,3))],
        [sg.Button("LAS 15 EMPRESAS CON MAS VENTAS GLOBALES",key="-3,empresas_mas_ventas.json-",size=(30,3))],
        [sg.Button("VOLVER",key="-SALIR-",size=(30,3),pad=(0,30))]
    ]
    return layout

def generar_opcion_1(datos):
    """ Genera una estructura para enviar los datos a un archivo json con el criterio del primer boton.
    Devuelve una lista de 20 diccionarios donde la clave es el nombre de un juego y el valor su fecha de
    lanzamiento """
    lista = list(map(lambda x: {x[1]:x[3]}, filter(lambda x: x[2]=="PS4" and x[5]=="Ubisoft",datos)))
    return lista[:20]

def generar_opcion_2(datos):
    """ Recorre la estructura con los datos y genera una lista de diccionarios donde la clave es un genero de
    juego y el valor es la cantidad de juegos de ese genero """
    generos = list(map(lambda x: x[4], datos))
    diez_generos = Counter(generos).most_common(10)
    diez_generos = list(map(lambda x: {x[0]: x[1]}, diez_generos))
    return diez_generos

def generar_opcion_3(datos):
    """ Devuelve una lista de diccionarios de las empresas con mayores ventas """
    dicc_datos = {}
    for elem in datos:
        try:
            dicc_datos[elem[5]] += float(elem[10])
        except KeyError:
            dicc_datos[elem[5]] = float(elem[10])
    dicc_ordenado = sorted(dicc_datos.items(), key=lambda x: x[1], reverse=True)
    lista = list(map(lambda x: {x[0]:round(x[1],2)},dicc_ordenado))
    return lista[:15]


def manejador(event):
    """ Recibe la key del boton que se apreto en la pantalla
    - Abre el archivo corresponiente al csv seleccionado
    - Consulta cual es el criterio por el que hay que ordenar
    - Se genera el archivo .json
    - Sale un Pop-Up avisando que ya se genero el archivo correspondiente """
    current_path = os.getcwd()
    games_file_path = os.path.join(current_path,'TareaPythonPlus','ArchivosCSV','vgsales.csv') 
    boton,json_name = event.replace('-','').split(',')
    with open(games_file_path,'r',encoding='UTF-8') as archivo:
        datos = csv.reader(archivo,delimiter=',')
        encabezado = datos.__next__()
        if boton == '1':
            json_data = generar_opcion_1(datos)
        elif boton == '2':
            json_data = generar_opcion_2(datos)
        elif boton == '3':
            json_data = generar_opcion_3(datos)
        with open(os.path.join(current_path,'TareaPythonPlus','ArchivosJSON',json_name),'w',encoding='UTF-8') as archivo_json:
            json.dump(json_data,archivo_json,indent=4,ensure_ascii=False)

def start():
    window = sg.Window("VIDEO JUEGOS",layout=display(),size=(400,350),element_justification='c',
                    disable_close=True,disable_minimize=True)
    while True:
        event,values = window.read()
        if event in ("-SALIR-"):
            break
        else:
            manejador(event)
            sg.popup("Se creo el archivo deseado. Lo puede obervar en la carpeta 'ArchivosJSON'",title='Listo!')
    window.close()