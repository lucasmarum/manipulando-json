#imprimindo um arquivo json copiado da internet
import json
from urllib.request import urlopen

response = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode('utf8')
dados = json.loads(response)[0]

print('título: ', dados['title'])
print('URL: ', dados['url'])
print('Duração: ', dados['duration'])
print('Número de visualizações: ', dados['stats_number_of_plays'])