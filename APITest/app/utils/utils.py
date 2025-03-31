import csv

def csvToList():
    listOperator = []
    csvPath = "C:\\Users\\guilh\\PycharmProjects\\SearchOperator\\Relatorio_cadop.csv"

    with open(csvPath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')

        for row in reader:
            listOperator.append(row)

    return listOperator