import csv

lista = [['a','b','c']]

with open('testando.csv', mode='w',newline='') as arq:
    csv_cursor = csv.writer(arq,delimiter=';')
    csv_cursor.writerow(['COLUNA_01','COLUNA_02','COLUNA_03'])
    csv_cursor.writerows(lista) #writerows precisa de uma matriz (lista de lista)

print('fim')