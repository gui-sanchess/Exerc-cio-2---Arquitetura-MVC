import unittest
from main import filtros_livro


class TestFiltroLivrosBDD(unittest.TestCase):

    def test_cenario_filtrar_por_catalogo(self):
        """
        Cenário: Cliente filtra livros por catálogo
        """
        # DADO (Given) que o cliente configurou o filtro para "Ficção Científica"
        filtro = {"titulo": "", "autor": "", "ano": [], "catalogo": "Ficção Científica"}

        # QUANDO (When) o sistema executa a busca no catálogo
        resultado = filtros_livro(filtro)

        # ENTÃO (Then) o resultado deve conter os livros correspondentes
        self.assertIn("Duna", resultado)
        self.assertIn("Eu, Robô", resultado)
        self.assertIn("Fundação", resultado)

    def test_cenario_filtrar_por_autor(self):
        """
        Cenário: Cliente busca todas as obras de um autor específico
        """
        # DADO (Given) que o cliente configurou o filtro para o autor "Tolkien"
        filtro = {"titulo": "", "autor": "Tolkien", "ano": [], "catalogo": ""}

        # QUANDO (When) o sistema executa a busca no catálogo
        resultado = filtros_livro(filtro)

        # ENTÃO (Then) o resultado deve ser exatamente os livros do Tolkien
        self.assertEqual(resultado, ['O Hobbit', 'O Senhor dos Anéis'])

    def test_cenario_livro_nao_encontrado(self):
        """
        Cenário: Cliente busca um autor que não existe na base
        """
        # DADO (Given) que o cliente busca por "Machado de Assis"
        filtro = {"titulo": "", "autor": "Machado de Assis", "ano": [], "catalogo": ""}

        # QUANDO (When) o sistema executa a busca
        resultado = filtros_livro(filtro)

        # ENTÃO (Then) o sistema deve retornar uma lista vazia
        self.assertEqual(resultado, [])


if __name__ == '__main__':
    unittest.main()