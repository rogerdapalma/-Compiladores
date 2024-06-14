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

# Análise Sintática e Semântica
def syntactic_analysis(tokens, symbol_table):
    stack = []
    for token_id, token, token_type, _, _ in tokens:
        if token_type in ["apar", "ach", "acol"]:
            stack.append((token_id, token, token_type))
        elif token_type in ["fpar", "fch", "fcol"]:
            if not stack:
                return False
            top_token_id, top_token, top_token_type = stack.pop()
            if symbol_table[str(top_token_id)]['ref'] != token_id:
                return False
    return len(stack) == 0

is_syntactically_correct = syntactic_analysis(tokens, symbol_table)

# Função para salvar a saída em um arquivo TXT
def save_output_to_file(tokens, is_syntactically_correct, filename='output.txt'):
    with open(filename, 'w') as f:
        f.write('Tokens Identificados:\n')
        for token_id, token, token_type, line, column in tokens:
            f.write(f'ID: {token_id}, Token: {token}, Tipo: {token_type}, Linha: {line}, Coluna: {column}\n')
            
# Salvar a saída no arquivo TXT
save_output_to_file(tokens, is_syntactically_correct)
print("Análise concluída e saída salva em 'output.txt'.")

