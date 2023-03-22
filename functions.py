import csv
def read_data(fichero):
    diccionario = dict()
    titulos = []
    with open(fichero, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        indice = 1
        fila = ""
        y = file.readline()
        x = y.replace('\n', '')
        titulos = x.split(",")
        for line in reader:
            for valor in line:
                if len(valor) == 0:
                    fila = line
            if(fila != line):
                diccionario_nuevo = dict()
                j = 0
                for i in titulos:
                    diccionario_nuevo.update({i: str(line[j])})
                    j+=1
                diccionario.update({"dato"+str(indice) : diccionario_nuevo})
                indice+=1
    
    if (len(diccionario.keys()) < 10):
        raise ValueError("Hay menos de 10 líneas con todos los datos completos")
    return diccionario

def split(diccionario):
    diccionario_white = dict()
    diccionario_red = dict()