# MathScript Documentação

## Ideia geral

O MathScript tem como ideia geral ser uma linguagem de processamento em massa de dados numéricos, com alta pressisão e responsividade.
Com umas sintaxe proxima a propria linguagem matemática, seu uso deve ser fácil e sua curva de aprendizado simples.


## Variáveis
As váriaveis são divididas em 3 tipos primitivos e 1 estrutura de daso complexa.
### tipos:
        num => tipo numérico, comportando números de ponto flutuante
        text => tipo de texto - recebendo qualquer valor entre " "
        bool => tipo boleano, true ou false
        conjuntos => Estrutura de dados de tamanho livre mas as variaveis internas imutáveis em valor e posição.

### atribuição:
        := => atribuição simples
        += => atribuição por soma
        -= => atribuição por subtração
        *= => atribuição por multiplicação
        /= => atribuição por divisão
        **= => atribuição por exponenciação
        //= => atribuição por redicionamento
        %= => atribuição por módulo

## Operadores
### operadores aritiméticos: 
        + => soma
        - => subtração
        * => multiplicação
        / => divisão
        ** => exponenciação
        // => rediciação
        % => módulo

### Operadores Lógicos:
        and => E lógico
        or => OU lógico
        not => NÃO lógico
        xand => Xand lógico
        xor => Xor lógico
        xnot => Xnot lógico
        not= => Diferente
        == => Igualdade
        < => Menor que
        > => Maior que
        <= => Menor ou igual a
        >= => Maior ou igual a

## Blocos de codigo
blocos de codigo são definidos em mathscript por `<>` onde os comandos são escritos dentro. Por exemplo:

```
num var := < codigo >
```
os blocos devem ter algum valor de retorno. que serão entreges a uma variavel apos o termino de sua execução.

## Funções
A definição de um bloco de função em MathScript é feita através da palavra-chave `fun`, seguida pelo nome da função e seus parâmetros entre parênteses. O corpo da função é definido entre chaves `{}`. Por exemplo:

```
fun minhaFuncao(param1, param2) {
    // corpo da função
}
```

essas funções não retornam valores, servem para criar novos valores a partir da entrada dos dados.
Se o parametro inserido for uma variável unica, ele prosseguirá normalmente, contudo se for um conjunto, ele percorrerá o conjunto e aplicará a função a cada elemento.
variaveis criadas dentro das funções são globais e passam a integrar todo o programa.

## Estruturas de Controle

As estruturas de controle em MathScript permitem que você execute diferentes blocos de código com base em condições. As principais estruturas de controle são:

### Condicional
A estrutura condicional é definida pela palavra-chave `if`, seguida pela condição e seguida por `->` onde o bloco será escrito na propria linha. Por exemplo:

```
if (condicao) -> < codigo >
```

## Formato inicial esperado do codigo:

```
num grupo1 := (/*valores iniciais*/)

fun função(input){
    if (grupo1 % 2 = 0) -> <num grupo2 := (grupo1)>
}

console.print(grupo2)
```
Nesse script é criado um conjunto de numeros pares (grupo2) a partir de um grupo de entrada (grupo1). Esse grupos2 passa a fazer parte do codigo como um todo sendo uma variável acessível em qualquer parte do script.