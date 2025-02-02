import os

def leitura(arquivo):
    # Obtém o caminho absoluto do arquivo
    caminho_arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), arquivo)
    
    # Exibe o caminho completo do arquivo
    print(f'Lendo o arquivo: {caminho_arquivo}')

    try:
        # Abre o arquivo com encoding UTF-8
        with open(caminho_arquivo, 'r', encoding="utf-8") as arq:
            conteudo = arq.read()
        
        # Exibe o conteúdo do arquivo
        print("\n=== Conteúdo do arquivo ===\n")
        print(conteudo)

    except FileNotFoundError:
        print("\n[ERRO] Arquivo não encontrado!")
    except Exception as e:
        print(f"\n[ERRO] Ocorreu um erro ao ler o arquivo: {e}")

# Testando a função
leitura("logs.txt")
