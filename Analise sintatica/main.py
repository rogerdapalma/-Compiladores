import pandas as pd

estados = []
simbolos = []
estadosFinais = []
regrasTransicao = []
estadoAtual = ''

def inicializacao(arquivo_automato):
    global estados, simbolos, estadosFinais, regrasTransicao, estadoAtual
    with open(arquivo_automato) as arquivo:
        linha_estados = arquivo.readline().strip()
        estados = linha_estados.split(':')
        linha_simbolos = arquivo.readline().strip()
        simbolos = linha_simbolos.split(':')
        estadosFinais = arquivo.readline().strip().split(':')
        regrasTransicao = [linha.strip() for linha in arquivo if linha.strip()]
    estadoAtual = estados[0]

def exec_afd(tokens):
    global estadoAtual
    for token in tokens:
        flag_encontrou_regra = False
        for regra in regrasTransicao:
            estado_origem, simbolo, estado_destino = regra.split(':')
            if estado_origem == estadoAtual and token == simbolo:
                estadoAtual = estado_destino
                flag_encontrou_regra = True
                break
        if not flag_encontrou_regra:
            estadoAtual = estados[0]
            print(f'Token {token} não reconhecido')
            return False
    if estadoAtual in estadosFinais:
        print(f'Reconhecido: {tokens}')
        return True
    else:
        print(f'Não Reconhecido: {tokens}')
        return False

def processar_arquivo(arquivo_tokens, arquivo_automato):
    df = pd.read_excel(arquivo_tokens)
    df.sort_values(by=['Linha', 'ID'], inplace=True)
    tokens_por_linha = df.groupby('Linha')['Token'].apply(list)
    resultados = []
    for linha_num, tokens in tokens_por_linha.items():
        print(f'\nProcessando linha {linha_num} com tokens: {tokens}')
        inicializacao(arquivo_automato)
        if exec_afd(tokens):
            resultado = "Reconhecida"
        else:
            resultado = "Não reconhecida"
        resultados.append((linha_num, resultado))
    return resultados

# Exemplo de uso
arquivo_automato = 'automato.txt'
arquivo_tokens = 'tabela_simbolos.xlsx'

# Processar arquivo de tokens
print("Processando arquivo de tokens:")
resultados = processar_arquivo(arquivo_tokens, arquivo_automato)
for linha_num, resultado in resultados:
    print(f'Linha {linha_num}: {resultado}')
