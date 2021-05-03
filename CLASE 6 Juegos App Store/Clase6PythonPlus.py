import csv
from collections import Counter

with open('appstore_games.csv','r',encoding='UTF-8') as archivo:
    lector = csv.reader(archivo,delimiter=',')
    encabezado = next(lector)
    gratis_en_espanol = list(filter(lambda x: x[7]=='0' and 'ES' in x[12],lector))
    for elem in gratis_en_espanol:
        print(elem[2])
    print(len(gratis_en_espanol))

    archivo.seek(0) # muevo el puntero del archivo para hacer el segundo inciso
    encabezado = next(lector) # Vuelvo a guardarme el encabezado
    dicc_ratings = {elem[4]:elem[6] for elem in lector}
    mas_votados = Counter(dicc_ratings).most_common(10)
    for elem in mas_votados:
        print(elem[0],' ',elem[1])

    print()
    print()

    mas_votados1 = sorted(dicc_ratings.items(), key=lambda x:x[1], reverse=True)
    mas_votados1 = mas_votados1[:10]
    for elem in mas_votados1:
        print(elem[0],' ',elem[1])