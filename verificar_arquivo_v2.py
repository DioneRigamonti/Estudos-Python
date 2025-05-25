import csv
import argparse
import sys
from pathlib import Path

class ValidadorArquivo:
    def __init__(self, caminho: str, separador: str = ";"):
        self.caminho = Path(caminho)
        self.separador = separador
        self.linhas_com_erro = []

    def verificar(self):
        try:
            with self.caminho.open(newline='', encoding='utf-8-sig') as f:
                leitor = csv.reader(f, delimiter=self.separador)
                linhas = list(leitor)
        except FileNotFoundError:
            print(f"Arquivo não encontrado: {self.caminho}")
            return

        if not linhas:
            print("Arquivo vazio.")
            return

        colunas_esperadas = len(linhas[0])

        for i, linha in enumerate(linhas, start=1):
            if len(linha) != colunas_esperadas:
                self.linhas_com_erro.append((i, linha))

        self._exibir_resultado(colunas_esperadas=colunas_esperadas)

    def _exibir_resultado(self, colunas_esperadas):
        if self.linhas_com_erro:
            print(f"{'#' * 10} {len(self.linhas_com_erro)} linha(s) com problema encontrada(s) (esperado: {colunas_esperadas} colunas): {'#' * 10}")
            for numero_linha, conteudo in self.linhas_com_erro:
                print(f"Linha {numero_linha}: {conteudo}")
        else:
            print(f"{'#' * 10} Nenhuma linha com problema encontrada. {'#' * 10}")

def main():
    if len(sys.argv) == 1:
        # Modo hardcoded (VSCode)
        caminho_debug = r"C:\Users\rigam\Downloads\clientes+cartao.csv"
        separador_debug = ";"
        print("Rodando em modo debug com parâmetros fixos...")
        ValidadorArquivo(caminho=caminho_debug, separador=separador_debug).verificar()
    else:
        # Modo terminal
        parser = argparse.ArgumentParser(description="Validador de arquivos CSV/TXT.")
        parser.add_argument("--arquivo", required=True, help="Caminho completo do arquivo.")
        parser.add_argument("--separador", default=";", help="Separador do arquivo. Padrão ';'.")
        args = parser.parse_args()
        ValidadorArquivo(caminho=args.arquivo, separador=args.separador).verificar()

if __name__ == "__main__":
    main()

#exemplo linha de comando python script.py --arquivo "C:/caminho/para/arquivo.csv" --separador ";"