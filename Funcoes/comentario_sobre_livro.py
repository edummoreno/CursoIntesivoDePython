# comentario_sobre_livro.py

def livro_bom(livro):
    """Comenta sobre a qualidade de um livro."""
    print(f"Então o livro {livro} é bom?")

# Pede ao usuário para informar um livro e chama a função para comentar sobre ele.
livro = input("Qual seu livro favorito? ")
livro_bom(livro)
