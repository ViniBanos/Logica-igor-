sum_das_notas = sum(notas.values())
n_de_disciplinas = len(notas)
media = sum_das_notas / n_de_disciplinas

pessoas = [ 
    {
        "nome" : "Igor",
        "idade": "20 anos",
        "id": "SP12345",
        "notas":{
            "portugues": 6,
            "matematica": 9,
            "ciencias": 2,
            "media": 10
        }
    },

    {
        "nome" : "Ana",
        "idade": "19 anos",
        "id": "SP54321",
        "notas": {
            "portugues": 3,
            "matematica": 3,
            "ciencias": 10,
            "media": 10
        }
    }
]

def get_pessoas():
    return pessoas

print (pessoas())

def add_pessoas():
    return 