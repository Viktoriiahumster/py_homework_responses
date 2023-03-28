import requests
import yadisk
import os


#Задача №1
def get_all_heroes():
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url)
    list_heroes = response.json()
    return list_heroes

def find_most_intellegent_hero(hero_1, hero_2, hero_3):
    heroes = get_all_heroes()

    for hero in heroes:
        if hero['name'] == hero_1:
            intelligent_1 = hero['powerstats']['intelligence']
        elif hero['name'] == hero_2:
            intelligent_2 = hero['powerstats']['intelligence']
        elif hero['name'] == hero_3:
            intelligent_3 = hero['powerstats']['intelligence']

    if max(intelligent_1, intelligent_2, intelligent_3) == intelligent_1:
        return f'Самый умный - {hero_1}'
    elif max(intelligent_1, intelligent_2, intelligent_3) == intelligent_2:
        return f'Самый умный - {hero_2}'
    elif max(intelligent_1, intelligent_2, intelligent_3) == intelligent_3:
        return f'Самый умный - {hero_3}'

if __name__ == '__main__':
    print(find_most_intellegent_hero('Hulk', 'Captain America', 'Thanos'))

#Задача №2

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def _get_link(self, disk_file_path: str):
        file_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'OAuth {}'.format(self.token)}
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(file_url, headers=headers, params=params)
        data = response.json()
        href = data.get('href')
        return href

    def upload(self, disk_file_path: str, filename: str):
        url_to_load = self._get_link(disk_file_path=disk_file_path)
        response = requests.put(url_to_load, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 200:
            print('Success')


if __name__ == '__main__':
    path_to_file = input('Введите путь к файлу ')
    token = input('Введите токен ')
    uploader = YaUploader(token)
    uploader.upload(path_to_file, 'text.txt')