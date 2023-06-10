from pprint import pprint

import requests
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        filename = file_path.split('/', )[-1]
        params = {
            "path": f"{filename}"
        }
        headers = {
            'Authorization': token
        }
        response_1 = requests.get(url, headers=headers, params=params).json()
        href = response_1.get("href", "")
        with open(path_to_file, 'rb') as f:
            response_2 = requests.put(href, files={"file": f})



if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = '2.png'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    print(f'Файл {path_to_file} загружен')
