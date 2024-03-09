import time

prazo = 21
current_time = time.localtime()
ano = current_time.tm_year
mes = current_time.tm_mon
devolucao_dia = current_time.tm_mday + prazo

if devolucao_dia > 30:
    mes += 1
    devolucao_dia = devolucao_dia - prazo

if mes > 12:
    ano += 1


class Funcionario():
    def __init__(self, cpf: str, nome: str, endereco: str, telefone: int, email: str):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

    def infofunc(self):
        print(f'\nNome:{self.nome}\n'
              f'Cadastro de pessoa física:{self.cpf}\n'
              f'Endereço:{self.endereco}\n'
              f'Telefone:{self.telefone}\n'
              f'Email:{self.email}')


class Gerente():
    def __init__(self, nome_g: str, anos_g, funcionarios: list = None) -> None:
        self.nome_g = nome_g
        self.anos_g = anos_g
        if funcionarios is None:
            self.funcionarios = []
        else:
            self.funcionarios = funcionarios

    def addfuncionario(self, funcionario):
        self.funcionarios.append(funcionario)
        print(f'Lista de funcionários atualizada:{self.funcionarios}')

    def removefuncionario(self, funcionario):
        if funcionario in self.funcionarios:
            self.funcionarios.remove(funcionario)
            print(f'Lista de funcionários atualizada:{self.funcionarios}')
        else:
            print(f'FUncionário {funcionario} não encontrado')

    def infogerente(self):
        print(f'\nNome do gerente:{self.nome_g}\n'
              f'Quantidade de anos que o gerente trabalha para a biblioteca:{self.anos_g}\n'
              f'Lista de funcionários que trabalham para o gerente:{self.funcionarios}\n')


class Biblioteca():
    def __init__(self):
        # Estrutura de dados para armazenar as informações dos livros
        self.catalogo = [
            {"nome": "Dom Casmurro", "isbn": "978-85-01-01952-5", "data_publicacao": "1899", "editora": "Globo", "genero": "Romance" },
            {"nome": "Capitães da Areia", "isbn": "978-85-01-01679-1", "data_publicacao": "1937", "editora": "Companhia das Letras", "genero": "Ficção"},
            {"nome": "O Cortiço", "isbn": "978-85-01-04902-0", "data_publicacao": "1890", "editora": "Ática", "genero": "Ficção" }
        ]
        # Lista para armazenar os livros emprestados
        self.emprestados = []

    def infolivro(self, nome_livro: str):
        encontrado = False
        for livro in self.catalogo:
            if livro["nome"] == nome_livro:
                print(f'\nNome do livro: {livro["nome"]}\n'
                      f'ISBN: {livro["isbn"]}\n'
                      f'Data de publicação: {livro["data_publicacao"]}\n'
                      f'Editora: {livro["editora"]}\n'
                      f'Gênero: {livro["genero"]}')
                encontrado = True
                break
        if not encontrado:
            print("\nSua pesquisa não obteve resultado. Verifique se digitou o nome do livro corretamente.")

    def add_livro(self, nome, isbn, data_publicacao, editora, genero):
        novo_livro = {"nome": nome, "isbn": isbn, "data_publicacao": data_publicacao, "editora": editora, "genero": genero}
        self.catalogo.append(novo_livro)

    def delete_livro(self, deletar):
        for livro in self.catalogo:
            if deletar == livro["nome"]:
                num = input(f'\nVocê tem certeza que deseja deletar o livro "{deletar}"? Para prosseguir, digite 1.')
                if num == "1":
                    self.catalogo.remove(livro)
                    print(f'"{deletar}" deletado do catálogo!')
                    break
                else:
                    print('Operação cancelada')
                    break
            else:
                print(f'\nO livro "{deletar}" não foi encontrado no catálogo.')
                break

    def emprestar_livro(self, nome_livro):
        encontrado = False
        for livro in self.catalogo:
            if livro["nome"] == nome_livro:
                encontrado = True
                if livro not in self.emprestados:
                    self.emprestados.append(livro)
                    self.catalogo.remove(livro)
                    print(f'\nO livro "{nome_livro}" foi emprestado com sucesso!')
                else:
                    print(f'\nO livro "{nome_livro}" já está emprestado.')
                break  # Saia do loop após encontrar o livro desejado
        if not encontrado:
            print(f'\nO livro "{nome_livro}" não está disponível na biblioteca.')

    def devolver_livro(self, nome_livro):
        for livro in self.emprestados:
            if livro["nome"] == nome_livro: #se o nome_livro for igual a algum nome de livro do self.emprestados...
                self.emprestados.remove(livro)
                self.catalogo.append(livro)
                print(f'O livro "{nome_livro}" foi devolvido com sucesso!')
                return
        print(f'O livro "{nome_livro}" não foi encontrado na lista de livros emprestados.')

    def infocatalogo(self): #Mostrar as informações de todos os livros dentro do catálgo.
        for livro in self.catalogo:
            print(f'\nNome do livro:{livro["nome"]}\n'
                  f'ISBN:{livro["isbn"]}\n'
                  f'Data de publicação:{livro["data_publicacao"]}\n'
                  f'Editora:{livro["editora"]}\n'
                  f'Genero: {livro["genero"]}')



#CAMPO DE TESTES:

roberio = Funcionario('12', 'Roberio', 'Rua dos piroquios', 116969696, 'piupiugames@gmail.com')
roberio.infofunc()

nelson = Gerente('Nelson', ['José', 'João', 'Maria']) #defininfo os funcionários do gerente Nelson
nelson.infogerente() #mostrando os dados

biblioteca = Biblioteca()

biblioteca.add_livro("Os piroqueos", "6969696969696-69", "6969", "Coisas", "Maldades") #adicionando um livro ao catálogo
biblioteca.infocatalogo() #mostrando o catálogo inteiro de livros


biblioteca.infolivro("Os piroqueos") #pesquisando as informações de um livro em específico dentro do catálogo!
biblioteca.infolivro("Os nelsons") #tentando pesquisar as informações um livro que não existe no catálogo

biblioteca.emprestar_livro("O Cortiço")#empretando um dos livros do catálogo.
biblioteca.infocatalogo()#"O Cortiço" foi removido do catálogo pois fo emprestado!

biblioteca.devolver_livro("O Cortiço")
biblioteca.infocatalogo()#"O Cortiço" voltou ao catálogo depois de ser devolvido."

biblioteca.delete_livro("Dom Casmurro")
biblioteca.infocatalogo()#Como você pode observar,"Dom Casmurro" foi deletado do catálogo.

