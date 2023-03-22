import csv
"""
Este módulo incluye un conjunto de funciones que trabaja con diccionarios.

Autora: Claudia Torres Cruz

"""
def read_data(fichero):
    """Lee un fichero csv y sus elementos los introduce en un diccionario, con clave datoX donde X es el número
        Args:
        fichero: Fichero csv
        Return:
        diccionario: Diccionario con los elementos
    """
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
    """Separa un diccionario según su tipo, white y red
        Args:
        diccionario: Diccionario que queremos recibir
        Return:
        diccionario_white: Diccionario con todos los datos cuyo type es white sin el atributo type
        diccionario_red: Diccionario con todos los datos cuyo type es red sin el atributo type
    """
    diccionario_white = dict()
    diccionario_red = dict()
    for i in diccionario:
        if(diccionario[i]['type'] == 'white'):
            diccionario_white.update({i : diccionario[i]})
            diccionario_white.get(i).pop('type')
        elif(diccionario[i]['type'] == 'red'):
            diccionario_red.update({i : diccionario[i]})
            diccionario_red.get(i).pop('type')
    return diccionario_white, diccionario_red

def reduce(diccionario, atributo):
    """Almacena en una lista dado un diccionario los valores cuyo atributo es el dado a la funcion
        Args:
        diccionario: Diccionario del que queremos saber valores concretos
        atributo: atributo del que queremos sacar los valores
        Return:
        lista: lista con el valor del diccionario según el atributo dado
    """
    lista = []
    for i in diccionario:
        if atributo in diccionario[i]:
            lista.append(diccionario[i][atributo])
        else:
            raise ValueError("El atributo no existe")
    return lista

def silhouette(lista1, lista2):
    a_i = 0
    b_i = 0
    for i in lista1:
        coeficiente_silhouette = 0