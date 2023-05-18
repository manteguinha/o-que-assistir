# Documentação do Sorteador de Filmes, Comidas e Bebidas

Este código utiliza a biblioteca `PySimpleGUI` para criar uma interface gráfica que sorteia filmes, comidas e bebidas a partir de uma lista de opções armazenada em um arquivo Excel.

## Requisitos

Você precisará das seguintes bibliotecas para executar este código:

- PySimpleGUI
- pandas

Para instalar as bibliotecas necessárias, execute o seguinte comando:

```sh
pip install PySimpleGUI pandas
```

## Como usar

O código é um script que, quando executado, exibe uma janela com um botão "SORTEAR". Ao clicar no botão, o programa seleciona aleatoriamente um filme, uma comida e uma bebida das listas de opções e exibe os resultados na janela.

### Arquivo de opções

O script utiliza um arquivo Excel chamado `lista_opcoes.xlsx` como fonte para as opções de filmes, comidas e bebidas. Este arquivo deve ter três colunas, com os seguintes cabeçalhos:

- `filmes`: Lista de opções de filmes
- `comidas`: Lista de opções de comidas
- `bebidas`: Lista de opções de bebidas

Certifique-se de que o arquivo `lista_opcoes.xlsx` esteja no mesmo diretório do script.

### Exemplo de uso

Para usar o sorteador, siga estas etapas:

1. Salve o código em um arquivo chamado, por exemplo, `sorteador.py`.
2. No mesmo diretório, coloque o arquivo `lista_opcoes.xlsx` com as opções de filmes, comidas e bebidas.
3. Execute o script `sorteador.py`:

```sh
python o_que_assistir.py
```

Uma janela será exibida com um botão "SORTEAR". Clique no botão para sortear um filme, uma comida e uma bebida aleatoriamente das listas de opções. Os resultados serão exibidos na janela.
