import json
#Criando um dict
dict_guido = {'nome': 'Guido van Rossun',
              'linguagem': 'Python',
              'similar': ['c','Modula-3', 'lisp'],
              'users': 1000000}


json.dumps(dict_guido)
with open(r'C:\Users\lucas\dados.json', 'w') as arquivo:
    arquivo.write(json.dumps(dict_guido))
with open(r'C:\Users\lucas\dados.json', 'r') as arquivo:
    texto = arquivo.read()
    dados = json.loads(texto)
dados
print(dados['nome'])
