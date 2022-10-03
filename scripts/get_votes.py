# import urllib library
from urllib.request import urlopen

# import json
import json
# store the URL in url as
# parameter for urlopen
url = "https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json"

def get_votes():
    # store the response of URL
    response = urlopen(url)

    # storing the JSON response
    # from url in data
    data_json = json.loads(response.read())

    # print the json response
    return data_json

# resultado = get_votes()
# apuracoes = []
# for n in range(4):
#     apuracoes.append('{nome}: {votos}%'.format(nome=resultado['cand'][n]['nm'],votos=resultado['cand'][n]['pvap']))

# print('\n'.join(apuracoes))
