# Playlist com Lista Duplamente Ligada - Fatec Rio Claro

Este projeto é uma implementação de uma playlist de músicas utilizando uma estrutura de dados de lista duplamente ligada em Python. Desenvolvido como parte da pré-avaliação para a Fatec Rio Claro, o programa simula as funcionalidades de um player de música real.

O objetivo principal é demonstrar a aplicação prática de listas duplamente ligadas, permitindo ao usuário navegar entre as faixas, adicionar, remover e gerenciar o estado da reprodução.

## ✨ Funcionalidades

- **Adicionar Músicas**: Insira novas músicas no final da playlist, informando o título e o artista.
- **Remover Músicas**: Exclua músicas específicas da playlist pelo título.
- **Navegação Completa**: Avance para a próxima música ou retroceda para a anterior com facilidade.
- **Tocar e Pausar**: Alterne o estado da música atual entre "Tocando" e "Pausada".
- **Listar a Playlist**: Exiba todas as faixas da playlist, com um indicador mostrando qual música está selecionada e seu status (tocando/pausada).
- **Persistência de Dados (Desafio Extra)**: Salve o estado atual da sua playlist em um arquivo JSON e carregue-a posteriormente para não perder suas músicas.

## 📂 Estrutura de Arquivos

O projeto é organizado em dois arquivos principais para separar a lógica da estrutura de dados da interface do usuário:

- `ClassLibrary.py`: Contém as classes `No` (que representa cada música) e `Playlist` (que implementa a lista duplamente ligada e gerencia todas as operações).
- `main.py`: Responsável pela interface interativa do usuário via console (CLI), exibindo o menu e capturando as entradas do usuário.

## 🛠️ Pré-requisitos

Para executar este projeto, você precisará ter:

- Python 3.x

## 🚀 Como Executar

1.  **Clone o repositório:**
    ```sh
    git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
    ```

2.  **Navegue até o diretório do projeto:**
    ```sh
    cd SEU_REPOSITORIO
    ```

3.  **Execute o script principal:**
    ```sh
    python main.py
    ```

Após a execução, um menu interativo será exibido no terminal, permitindo que você utilize todas as funcionalidades da playlist.

## 🖥️ Exemplo de Uso

```
======= Playlist Fatec Rio Claro =======
1. Adicionar música
2. Remover música
3. Avançar para a próxima música
4. Retroceder para a música anterior
5. Tocar/Pausar música
6. Exibir playlist atual
7. Salvar playlist em JSON
8. Carregar playlist de JSON
9. Sair
======================================
Escolha uma opção: 1
Digite o título da música: Nothing Else Matters
Digite o nome do artista: Metallica
Música 'Nothing Else Matters' por Metallica adicionada com sucesso!

Escolha uma opção: 1
Digite o título da música: Bohemian Rhapsody
Digite o nome do artista: Queen
Música 'Bohemian Rhapsody' por Queen adicionada com sucesso!

Escolha uma opção: 6

--- Playlist Atual ---
1. Nothing Else Matters - Metallica <-- ⏸️ Pausado
2. Bohemian Rhapsody - Queen
----------------------

Escolha uma opção: 5
▶️ Tocando: Nothing Else Matters - Metallica

Escolha uma opção: 3
▶️ Tocando agora: Bohemian Rhapsody - Queen
```

