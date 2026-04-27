from lista_livros import meus_livros


def filtros_livro(filtro):
    livros_encontrados = []

    for livro in meus_livros:
        if filtro.get("titulo") != "" and livro["titulo"] == filtro.get("titulo"):
            livros_encontrados.append(livro["titulo"])

        elif filtro.get("autor") != "" and livro["autor"] == filtro.get("autor"):
            livros_encontrados.append(livro["titulo"])

        elif filtro.get("ano") != [] and livro["ano"] == filtro.get("ano"):
            livros_encontrados.append(livro["titulo"])

        elif filtro.get("catalogo") != "" and livro["catalogo"] == filtro.get("catalogo"):
            livros_encontrados.append(livro["titulo"])

    return livros_encontrados