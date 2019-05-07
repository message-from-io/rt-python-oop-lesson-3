
'''
1. Написать функцию получения IATA-кода города из его названия, используя API Aviasales.

Пример запроса:
https://www.travelpayouts.com/widgets_suggest_params?q=Из%20Москвы%20в%20Лондон

Пример ответа:
{
    "origin": {
        "iata": "MOW",
        "name": "Moscow"
    },
    "destination": {
        "iata": "LON",
        "name": "London"
    }
}
'''


import requests
import json

search_phrase = 'Из Москвы в Пензу'
link = 'https://www.travelpayouts.com/widgets_suggest_params?q={}'.format(search_phrase)

data = requests.get(link).text
moscow = json.loads(data)['origin']['iata']
penza = json.loads(data)['destination']['iata']

print('IATA-код Москвы:', moscow)
print('IATA-код Пензы:', penza)


# Результат:
#
# IATA-код Москвы: MOW
# IATA-код Пензы: PEZ
