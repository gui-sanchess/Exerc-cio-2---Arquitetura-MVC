# 📚 App Livraria - MVP

Este repositório contém a entrega das atividades práticas da disciplina de Engenharia de Software, aplicando conceitos de **UX Design, Definição de MVP, Desenvolvimento Top-Down e Testes BDD**.

## 🎯 Sobre o Projeto (MVP)
O Produto Mínimo Viável (MVP) foi focado na **experiência de descoberta**. O objetivo é permitir que o cliente filtre o catálogo de livros por diferentes critérios de forma rápida e intuitiva. 

Funcionalidades complexas (como carrinho de compras e pagamentos) foram mapeadas na Matriz de Esforço x Resultado, mas deixadas para uma versão futura, garantindo entregas rápidas e de alto valor.

## ⚙️ Funcionalidades Implementadas
* Interface Web dinâmica utilizando **Flask** (Python).
* Filtros cruzados por **Título, Autor, Categoria e Ano**.
* Listagem de resultados com detalhes da obra (Sinopse, Estoque e Preço).
* Base de dados local em formato de dicionários (`lista_livros.py`).

## 🚀 Como rodar a aplicação

1. Certifique-se de ter o Python e o Flask instalados:
   ```bash
    pip install Flask

2. Execute o servidor backend:
   ```bash
    python app.py
    ```
3. Acesse no seu navegador o endereço

## 🧪 Como rodar os testes (BDD)
A lógica principal de filtros foi construída utilizando o método BDD (Behavior-Driven Development) seguindo a estrutura Dado-Quando-Então.
Para rodar os testes automatizados, execute no terminal:
   ```bash
    python test_bdd.py
   ```
