# Atividade Prática: Sistema de uma Biblioteca
'''
Contexto:
Você foi contratado para desenvolver um sistema de gerenciamento de biblioteca usando POO em Python.
O sistema deve modelar livros, usuários e empréstimos, com funcionalidades básicas de cadastro, consulta e operações.

Requisitos:
- O sistema deve permitir o cadastro de livros, usuários e empréstimos.
- O sistema deve permitir a consulta de livros cadastrados.
- O sistema deve permitir a consulta de usuários cadastrados.
'''

# DESAFIO (opcional) Classe LivroDigital:
# Herde de Livro e adicione o formato do e-book e formas de download.

class livros:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def __str__(self):
        return f'Titulo: {self.titulo}\nAutor: {self.autor}\nAno: {self.ano}'
    
    def __repr__(self):
        return f'Titulo: {self.titulo}\nAutor: {self.autor}\nAno: {self.ano}'
    
    def cadastro_livro(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def consulta_livro(self):
        return f'Titulo: {self.titulo}\nAutor: {self.autor}\nAno: {self.ano}'
    
    def listar_livros(self):
        for livro in self.livros:
            print(livro)

class usuarios:
    def __init__(self, id, nome, email, senha):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha

    def __str__(self):
        return f'ID: {self.id}\nNome: {self.nome}\nEmail: {self.email}\nSenha: {self.senha}'
    
    def __repr__(self):
        return f'ID: {self.id}\nNome: {self.nome}\nEmail: {self.email}\nSenha: {self.senha}'
    
    def cadastro_usuario(self, id, nome, email, senha):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha