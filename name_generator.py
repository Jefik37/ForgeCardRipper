import csv

names=open('names.csv', 'w', encoding='utf8', newline='')

with open('cardnames-pt-BR.txt', newline='', encoding='utf8') as f:
    reader = csv.reader(f, delimiter='|')
    writer = csv.writer(names, delimiter='|')
    for i in reader:
        writer.writerow((i[0], i[1]))

names.close()