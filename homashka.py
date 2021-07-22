# Задача 1

import requests

url = [
    "https://superheroapi.com/api/2619421814940190/search/Hulk",
    "https://www.superheroapi.com/api.php/2619421814940190/search/Captain%20America",
    "https://superheroapi.com/api/2619421814940190/search/Thanos"
]

hero_dict = {}
for u in url:
    rq = requests.get(u).json()['results'][0]
    name = rq['name']
    intelligence = rq['powerstats']['intelligence']
    hero_dict[name] = intelligence
    superhero = max(name, intelligence)

print(f"{superhero} - самый умный супергерой, его интеллект равен {intelligence}")

# Задача 2


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загруджает файл file_path на яндекс диск"""

        response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload',
                                params={'path': file_path},
                                headers={'Authorization': self.token})

        href = response.json()['href']
        with open(file_path) as f:
            requests.put(href, files={'file': f})
        return response.status_code


if __name__ == '__main__':
    uploader = YaUploader('<TOKEN>')
    result = uploader.upload('test.txt')
