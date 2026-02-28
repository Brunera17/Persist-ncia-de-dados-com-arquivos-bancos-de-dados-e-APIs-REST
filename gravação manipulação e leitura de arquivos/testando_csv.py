import csv

with open('dados.csv', 'w') as f:
    escritor = csv.writer(f)
    escritor.writerow(['nome', 'idade'])
    escritor.writerow(['Bruno', '24'])