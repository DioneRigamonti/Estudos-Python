import csv

dicionario = {}
caminho = r"C:\Users\rigam\OneDrive\Área de Trabalho\z\carteira.csv"

with open(caminho, newline='', encoding='utf-8-sig') as arq:
    leitor = csv.DictReader(arq,delimiter=';')
    
    for linha in leitor:
        # remove espaços extras do header
        linha = {k.strip(): v for k, v in linha.items()}

        id_cliente = str(linha['id'])
        dicionario[id_cliente] = {
            "cd_mes": linha["cd_mes"],
            "cd_producao": linha["cd_producao"],
            "ilha": linha["ilha"],
            "EPS": linha["EPS"],
            "MASTER": linha["MASTER"],
            "faturamento": linha["faturamento"]
        }

for i,k in dicionario.items():
    print(i,k)