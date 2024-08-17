pessoas = [
    {
        "nome": "Igor",
        "idade": "20 anos",
        "id": "SP12345",
        "notas": {
            "portugues": 6,
            "matematica": 9,
            "ciencias": 2,
        }
    },
    {
        "nome": "Ana",
        "idade": "19 anos",
        "id": "SP54321",
        "notas": {
            "portugues": 3,
            "matematica": 3,
            "ciencias": 10,
        }
    }
]

def calc_media(pessoa):
    notas = pessoa["notas"]
    sum_das_notas = sum(notas.values())
    n_de_disciplinas = len(notas)
    media = sum_das_notas / n_de_disciplinas
    return media

def get_pessoas():
    print(pessoas)

def add_pessoa():
    pessoa = {}
    for i in pessoas[0].keys():
        print('Digite o Campo ', i)
        valor = input()
        pessoa[i] = valor
    pessoas.append(pessoa)

add_pessoa()
get_pessoas()
