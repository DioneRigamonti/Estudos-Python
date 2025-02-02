import subprocess

# 1️⃣ Executar Comandos do Sistema
subprocess.run(["ls", "-l"])  # Executa 'ls -l' (Linux) ou 'dir' (Windows)

# 2️⃣ Executar um Script Externo
subprocess.run(["python", "outro_script.py"])  # Executa um script Python

# 3️⃣ Capturar Saída de um Comando
resultado = subprocess.run(["echo", "Olá, Mundo!"], capture_output=True, text=True)  # Captura a saída do comando
print(resultado.stdout)  # Exibe "Olá, Mundo!"

# 4️⃣ Verificar o Código de Retorno
resultado = subprocess.run(["ls", "-l"], capture_output=True)
if resultado.returncode == 0:  # Verifica se o comando foi bem-sucedido
    print("Comando executado com sucesso!")
else:
    print("Houve um erro ao executar o comando.")

# 5️⃣ Executar Comandos com Entrada (stdin)
processo = subprocess.Popen(["python", "processa_entrada.py"], stdin=subprocess.PIPE, text=True)
processo.communicate(input="Texto para ser processado\n")  # Passa entrada para o script

# 6️⃣ Executar Processos em Paralelo
p1 = subprocess.Popen(["python", "script1.py"])  # Executa o primeiro script
p2 = subprocess.Popen(["python", "script2.py"])  # Executa o segundo script
p1.wait()  # Espera o primeiro terminar
p2.wait()  # Espera o segundo terminar
print("Ambos os scripts terminaram!")

# 7️⃣ Redirecionar a Saída para um Arquivo
with open("output.txt", "w") as arquivo:  # Abre o arquivo para escrever
    subprocess.run(["ls", "-l"], stdout=arquivo)  # Redireciona a saída para 'output.txt'

# 8️⃣ Usar Shell para Executar Comandos Complexos
subprocess.run("echo 'olá' | tr 'a-z' 'A-Z'", shell=True)  # Executa comandos usando o shell

# 9️⃣ Gerenciar Processos em Segundo Plano
processo = subprocess.Popen(["python", "script_em_segundo_plano.py"])  # Executa em segundo plano
print("Processo em segundo plano está rodando...")

# 🔟 Trabalhando com Processos Filhos e Comunicação entre Processos
processo = subprocess.Popen(
    ["python", "processa_entrada.py"], 
    stdin=subprocess.PIPE, 
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE, 
    text=True
)
saida, erro = processo.communicate(input="Texto para o processo\n")  # Envia entrada e captura saída e erro
print("Saída:", saida)
print("Erro:", erro)
