import json

class No:
    """
    Representa cada música (nó) na lista duplamente ligada.
    """
    def __init__(self, titulo, artista):
        """
        Inicializa um novo nó (música).
        Args:
            titulo (str): O nome da música.
            artista (str): O nome do artista ou banda.
        """
        self.titulo = titulo
        self.artista = artista
        self.anterior = None
        self.proximo = None

class Playlist:
    """
    Gerencia a estrutura de dados da lista duplamente ligada e as operações da playlist.
    """
    def __init__(self):
        """
        Inicializa a playlist, que começa vazia e pausada.
        """
        self.inicio = None
        self.fim = None
        self.atual = None
        self.tocando = False # Novo atributo para controlar o estado de reprodução

    def tocar_pausar(self):
        """
        Alterna entre tocar e pausar a música atual.
        """
        if self.atual is None:
            print("A playlist está vazia. Adicione uma música primeiro.")
            return

        self.tocando = not self.tocando # Inverte o estado (True -> False, False -> True)
        
        if self.tocando:
            print(f"▶️ Tocando: {self.atual.titulo} - {self.atual.artista}")
        else:
            print(f"⏸️ Pausado: {self.atual.titulo} - {self.atual.artista}")
            
    def adicionar_musica(self, titulo, artista):
        """
        Adiciona uma nova música no final da playlist.
        """
        nova_musica = No(titulo, artista)
        if self.inicio is None:
            self.inicio = nova_musica
            self.fim = nova_musica
            self.atual = nova_musica
        else:
            self.fim.proximo = nova_musica
            nova_musica.anterior = self.fim
            self.fim = nova_musica
        print(f"Música '{titulo}' por {artista} adicionada com sucesso!")

    def remover_musica(self, titulo):
        """
        Remove uma música específica da playlist pelo título.
        """
        if self.inicio is None:
            print("A playlist está vazia.")
            return

        no_a_remover = self.inicio
        while no_a_remover:
            if no_a_remover.titulo.lower() == titulo.lower():
                if self.atual == no_a_remover:
                    self.tocando = False # Pausa a reprodução se a música atual for removida

                if no_a_remover == self.inicio and no_a_remover == self.fim:
                    self.inicio = self.fim = self.atual = None
                elif no_a_remover == self.inicio:
                    self.inicio = no_a_remover.proximo
                    self.inicio.anterior = None
                    if self.atual == no_a_remover: self.atual = self.inicio
                elif no_a_remover == self.fim:
                    self.fim = no_a_remover.anterior
                    self.fim.proximo = None
                    if self.atual == no_a_remover: self.atual = self.fim
                else:
                    no_a_remover.anterior.proximo = no_a_remover.proximo
                    no_a_remover.proximo.anterior = no_a_remover.anterior
                    if self.atual == no_a_remover: self.atual = no_a_remover.proximo
                
                print(f"Música '{titulo}' removida.")
                return
            no_a_remover = no_a_remover.proximo
        
        print(f"Música '{titulo}' não encontrada na playlist.")

    def avancar(self):
        """
        Avança para a próxima música e a toca automaticamente.
        """
        if self.atual and self.atual.proximo:
            self.atual = self.atual.proximo
            self.tocando = True
            print(f"▶️ Tocando agora: {self.atual.titulo} - {self.atual.artista}")
        elif self.atual is None:
            print("A playlist está vazia.")
        else:
            print("Você já está na última música da playlist.")

    def retroceder(self):
        """
        Retrocede para a música anterior e a toca automaticamente.
        """
        if self.atual and self.atual.anterior:
            self.atual = self.atual.anterior
            self.tocando = True
            print(f"▶️ Tocando agora: {self.atual.titulo} - {self.atual.artista}")
        elif self.atual is None:
            print("A playlist está vazia.")
        else:
            print("Você já está na primeira música da playlist.")

    def exibir_playlist(self):
        """
        Lista todas as músicas, indicando a que está tocando ou pausada.
        """
        if self.inicio is None:
            print("A playlist está vazia.")
            return
        
        print("\n--- Playlist Atual ---")
        no_atual = self.inicio
        contador = 1
        while no_atual:
            status = ""
            if no_atual == self.atual:
                status = " <-- ▶️ Tocando Agora" if self.tocando else " <-- ⏸️ Pausado"
            
            print(f"{contador}. {no_atual.titulo} - {no_atual.artista}{status}")
            no_atual = no_atual.proximo
            contador += 1
        print("----------------------\n")
        
    def salvar_em_json(self, nome_arquivo="playlist.json"):
        """
        (Desafio Extra) Salva a playlist atual em um arquivo JSON.
        """
        if self.inicio is None:
            print("Nada para salvar. A playlist está vazia.")
            return

        lista_musicas = []
        no_atual = self.inicio
        while no_atual:
            lista_musicas.append({"titulo": no_atual.titulo, "artista": no_atual.artista})
            no_atual = no_atual.proximo
        
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            json.dump(lista_musicas, f, indent=4, ensure_ascii=False)
        
        print(f"Playlist salva com sucesso em '{nome_arquivo}'.")

    def carregar_de_json(self, nome_arquivo="playlist.json"):
        """
        (Desafio Extra) Carrega uma playlist de um arquivo JSON.
        """
        try:
            with open(nome_arquivo, 'r', encoding='utf-8') as f:
                lista_musicas = json.load(f)
            
            self.inicio = self.fim = self.atual = None
            self.tocando = False # Reseta o estado ao carregar
            
            for musica in lista_musicas:
                self.adicionar_musica(musica['titulo'], musica['artista'])
            
            print(f"Playlist carregada de '{nome_arquivo}'.")
        except FileNotFoundError:
            print(f"Arquivo '{nome_arquivo}' não encontrado.")
        except json.JSONDecodeError:
            print(f"Erro ao decodificar o arquivo JSON '{nome_arquivo}'.")