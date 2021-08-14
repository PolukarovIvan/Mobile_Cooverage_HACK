import requests
import os
import time
from links import get_link_by_coordinates

# api-endpoint
example_URL = "https://core-renderer-tiles.maps.yandex.net/tiles?l=map&v=21.08.12-2-b210701140430&x=2599&y=1305&z=12&scale=1&lang=ru_RU"
URL = "https://core-renderer-tiles.maps.yandex.net/tiles"

EMPTY_TILE = requests.get(url='https://coverage-map.megafon.ru/12/2571/1271.png', params={'layers': '3g'})

OPERATORS = ['Map'] + ['Meg', 'Mtc', 'Bel', 'Tel']
CONNECTION_TYPES = ['3g', 'lte']

left_up_x = 2571
left_up_y = 1271

right_down_x = 2598
right_down_y = 1304

zoom = 12
scale = 1


class Img_parser(object):

    def __init__(self, n_jobs=-1, delay=50):
        self.url = None
        self.params = None
        self.n_jobs = n_jobs  ## for future
        self.delay = delay / 1000

    def load_img(self, url, params, headers):
        try:
            response = requests.get(url=url, params=params, headers=headers)
            if response.status_code == 404:
                return None
            if response.status_code == 200:
                return response.content
        except:
            print('Fail to load image')
            return None

    def parce_img(self, z, x, y, operator, type_of_net='Map'):

        dir = operator + '_Tiles'
        if not os.path.exists(dir):
            os.mkdir(dir)
        img_path = os.path.join(operator + '_Tiles', f'{operator}_{str(type_of_net)}_{str(x)}_{str(y)}.jpg')

        print(img_path)

        link_and_params = get_link_by_coordinates(z, x, y, operator, type_of_net)
        print(link_and_params)

        cur_img = self.load_img(**link_and_params)

        try:
            with open(img_path, 'wb') as handler:
                handler.write(cur_img)
        except FileNotFoundError as e:
            print(e.args)
            with open(img_path, 'wb') as handler:
                handler.write(EMPTY_TILE)

    def load_region(self, dir_to_save, url, boundaries, zoom):
        # boundaries = (left_up_x, left_up_x, right_down_x, right_down_y)
        start_time = time.time()

        if not os.path.exists(dir_to_save):
            os.mkdir(dir_to_save)
        for x_i in range(boundaries[0], boundaries[2]):
            for y_i in range(boundaries[1], boundaries[3]):
                for operator in OPERATORS:
                    if operator == 'Map':
                        self.parce_img(z=zoom, x=x_i, y=y_i, operator=operator)
                    else:
                        for type_of_connection in CONNECTION_TYPES:
                            self.parce_img(z=zoom, x=x_i, y=y_i,
                                           operator=operator, type_of_net=type_of_connection)

        end_time = time.time()
        print(f'Done in {end_time - start_time}')


parser = Img_parser()
parser.load_region('test', URL, (left_up_x, left_up_y, right_down_x, right_down_y), zoom=12)
