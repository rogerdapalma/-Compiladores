# Apresentação do Código de Análise Sintática com Autômato

Este código em Python realiza uma análise sintática de tokens utilizando um autômato finito determinístico (AFD) configurado a partir de um arquivo de texto. O código lê uma tabela de símbolos de um arquivo Excel, aplica o autômato para validar cada token e adiciona os resultados de reconhecimento à tabela de símbolos. A seguir, apresento uma descrição detalhada de cada parte do código:

### **Bibliotecas Utilizadas**
```python
import pandas as pd
```
- A biblioteca pandas é usada para manipulação e análise de dados, facilitando a leitura e modificação da tabela de símbolos.

### **Função carregar_automato**
```python
def carregar_automato(arquivo):
    estados = {}
    with open(arquivo, 'r') as f:
        linhas = f.read().splitlines()
        for linha in linhas:
            partes = linha.split(':')
            if len(partes) < 2:
                print(f"Linha em formato incorreto: {linha}")
                continue
            estado, transicoes = partes[0].strip(), partes[1].split(',')
            transicao_dict = {}
            for transicao in transicoes:
                entrada_destino = transicao.split()
                if len(entrada_destino) < 2:
                    print(f"Transição em formato incorreto: {transicao} em estado {estado}")
                    continue
                entrada, destino = entrada_destino
                transicao_dict[entrada] = destino
            estados[estado] = transicao_dict
    print("Leu arquivo de configuração AFD.")
    return estados

```
- Esta função lê o arquivo de configuração do AFD, construindo um dicionário de estados e transições a partir das informações lidas. Em caso de erro no formato, a função exibe mensagens informativas.

### **Função analisar_sintaxe**
```python
def analisar_sintaxe(tabela_simbolos, automato):
    resultados = []
    for index, row in tabela_simbolos.iterrows():
        estado_atual = 'q0'
        token = str(row['Token'])
        tokens = token.split()
        for token in tokens:
            if token in automato[estado_atual]:
                estado_atual = automato[estado_atual][token]
            else:
                resultados.append(False)
                break
        else:
            if 'aceitacao' in automato.get(estado_atual, {}):
                resultados.append(True)
            else:
                resultados.append(False)
    print("Converteu corretamente.")
    return resultados

```
- Esta função recebe a tabela de símbolos e o AFD carregado, iterando sobre cada token para verificar se ele é reconhecido pelo autômato. O resultado da análise (reconhecido ou não) é armazenado em uma lista de resultados.

### **Função main**
```python
def main():
    tabela_simbolos = pd.read_excel(r'C:\Users\roger\Downloads\Analise Sintatica\tabela_simbolos.xlsx')
    print(tabela_simbolos)
    print("Leu tabela de símbolos.")

    automato = carregar_automato(r'C:\Users\roger\Downloads\Analise Sintatica\automato.txt')

    resultados = analisar_sintaxe(tabela_simbolos, automato)

    tabela_simbolos['Reconhecido'] = resultados
    print(tabela_simbolos)
    print("Gerou a saída corretamente.")

if __name__ == "__main__":
    main()

```
### **A função principal do script realiza as seguintes ações:**

Lê a tabela de símbolos de um arquivo Excel.
Carrega o autômato a partir de um arquivo de texto.
Realiza a análise sintática dos tokens.
Adiciona os resultados da análise à tabela de símbolos.
Exibe a tabela de símbolos atualizada com os resultados.
Arquivos Utilizados
automato.txt: Configuração do autômato com estados e transições.
tabela_simbolos.xlsx: Arquivo Excel contendo os tokens a serem analisados.