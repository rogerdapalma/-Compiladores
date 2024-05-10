# Análise sintática

-> Sisntaxe de declaração com atribuição

```less
01 D -> [TIPO] [NV] [PV]
        [TIPO] [NV] [SA] [VALOR] [PV]

02 Tipo-> int | char | float | double |

03 Valor-> digito | valorDigito

04 Digito-> 0|1|2|3|4|5|6|7|8|9

05 NV-> CARACT | caracDigito

06 CARACT-> _|A|B|...|z|A|...|Z|

07 SA-> =

08 PV-> ;

09 Condição->      BLOCO-> Tipo | SIF
                Condição-> NV sComp NV
                           NV sComp VALOR
                           VALOR sComp VALOR

10 SIF-> if | [AP] | [Condição] | [FP] | [ACH] | [BLOCO] | [FCH] OU SIF ELSE [ACH] [BLOCO] |[FCH]
```

```less
                      D
                      |
        [TIPO] [NV] [SA] [Dvalor] [PV]
           |     |    |     |       |
          INT [CARACT]|   Digito    |
           |     |    |    erro     |
           |     x    =             |
           |     |    |             |
           |     |    |             |
           |     |    |             |
           |---[INT X = Y;]---------| 
```
<span style="color: red;">  [INT X = Y;] </span>

```less
                      D
                      |
        [TIPO] [NV] [SA] [Dvalor] [PV]
           |     |    |     |       |
          INT [CARACT]|   Digito    |
           |     |    |     |       |
           |     0    =     |       |
           |     |    |     |       |
           |     |    |     0       |
           |     |    |     |       |
           |---[INT 1 = 0;]---------| 
```
<span style="color: red;"> [INT 1 = 0;] </span>

```java
    ERRO X:
[Nao foi encontrado] um digito [depois do sinal
de attribuição] na [declaração com inicialização]
```


## Sintaxe IF-ELSE



```less
                        SIF
                         |
        SIF  ELSE  [APH]                        [BLOCO]  [FCH]
            |                                       |     
            |                                      SIF
IF[AP][CONDIÇÃO][FCH][ACH][BLOCO][FCH]              |     
                          IF[AP][CONDIÇÃO][ACH][BLOCO][FCH]
                             |                     |
                             NV SIG VALOR         SIF
                                                   |
                                                 IF[BLOCO]AP[FCH]


if(A>B){_}else{if(a>b){{if(a<100>){_}}}
```

```less

[TIPO]
 |
[Condição] -----------IF
 |                    |
[NV]------------------|--idade
 |                    |    |
[SA]------------------|----|--=
 |                    |    |  |
[Dvalor]--------------|----|--|-Digito
 |                    |    |  | 18
[PV]------------------|----|--|-|--;
                      |    |  | |  |
                      |    |   \ \ |
                     if idade >= 18;               
```

```less
SIF (Structura If-Else)
|
├── IF
│   ├── Condição
│   │   ├── NV (Nome da Variável): A
│   │   ├── sComp (Símbolo de Comparação): >
│   │   └── NV (Nome da Variável): B
│   └── BLOCO
│       └── NOP (Operação Nula, representada por "_")
└── ELSE
    └── SIF (Nova Estrutura If-Else dentro do ELSE)
        └── IF
            ├── Condição
            │   ├── NV (Nome da Variável): a
            │   ├── sComp (Símbolo de Comparação): >
            │   └── NV (Nome da Variável): b
            └── BLOCO
                └── SIF (Mais um nível de IF aninhado)
                    └── IF
                        ├── Condição
                        │   ├── NV (Nome da Variável): a
                        │   ├── sComp (Símbolo de Comparação): <
                        │   └── VALOR: 100
                        └── BLOCO
                            └── NOP (Operação Nula, representada por "_")
```
