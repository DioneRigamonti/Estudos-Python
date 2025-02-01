import os
import datetime

def arquivo_mais_recente():
    """
    Retorna o nome do arquivo CSV mais recentemente modificado no diretório atual.

    A função faz o seguinte:
    1. Filtra apenas os arquivos no diretório atual (ignorando pastas).
    2. Ordena esses arquivos pelo tempo de modificação, do mais antigo para o mais recente.
    3. Percorre a lista de arquivos na ordem inversa (do mais recente para o mais antigo).
    4. Retorna o primeiro arquivo com a extensão `.csv` encontrado.
    
    Se não houver arquivos `.csv` no diretório, a função retorna `None`.

    Retorna:
        str: O nome do arquivo CSV mais recente, ou `None` se não houver arquivos `.csv`.
    """
    lista_arq = filter(lambda x: os.path.isfile(os.path.join('./',x)),os.listdir('./'))

    lista_arq = sorted(lista_arq, key= lambda x: os.path.getmtime(os.path.join('./',x)))
    
    for i in reversed(lista_arq):
        if i.endswith('.csv'):            
            return i

    return None

arquivo_recente = arquivo_mais_recente()

##### EXTRA: convertendo a data de modificação para saber qual dia o arquivo foi modificado
arquivo = os.path.getmtime('testando.csv')
data_modificacao = datetime.datetime.fromtimestamp(arquivo)
print(data_modificacao)