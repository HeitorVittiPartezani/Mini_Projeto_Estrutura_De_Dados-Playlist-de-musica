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

