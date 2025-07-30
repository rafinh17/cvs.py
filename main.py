import csv

with open("export_20250729.csv", newline="",encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        if "Damian Ramirez" in linha["Author(s)"]:
            print(linha)
         