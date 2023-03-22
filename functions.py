import csv
def read_data(fichero):
    diccionario = dict()
    titulos = []
    with open(fichero, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        indice = 1
        fila = ""
        for line in reader:
            titulos = line[0]
            for valor in line:
                if len(valor) == 0:
                    fila = line
            if(fila != line and indice != 1):
                diccionario_nuevo = dict()
                for i in titulos:
                    diccionario_nuevo.update({i: str(line[i])})
                    print(diccionario_nuevo)
                diccionario.update({"dato"+str(indice) : diccionario_nuevo})
                indice+=1
    return diccionario