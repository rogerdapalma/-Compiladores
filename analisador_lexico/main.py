import os
from afd import AFD

# Diretório base onde os arquivos estão localizados
# Obtém o caminho absoluto do diretório onde o script está localizado
base_dir = os.path.dirname(os.path.abspath(__file__))

# Caminhos completos dos arquivos
# Define o caminho completo para o arquivo de configuração (maquina.txt)
config_path = os.path.join(base_dir, 'maquina.txt')
# Define o caminho onde a tabela de símbolos será salva (mesmo diretório base)
save_path = base_dir
# Define o caminho completo para o arquivo de entrada (input.c)
input_path = os.path.join(base_dir, 'input.c')

# Inicialização do AFD
# Cria uma instância do AFD passando os caminhos do arquivo de configuração e do diretório de salvamento
afd = AFD(config_path, save_path)

# Processamento do arquivo de entrada
# Abre o arquivo de entrada (input.c) para leitura
with open(input_path, 'r') as file:
    index = 1  # Inicializa o índice da linha
    # Itera sobre cada linha do arquivo de entrada
    for linha in file.readlines():
        linha = linha.strip()  # Remove espaços em branco no início e no fim da linha
        afd.exec(linha, index)  # Executa o AFD com a linha atual e o índice da linha
        index += 1  # Incrementa o índice da linha
        print()  # Imprime uma linha em branco para separação visual
