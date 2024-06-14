import json
from afd import AFD

# Carregar a tabela de transições
with open('maquina.txt', 'r') as f:
    transitions = f.read().splitlines()

# Carregar o código de entrada
with open('input.c', 'r') as f:
    input_code = f.read()

# Carregar a tabela de símbolos
with open('tabela_simbolos.json', 'r') as f:
    symbol_table = json.load(f)

# Estados finais e seus tokens
final_states = {
    "q1": "inteiro",
    "q3": "fracionario",
    "q5": "nomeVar",
    "q6": "satrib",
    "q7": "pv",
    "q9": "virgula",
    "q10": "sinalCompara",
    "q11": "apar",
    "q12": "fpar",
    "q13": "ach",
    "q14": "fch",
    "q15": "acol",
    "q16": "fcol",
    "q17": "conetivo"
}

# Instanciar o AFD
afd = AFD(transitions, final_states)

# Análise Léxica
tokens = afd.lexical_analysis(input_code)

# Função para salvar a saída em um arquivo TXT
def save_output_to_file(tokens, is_syntactically_correct, is_semantically_correct, filename='output.txt'):
    with open(filename, 'w') as f:
        f.write('Tokens Identificados:\n')
        for token, token_type, line, column in tokens:
            f.write(f'Token: {token}, Tipo: {token_type}, Linha: {line}, Coluna: {column}\n')
# Análise Sintática
def syntactic_analysis(tokens):
    stack = []
    for token, token_type, _, _ in tokens:
        if token_type in ["apar", "ach", "acol"]:
            stack.append((token, token_type))
        elif token_type in ["fpar", "fch", "fcol"]:
            if not stack:
                return False
            top_token, top_token_type = stack.pop()
            if (token_type == "fpar" and top_token_type != "apar") or \
               (token_type == "fch" and top_token_type != "ach") or \
               (token_type == "fcol" and top_token_type != "acol"):
                return False
    return len(stack) == 0

is_syntactically_correct = syntactic_analysis(tokens)

# Análise Semântica
def semantic_analysis(tokens, symbol_table):
    for token, token_type, _, _ in tokens:
        if token_type == "nomeVar" and not any(entry['token'] == token for entry in symbol_table.values()):
            return False
    return True

is_semantically_correct = semantic_analysis(tokens, symbol_table)

# Salvar a saída no arquivo TXT
save_output_to_file(tokens, is_syntactically_correct, is_semantically_correct)
print("Análise concluída e saída salva em 'output.txt'.")
