import csv
def read_data(fichero):
    diccionario = dict()
    with open(fichero, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        indice = 1
        for line in reader:
            for valor in line:
                if len(valor) == 0:
                    print("Vacio")
            #diccionario.update({"dato"+str(indice) : line})
            indice+=1
    return diccionario