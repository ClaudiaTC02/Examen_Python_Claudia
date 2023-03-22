import csv
def read_data(fichero):
    with open(fichero, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        for line in reader:
            print(line)