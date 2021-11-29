import json
import requests

req = requests.get("https://api.estagio.amfernandes.com.br/imoveis")
dados = json.loads(req.content)

print("opções: bairro | cep | cidade | nome | planta")
info = input("digite a informação desejada: ")
#código não possue algortimo de ordenação [dificuldades trabalhando com o Json]


for local in dados:
    resposta = local[info]
    print(resposta)
 
