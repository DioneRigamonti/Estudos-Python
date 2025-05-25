import csv
import argparse
import sys

class ValidadorArquivo:
    def verificar_arquivo(self, caminho_arquivo, separador) -> str:
        linhas_com_erro = []

        with open(caminho_arquivo, newline='', encoding='utf-8-sig') as arquivo:
            leitor = csv.reader(arquivo, delimiter=separador)
            linhas = list(leitor)

        if not linhas:
            print("Arquivo vazio.")
            return

        colunas_esperadas = len(linhas[0])

        for i, linha in enumerate(linhas, start=1):
            if len(linha) != colunas_esperadas:
                linhas_com_erro.append((i, linha))

        if linhas_com_erro:
            print(f"{'#' * 10} {len(linhas_com_erro)} linha(s) com problema encontrada(s): {'#' * 10}")
            for numero_linha, conteudo in linhas_com_erro:
                print(f"Linha {numero_linha}: {conteudo}")
        else:
            print(f"{'#' * 10} Nenhuma linha com problema encontrada. {'#' * 10}")

if __name__ == "__main__":
    validador = ValidadorArquivo()

    ### Se não houver argumentos (exceto o próprio script), roda modo hardcoded para debug/VSCode
    if len(sys.argv) == 1:
        ### Coloque aqui o caminho e separador desejados para rodar no VSCode
        caminho_debug = r"C:\Users\rigam\Downloads\clientes+cartao.csv"
        separador_debug = ";"
        print("Rodando modo debug com parâmetros hardcoded:")
        validador.verificar_arquivo(caminho_arquivo=caminho_debug, separador=separador_debug)
    else:
        ### Se tiver argumentos, processa com argparse normalmente
        parser = argparse.ArgumentParser(description="Validador de arquivos delimitados (CSV/TXT).")
        #parser.add_argument("--metodo", choices=["verificar"], required=True, help="Método a ser executado.")
        parser.add_argument("--arquivo", required=True, help="Caminho completo do arquivo a ser verificado.")
        parser.add_argument("--separador", default=";", help="Separador utilizado no arquivo. Padrão é ';'.")
        args = parser.parse_args()

        #if args.metodo == "verificar":
        validador.verificar_arquivo(caminho_arquivo=args.arquivo, separador=args.separador)

#exemplo linha de comando python script.py --arquivo "C:/caminho/para/arquivo.csv" --separador ";"
