import re  # Importa o módulo de expressões regulares para analisar strings

# Função para analisar declarações de variáveis em um bloco de código
def parse_variable_declaration(code):
    # Define o padrão de expressão regular para capturar tipos e variáveis
    pattern = r'(\w+)\s+((?:\w+\s*(?:=\s*[\w.]+)?,?\s*)+);'
    # Utiliza finditer para encontrar todas as ocorrências do padrão no código
    declarations = re.finditer(pattern, code)

    results = []  # Lista para armazenar os resultados das análises
    for declaration in declarations:
        data_type = declaration.group(1)  # Captura o tipo da variável (int, float, etc.)
        variables = declaration.group(2).split(',')  # Divide as variáveis listadas em uma declaração

        result = {'Tipo': data_type, 'Variaveis': []}  # Dicionário para armazenar o tipo e as variáveis

        for variable in variables:
            # Analisa cada variável para identificar nome e valor inicial (se houver)
            var_match = re.match(r'(\w+)\s*(?:=\s*([\w.]+))?', variable.strip())
            if var_match:
                var_name = var_match.group(1)  # Nome da variável
                var_value = var_match.group(2) if var_match.group(2) else None  # Valor inicial, se definido
                result['Variaveis'].append({
                    'Identificador': var_name,
                    'ValorInicial': var_value
                })

        results.append(result)  # Adiciona o dicionário ao resultado final
    return results

# Função para imprimir árvores de derivação com base na análise de declaração
def print_derivation_tree(declaration):
    print("DeclaraçãoInicialização")
    print("    |")
    print(f"    +---> <tipo> --------------> {declaration['Tipo']}")
    print("    |")
    print("    +---> <listaVariaveis>")

    for var in declaration['Variaveis']:
        print("        |")
        print("        +---> <variavel>")
        print("            |")
        print(f"            +---> <identificador> ---> {var['Identificador']}")
        if var['ValorInicial'] is not None:
            print("            |")
            print(f"            +---> <valor> ------------> {var['ValorInicial']}")

    print("    |")
    print("    +---> ;\n")

# Exemplo de uso da função
code_input = """
int x = 0;
float a=0.0, b, c=3.14;
int i, j=5, k=3, w=2;
"""

# Analisa o código de entrada e armazena o resultado
parsed_variables = parse_variable_declaration(code_input)
for decl in parsed_variables:
    print_derivation_tree(decl)  # Imprime a árvore de derivação para cada declaração analisada
    print("-" * 40)
