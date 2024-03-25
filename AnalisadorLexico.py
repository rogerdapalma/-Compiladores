estados = []
simbolos = []
estadosFinais = {}
transicoes = {}
pilhaEstados = []
token = ''

def inicializacao():
    global estados, simbolos, estadosFinais, transicoes, pilhaEstados
    estados = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8']
    simbolos = ['+', '-', '.', '0123456789', 'abcdefghijklmnopqrstuvwxyz', '_', '=', ';']
    estadosFinais = {'q1': 'inteiro', 'q3': 'fracionario', 'q5': 'nomeVar', 'q6': 'SinalAtrib', 'q7': 'PV', 'q8': 'palavraChave'}
    transicoes = {
        'q0': {'+': 'q4', '-': 'q4', '0123456789': 'q1', 'abcdefghijklmnopqrstuvwxyz': 'q5', '=': 'q6', ';': 'q7'},
        'q1': {'0123456789': 'q1', '.': 'q2'},
        'q2': {'0123456789': 'q3'},
        'q3': {'0123456789': 'q3'},
        'q4': {'0123456789': 'q1'},
        'q5': {'abcdefghijklmnopqrstuvwxyz': 'q5', '_': 'q5', '0123456789': 'q5'},
        'q8': {'abcdefghijklmnopqrstuvwxyz': 'q5'}
    }
    pilhaEstados.append('q0')

def exec_afd(linha):
    global pilhaEstados, token
    for c in linha:
        token += c
        estadoAtual = pilhaEstados[-1]
        transicaoEncontrada = False
        for simbolo, proximoEstado in transicoes[estadoAtual].items():
            if c in simbolo:
                pilhaEstados.append(proximoEstado)
                transicaoEncontrada = True
                break
        if not transicaoEncontrada:
            if estadoAtual in estadosFinais:
                print(f'{token[:-1]} reconhecido como {estadosFinais[estadoAtual]}')
            else:
                print(f'Token não reconhecido: {token[:-1]}')
            token = c
            pilhaEstados = ['q0']
    estadoFinal = pilhaEstados.pop()
    if estadoFinal in estadosFinais:
        print(f'{token} reconhecido como {estadosFinais[estadoFinal]}')
    else:
        print(f'Token não reconhecido: {token}')
    token = ''
    pilhaEstados = ['q0']

def input_afd():
    linha = 'int x_123=254;'
    exec_afd(linha)

inicializacao()
input_afd()
