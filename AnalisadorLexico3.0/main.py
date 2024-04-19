# Variáveis para armazenar os estados, símbolos, estados finais, regras de transição,
# estado atual, tokens reconhecidos e pilha para rastrear tokens de abertura.
estados = []
simbolos = []
estadosFinais = []
regrasTransicao = []
estadoAtual = ''
tokens_reconhecidos = []
pilha_tokens_abertura = []  # Pilha para rastrear tokens de abertura


def inicializacao():
  # Função para inicializar o autômato finito determinístico (AFD) a partir de um arquivo 'automato.txt'.
  global estados, simbolos, estadosFinais, regrasTransicao, estadoAtual
  with open('automato.txt') as arquivo:
    estados = arquivo.readline().strip().split(
        ',')  # Leitura dos estados do AFD.
    linha_simbolos = arquivo.readline().strip(
    )  # Leitura dos símbolos do alfabeto do AFD.
    simbolos.extend(linha_simbolos)
    estadosFinais = arquivo.readline().strip().split(':')[-1].split(
        ',')  # Leitura dos estados finais do AFD.
    regrasTransicao = [linha.strip() for linha in arquivo if linha.strip()
                       ]  # Leitura das regras de transição do AFD.
  estadoAtual = estados[0]  # Define o estado atual como o estado inicial.


def exec_afd(linha, numero_linha):
  # Função para executar o AFD em uma linha de código, reconhecendo os tokens.
  global estadoAtual, tokens_reconhecidos, pilha_tokens_abertura
  buffer = ''
  coluna_atual = 1
  for c in linha:
    flag_encontrou_regra = False
    for regra in regrasTransicao:
      estado_origem, chars_validos, estado_destino = regra.split(':')
      if estadoAtual == estado_origem and c in chars_validos:
        estadoAtual = estado_destino
        buffer += c
        flag_encontrou_regra = True
        break

    if c == ' ' or not flag_encontrou_regra:
      if buffer:
        tipo_token = mapeia_estado_para_tipo_token(estadoAtual)
        ref = None
        if tipo_token in ['fpar', 'fch', 'fcol']:
          if pilha_tokens_abertura:
            ref = pilha_tokens_abertura.pop()
        elif tipo_token in ['apar', 'ach', 'acol']:
          pilha_tokens_abertura.append(len(tokens_reconhecidos) + 1)
        tokens_reconhecidos.append(
            (len(tokens_reconhecidos) + 1, buffer, tipo_token, numero_linha,
             coluna_atual - len(buffer), ref))
      buffer = ''
      estadoAtual = estados[0]

    coluna_atual += 1

  if buffer:
    tipo_token = mapeia_estado_para_tipo_token(estadoAtual)
    ref = None
    if tipo_token in ['fpar', 'fch', 'fcol']:
      if pilha_tokens_abertura:
        ref = pilha_tokens_abertura.pop()
    tokens_reconhecidos.append(
        (len(tokens_reconhecidos) + 1, buffer, tipo_token, numero_linha,
         coluna_atual - len(buffer), ref))
  estadoAtual = estados[0]


def mapeia_estado_para_tipo_token(estado):
  # Função para mapear os estados do AFD para os tipos de token correspondentes.
  tipo_token = {
      'q1': 'inteiro',
      'q3': 'fracionario',
      'q5': 'nomeVar',
      'q6': 'satrib',
      'q7': 'sinalCompara',
      'q8': 'virgula',
      'q9': 'pv',
      'q10': 'apar',
      'q11': 'fpar',
      'q12': 'ach',
      'q13': 'fch',
      'q14': 'acol',
      'q15': 'fcol',
      'q16': 'conectivo',
      'q17': 'sinalCompara'
  }
  return tipo_token.get(estado, 'Outro')


def gera_tabela_simbolos():
  # Função para gerar a tabela de símbolos reconhecidos e salvar em 'tabela_simbolos.txt'.
  with open('tabela_simbolos.txt', 'w') as tabela:
    tabela.write('ID,Token,Tipo de Token,Linha,Coluna,Ref\n')
    for token_id, token, tipo_token, linha, coluna, ref in tokens_reconhecidos:
      ref_str = f'->{ref}' if ref else ''
      tabela.write(
          f'{token_id},{token},{tipo_token},{linha},{coluna}{ref_str}\n')


# Inicializa o AFD.
inicializacao()

# Abre o arquivo de entrada ('input.c') e executa o AFD em cada linha.
with open('input.c') as arquivo:
  for numero_linha, linha in enumerate(arquivo, start=1):
    exec_afd(linha.strip(), numero_linha)

# Gera a tabela de símbolos reconhecidos.
gera_tabela_simbolos()
