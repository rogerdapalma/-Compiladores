import sys

class Token:
    def __init__(self, tipo, valor, linha, coluna):
        self.tipo = tipo    # Tipo do token (ex: IDENTIFICADOR, NUMERO, etc.)
        self.valor = valor  # Valor textual do token
        self.linha = linha  # Número da linha onde o token foi encontrado
        self.coluna = coluna  # Número da coluna onde o token começa

# Função para analisar o código-fonte e extrair tokens
def analisar_codigo(arquivo_fonte):
    tokens = []  # Lista para armazenar os tokens encontrados
    try:
        with open(arquivo_fonte, 'r') as arquivo:
            linhas = arquivo.readlines()  # Ler todas as linhas do arquivo
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_fonte}' não foi encontrado.")
        sys.exit(1)  # Encerra o programa com um código de erro

    # Itera sobre cada linha do arquivo
    for num_linha, linha in enumerate(linhas):
        coluna = 0  # Inicializa a coluna para o início da linha
        while coluna < len(linha):  # Enquanto não chegar ao fim da linha
            char = linha[coluna]  # Caractere atual
            if char.isalpha():  # Se for uma letra, inicia um identificador
                inicio = coluna
                # Avança enquanto for letra ou número (identificador)
                while coluna < len(linha) and linha[coluna].isalnum():
                    coluna += 1
                # Adiciona o token identificador à lista de tokens
                tokens.append(Token("IDENTIFICADOR", linha[inicio:coluna], num_linha, inicio))
            else:
                coluna += 1  # Avança para o próximo caractere
    return tokens  # Retorna a lista de tokens

# Função para salvar os tokens em um arquivo CSV
def salvar_tokens(tokens, arquivo_saida):
    with open(arquivo_saida, 'w') as arquivo:
        for token in tokens:
            # Escreve cada token como uma linha no formato CSV
            arquivo.write(f"{token.tipo},{token.valor},{token.linha + 1},{token.coluna}\n")

# Exemplo de uso
arquivo_codigo_fonte = "codigo_fonte.c"  #.txt,.js,.lua,etc...
tokens = analisar_codigo(arquivo_codigo_fonte)  # Analisa o código-fonte
salvar_tokens(tokens, "tokens.csv")  # Salva os tokens em um arquivo CSV
