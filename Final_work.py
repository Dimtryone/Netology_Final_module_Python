import requests
from urllib.parse import urlencode
import webbrowser
from urllib.parse import urlparse

class VKCustomer:
    URL_BASE = 'https://api.vk.com/method/'
    URL_REDIRECT = 'https://oauth.vk.com/blank.html'
    URL_AUTH = 'https://oauth.vk.com/authorize/'
    APP_ID = 51449059
    METHOD_GET_PHOTOS = 'photos.get'
    FRIENDS = 'friends'
    PHOTOS = 'photos'
    AUDIO = 'audio'
    WALL = 'wall'
    SCOPE_LIST: list[str] = [FRIENDS, PHOTOS, AUDIO, WALL]
    SCOPE: str = ','.join(SCOPE_LIST)
    PROTOCOL_VERSION = '5.131'

    def __init__(self, user_id):
        self.user_id = user_id
        self.token = ''

    def get_token(self):
        param = {
            "client_id": self.APP_ID,
            "redirect_uri": self.URL_REDIRECT,
            "display": 'page',
            "scope": self.SCOPE,
            "response_type": "token"
        }
        print('')
        webbrowser.open('?'.join((self.URL_AUTH, urlencode(param))), new=1)
        url_back = input('вставьте скопированную строку из открывшейся страницы:')
        strange = urlparse(url_back)
        str_with_token = strange[5]
        list_with_token = str_with_token.split('&')
        token = list_with_token[0]
        token = token.replace('access_token=', '')
        self.token = token
        print('токен сохранен')


    def __get_url__(self, name_method) -> str:
        return f'{self.URL_BASE}{name_method}'

    def get_photos(self):
        url = self.__get_url__(self.METHOD_GET_PHOTOS)
        album_ID = ['wall', 'profile', 'saved']
        param = {
            'access_token': self.token,
            'owner_id': self.user_id,
            'album_id': album_ID[1],
            'extended': '1',
            'photo_sizes': '1',
            'v': self.PROTOCOL_VERSION
        }

        response = requests.get(url, param)
        response.json()
        print('Фото успешно загружены')


example_user_ID = 1

vk_client = VKCustomer(example_user_ID)
vk_client.get_token()
vk_client.get_photos()

print('the end')


#OWNER_ID = '2481318'
#URL_PHOTOS = 'api.vk.com/method/photos.get'
#METHOD_GET_PHOTOS = 'photos.get'
#PROTOCOL_VERSION: str = "5.131"
#params = {'access_token':TOKEN_MY, 'owner_id': OWNER_ID, 'album_id': 'profile', 'extended': 1, 'photo_sizes': 1, 'V': PROTOCOL_VERSION}
#response = requests.get(url=URL_PHOTOS, params=params)
#print(response.json())
