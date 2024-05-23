import pandas as pd # type: ignore

def carregar_automato(arquivo):
    estados = {}
    with open(arquivo, 'r') as f:
        linhas = f.read().splitlines()
        for linha in linhas:
            partes = linha.split(':')
            if len(partes) < 2:
                print(f"Linha em formato incorreto: {linha}")
                continue  # Pula esta linha e continua com a próxima
            estado, transicoes = partes[0].strip(), partes[1].split(',')
            transicao_dict = {}
            for transicao in transicoes:
                entrada_destino = transicao.split()
                if len(entrada_destino) < 2:
                    print(f"Transição em formato incorreto: {transicao} em estado {estado}")
                    continue  # Pula esta transição e continua com as próximas
                entrada, destino = entrada_destino
                transicao_dict[entrada] = destino
            estados[estado] = transicao_dict
    print("Leu arquivo de configuração AFD.")
    return estados

def analisar_sintaxe(tabela_simbolos, automato):
    resultados = []
    for index, row in tabela_simbolos.iterrows():
        estado_atual = 'q0'
        token = str(row['Token'])  # Garante que o token seja tratado como string
        tokens = token.split()  # Assume que os tokens em cada linha estão separados por espaço
        for token in tokens:
            if token in automato[estado_atual]:
                estado_atual = automato[estado_atual][token]
            else:
                resultados.append(False)
                break
        else:
            if 'aceitacao' in automato.get(estado_atual, {}):  # Verifica se está num estado de aceitação
                resultados.append(True)
            else:
                resultados.append(False)
    print("Converteu corretamente.")
    return resultados

def main():
    tabela_simbolos = pd.read_excel(r'C:\Users\roger\Downloads\d\tabela_simbolos.xlsx')  # Ajuste o caminho conforme necessário
    print(tabela_simbolos)

    print("Leu tabela de símbolos.")

    # Carrega o automato
    automato = carregar_automato(r'C:\Users\roger\Downloads\d\automato.txt')

    # Análise sintática dos tokens
    resultados = analisar_sintaxe(tabela_simbolos, automato)

    # Geração de saída
    tabela_simbolos['Reconhecido'] = resultados
    print(tabela_simbolos)
    print("Gerou a saída corretamente.")

if __name__ == "__main__":
    main()
