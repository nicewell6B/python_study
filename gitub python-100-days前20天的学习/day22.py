import json

my_dict = {
   'name': "刘滨豪",
    'age': 17,
    'friends': ["jdfs","jdsfjd"],
    'cars': [
        {"brand": "BMW", "max_speed": 240},
        {"brand": "Benz", "max_speed":280},
        {"brand": "Audi", "max_speed": 280}
    ]
}
print(json.dumps(my_dict))

import json


with open('data.json','w') as file:
    json.dump(my_dict,file)
with open('data.json', 'r') as file:
    my_dict = json.load(file)
    print(type(my_dict))
    print(my_dict)

'''import requests

resp = requests.get('https://api.tianapi.com/guonei/?key=APIKey&num=10')
if resp.status_code == 200:
    data_model = resp.json()
    for news in data_model['newslist']:
        print(news['title'])
        print(news['url'])
        print('-' * 60)'''

