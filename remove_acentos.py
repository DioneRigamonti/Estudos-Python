from unidecode import unidecode

def contar_vogais_consoantes(texto):
    vogais = "aeiou"
    qtd_vogais = 0
    qtd_consoantes = 0

    texto_sem_acento = unidecode(texto.lower())  # Remove acentos e coloca tudo em minúsculas

    for char in texto_sem_acento:
        if char.isalpha():  # Verifica se é uma letra
            if char in vogais:
                qtd_vogais += 1
            else:
                qtd_consoantes += 1

    return {"vogais": qtd_vogais, "consoantes": qtd_consoantes}

# Teste
print(contar_vogais_consoantes("Olá, Mundo! É incrível 123"))
# Saída esperada: {'vogais': 6, 'consoantes': 7}