from ClassLibrary import Playlist

def exibir_menu():
    """Exibe o menu de opções para o usuário."""
    print("\n======= Playlist Fatec Rio Claro =======")
    print("1. Adicionar música")
    print("2. Remover música")
    print("3. Avançar para a próxima música")
    print("4. Retroceder para a música anterior")
    print("5. Tocar/Pausar música") # Nova opção
    print("6. Exibir playlist atual")
    print("7. Salvar playlist em JSON")
    print("8. Carregar playlist de JSON")
    print("9. Sair") # Opção Sair renumerada
    print("======================================")

def main():
    """Função principal que executa o programa da playlist."""
    minha_playlist = Playlist()

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            titulo = input("Digite o título da música: ")
            artista = input("Digite o nome do artista: ")
            minha_playlist.adicionar_musica(titulo, artista)
        
        elif escolha == '2':
            titulo = input("Digite o título da música que deseja remover: ")
            minha_playlist.remover_musica(titulo)
            
        elif escolha == '3':
            minha_playlist.avancar()
            
        elif escolha == '4':
            minha_playlist.retroceder()

        elif escolha == '5': # Nova lógica para a opção 5
            minha_playlist.tocar_pausar()

        elif escolha == '6':
            minha_playlist.exibir_playlist()
            
        elif escolha == '7':
            nome_arquivo = input("Digite o nome do arquivo para salvar (ex: minha_playlist.json): ")
            minha_playlist.salvar_em_json(nome_arquivo)
            
        elif escolha == '8':
            nome_arquivo = input("Digite o nome do arquivo para carregar (ex: minha_playlist.json): ")
            minha_playlist.carregar_de_json(nome_arquivo)

        elif escolha == '9': # Opção Sair atualizada
            print("Encerrando o programa. Até mais!")
            break
        
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()