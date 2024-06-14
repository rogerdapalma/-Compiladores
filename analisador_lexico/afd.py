class AFD:
    def __init__(self, transitions, final_states):
        self.transitions = transitions
        self.final_states = final_states
        self.keywords = {
            "int": "tipoInteiro",
            "float": "tipoFracionario",
            "if": "condicao"
        }

    def lexical_analysis(self, code):
        tokens = []
        state = 'q0'
        buffer = ''
        line = 1
        column = 0

        code += ' '  # Adiciona espaço ao final para garantir a captura do último token

        for i, char in enumerate(code):
            if char == '\n':
                line += 1
                column = 0
                continue
            elif char in ' \t':
                column += 1
                continue

            buffer += char
            column += 1

            # Verificar se precisa fechar o token atual
            if i + 1 < len(code) and not code[i + 1].isalnum() and code[i + 1] != '.':
                if buffer.isdigit():
                    tokens.append((buffer, 'inteiro', line, column - len(buffer)))
                elif self.is_float(buffer):
                    tokens.append((buffer, 'fracionario', line, column - len(buffer)))
                elif buffer in self.keywords:
                    tokens.append((buffer, self.keywords[buffer], line, column - len(buffer)))
                else:
                    tokens.append((buffer, 'nomeVar', line, column - len(buffer)))
                buffer = ''

        return tokens

    def is_float(self, s):
        parts = s.split('.')
        return len(parts) == 2 and all(part.isdigit() for part in parts)

# Exemplo de uso
transitions = ['transições a serem definidas...']
final_states = {'estados finais a serem definidos...'}
afd = AFD(transitions, final_states)
code = "int x = 10; float pi = 3.14; if (x < 3.14) { pi = pi * 2; }"
tokens = afd.lexical_analysis(code)
for token in tokens:
    print(f'Token: {token[0]}, Tipo: {token[1]}, Linha: {token[2]}, Coluna: {token[3]}')
