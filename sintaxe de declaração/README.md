# sintaxe de declaração com inicialização de variável

Construir uma sintaxe (de acordo com o modelo) para declaracao e inicializacao de variavel e a partir dela construir arvores de derivacao para os seguintes tokens:

**a) int x = 0 ;**

**b) float a=0.0, b, c=3.14;**

**c) int i, j=5, k=3, w=2;**

```
Declaração e Inicialização
        |
        +---> <tipo>
        |       |
        |       +---> int
        |
        +---> <identificador>
        |       |
        |       +---> x
        |
        +---> =
        |
        +---> <valor>
        |       |
        |       +---> 5
        |
        +---> ;

```

```
Declaração e Inicialização
        |
        +---> <tipo>
        |       |
        |       +---> float
        |
        +---> <identificador>
        |       |
        |       +---> y
        |
        +---> =
        |
        +---> <valor>
        |       |
        |       +---> 3.14
        |
        +---> ;

```

```
Declaração e Inicialização
        |
        +---> <tipo>
        |       |
        |       +---> float
        |
        +---> <identificador>
        |       |
        |       +---> y
        |
        +---> =
        |
        +---> <valor>
        |       |
        |       +---> 3.14
        |
        +---> ;
```