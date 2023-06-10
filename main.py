import requests
url = 'https://akabab.github.io/superhero-api/api/all.json'
resource = requests.get(url)
text = resource.json()


def who_is_the_smartest(name):
    dict_hero = {}
    list_hero = []
    for list_text in text:
        for names in name:
            if list_text['name'] == names:
                list_hero.append(list_text['powerstats']['intelligence'])
                dict_hero[names] = list_text['powerstats']['intelligence']
    list_hero_sort = list(reversed(list_hero))
    for name, number in dict_hero.items():
        for numb in list_hero:
            if numb < number:
                intelligence_super_hero = number
                name_hero = name
    print(f'Самый умный супергерой: {name_hero} = {intelligence_super_hero}')




who_is_the_smartest(['Hulk', 'Captain America', 'Thanos'])




