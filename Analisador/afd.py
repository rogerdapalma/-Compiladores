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
        token_id = 1  # Iniciar a contagem de ID dos tokens

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

            if i + 1 < len(code) and not code[i + 1].isalnum() and code[i + 1] != '.':
                if buffer.isdigit():
                    tokens.append((token_id, buffer, 'inteiro', line, column - len(buffer)))
                elif self.is_float(buffer):
                    tokens.append((token_id, buffer, 'fracionario', line, column - len(buffer)))
                elif buffer in self.keywords:
                    tokens.append((token_id, buffer, self.keywords[buffer], line, column - len(buffer)))
                else:
                    tokens.append((token_id, buffer, 'nomeVar', line, column - len(buffer)))
                buffer = ''
                token_id += 1  # Incrementar o ID do token

        return tokens

    def is_float(self, s):
        parts = s.split('.')
        return len(parts) == 2 and all(part.isdigit() for part in parts)
