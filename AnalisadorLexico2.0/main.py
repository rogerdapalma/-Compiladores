import sys

# Definition of the Token class which represents each recognized token in the source code
class Token:
    def __init__(self, id, tipo, linha, coluna):
        self.id = id  # The actual token value (e.g., 'void', 'main', etc.)
        self.tipo = tipo  # The type of token (e.g., 'nomeVAR', 'AP', etc.)
        self.linha = linha  # The line number where the token was found
        self.coluna = coluna  # The column number where the token starts

# Function to load recognized tokens from a file into a dictionary
def carregar_tokens_reconhecidos(arquivo_tokens):
    tokens_reconhecidos = {}
    try:
        with open(arquivo_tokens, 'r') as arquivo:
            for linha in arquivo:
                token, tipo = linha.strip().split(',')
                tokens_reconhecidos[token] = tipo
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_tokens}' não foi encontrado.")
        sys.exit(1)
    return tokens_reconhecidos

# Function to analyze a source code file and extract tokens based on recognized tokens
def analisar_codigo(arquivo_fonte, tokens_reconhecidos):
    tokens = []
    try:
        with open(arquivo_fonte, 'r') as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_fonte}' não foi encontrado.")
        sys.exit(1)

    for num_linha, linha in enumerate(linhas):
        coluna = 0
        while coluna < len(linha):
            match = False
            for token in tokens_reconhecidos:
                if linha[coluna:].startswith(token):
                    tokens.append(
                        Token(token, tokens_reconhecidos[token], num_linha + 1, coluna))
                    coluna += len(token)
                    match = True
                    break
            if not match:
                coluna += 1
    return tokens

# Function to save the list of tokens into a CSV file
def salvar_tokens(tokens, arquivo_saida):
    with open(arquivo_saida, 'w') as arquivo:
        for token in tokens:
            arquivo.write(f"{token.id},{token.tipo},{token.linha},{token.coluna}\n")

# Example usage of the code
tokens_reconhecidos = carregar_tokens_reconhecidos("tokens_reconhecidos.txt")
arquivo_codigo_fonte = "codigo_fonte.c"
tokens = analisar_codigo(arquivo_codigo_fonte, tokens_reconhecidos)
salvar_tokens(tokens, "tokens.csv")
