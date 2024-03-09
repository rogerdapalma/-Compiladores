estados = []
simbolos = []
estadosFinais = []
regrasTransicao = []
estadoAtual = ''

def inicializacao():
    global estados, simbolos, estadosFinais, regrasTransicao, estadoAtual
    arquivo = open('/content/drive/MyDrive/COMPILADOR/automato.txt')
    linha_estados = arquivo.readline().strip()
    estados = linha_estados.split(',')
    linha_simbolos = arquivo.readline().strip()
    for c in linha_simbolos:
        simbolos.append(c)
    estadosFinais = arquivo.readline().strip().split(',')
    linha = arquivo.readline().strip()
    while linha:
        regrasTransicao.append(linha)
        linha = arquivo.readline().strip()
    estadoAtual = estados[0]
    arquivo.close()

def exec_afd(linha):
    global estados, simbolos, estadosFinais, regrasTransicao, estadoAtual
    for c in linha:
      for regra in regrasTransicao:
        r = regra.split(':')
        if r[0]==estadoAtual and c in r[1] :
          estadoAtual = r[2]
       # print(c,r)
    print(linha,'terminou no estado:', estadoAtual)
    flag = 0
    for ef in estadosFinais:
      if ef.split(':')[0]==estadoAtual:
        print(linha,'reconhecido:',ef.split(':')[1])
        flag=1
    if flag==0:
        print('linha',linha,'nao reconhecida')
    estadoAtual = estados[0]
def input():
    arquivo = open('/content/drive/MyDrive/COMPILADOR/input.c')
    linhas = arquivo.readlines()
    for linha in linhas:
        exec_afd(linha.strip())

inicializacao()
input()