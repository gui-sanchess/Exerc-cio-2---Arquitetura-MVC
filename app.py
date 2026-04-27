from flask import Flask, render_template, request
from lista_livros import meus_livros

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    # 1. Cria listas únicas e ordenadas puxando direto do banco de dados
    titulos_unicos = sorted(list(set([livro['titulo'] for livro in meus_livros])))
    autores_unicos = sorted(list(set([livro['autor'] for livro in meus_livros])))
    categorias_unicas = sorted(list(set([livro['catalogo'] for livro in meus_livros])))
    anos_unicos = sorted(list(set([livro['ano'] for livro in meus_livros])), reverse=True)

    # 2. Pega as escolhas do cliente nos selects do HTML
    filtro_titulo = request.args.get('titulo', '')
    filtro_autor = request.args.get('autor', '')
    filtro_categoria = request.args.get('categoria', '')
    filtro_ano = request.args.get('ano', '')

    livros_filtrados = []

    # 3. Lógica de Filtragem Exata (já que agora ele seleciona de uma lista)
    for livro in meus_livros:
        if filtro_titulo and filtro_titulo != livro["titulo"]:
            continue
        if filtro_autor and filtro_autor != livro["autor"]:
            continue
        if filtro_categoria and filtro_categoria != livro["catalogo"]:
            continue
        if filtro_ano and int(filtro_ano) != livro["ano"]:
            continue

        livros_filtrados.append(livro)

    # 4. Envia tudo para a tela
    return render_template('index.html',
                           livros=livros_filtrados,
                           titulos=titulos_unicos,
                           autores=autores_unicos,
                           categorias=categorias_unicas,
                           anos=anos_unicos)


if __name__ == '__main__':
    app.run(debug=True)