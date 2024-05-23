import pandas as pd # type: ignore

def carregar_automato(arquivo):
    estados = {}
    # Abre o arquivo de configuração do autômato para leitura
    with open(arquivo, 'r') as f:
        linhas = f.read().splitlines()
        for linha in linhas:
            partes = linha.split(':')
            if len(partes) < 2:
                # Exibe uma mensagem de erro se a linha estiver no formato incorreto e pula para a próxima
                print(f"Linha em formato incorreto: {linha}")
                continue
            estado, transicoes = partes[0].strip(), partes[1].split(',')
            transicao_dict = {}
            for transicao in transicoes:
                entrada_destino = transicao.split()
                if len(entrada_destino) < 2:
                    # Exibe uma mensagem de erro se a transição estiver no formato incorreto e pula para a próxima
                    print(f"Transição em formato incorreto: {transicao} em estado {estado}")
                    continue
                entrada, destino = entrada_destino
                transicao_dict[entrada] = destino
            estados[estado] = transicao_dict
    # Exibe uma mensagem indicando que o arquivo de configuração foi lido com sucesso
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
                # Adiciona False à lista de resultados se a transição não for encontrada no autômato
                resultados.append(False)
                break
        else:
            # Verifica se o estado atual é um estado de aceitação
            if 'aceitacao' in automato.get(estado_atual, {}):
                resultados.append(True)
            else:
                resultados.append(False)
    # Exibe uma mensagem indicando que a conversão foi realizada corretamente
    print("Converteu corretamente.")
    return resultados

def main():
    # Lê a tabela de símbolos a partir de um arquivo Excel
    tabela_simbolos = pd.read_excel(r'C:\Users\roger\Downloads\Analise Sintatica\tabela_simbolos.xlsx')
    print(tabela_simbolos)
    print("Leu tabela de símbolos.")

    # Carrega o autômato a partir de um arquivo de texto
    automato = carregar_automato(r'C:\Users\roger\Downloads\Analise Sintatica\automato.txt')

    # Realiza a análise sintática dos tokens
    resultados = analisar_sintaxe(tabela_simbolos, automato)

    # Adiciona os resultados da análise sintática à tabela de símbolos
    tabela_simbolos['Reconhecido'] = resultados
    print(tabela_simbolos)
    print("Gerou a saída corretamente.")

if __name__ == "__main__":
    main()
