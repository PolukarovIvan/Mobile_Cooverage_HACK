import requests
import os
import time

# api-endpoint
example_URL = "https://core-renderer-tiles.maps.yandex.net/tiles?l=map&v=21.08.12-2-b210701140430&x=2599&y=1305&z=12&scale=1&lang=ru_RU"
URL = "https://core-renderer-tiles.maps.yandex.net/tiles"
left_up_x = 5139
left_up_y = 2544

right_down_x = 5200
right_down_y = 2614

zoom = 13
scale = 1


class Img_parser(object):

    def __init__(self, n_jobs=-1, delay=50):
        self.url = None
        self.params = None
        self.n_jobs = n_jobs  ## for future
        self.delay = delay / 1000

    def make_params(self, x, y, z=13, scale=1):
        params = {'l': 'map',
                  'v': '21.08.12-2-b210701140430',
                  'x': str(x),
                  'y': str(y),
                  'z': str(z),
                  'scale': str(scale),
                  'lang': 'ru_RU'}
        return params

    def load_img_by_url(self, url, params):
        try:
            response = requests.get(url=url, params=params)
            if response.status_code == 404:
                return None
            if response.status_code == 200:
                return response.content
        except:
            print('Fail to load image')
            return None

    def load_region(self, dir_to_save, url, boundaries, zoom):
        # boundaries = (left_up_x, left_up_x, right_down_x, right_down_y)
        start_time = time.time()

        if not os.path.exists(dir_to_save):
            os.mkdir(dir_to_save)
        try:
            if len(boundaries) != 4:
                raise Exception
            for x_i in range(boundaries[0], boundaries[2]):
                for y_i in range(boundaries[1], boundaries[3]):
                    img_path = os.path.join(dir_to_save, f'map_{x_i}_{y_i}.jpg')
                    print(img_path)
                    cur_params = self.make_params(x_i, y_i, zoom)
                    cur_img = self.load_img_by_url(url, cur_params)
                    with open(img_path, 'wb') as handler:
                        handler.write(cur_img)
                    time.sleep(self.delay)
        except:
            print('Fail to load region')

        end_time = time.time()
        print(f'Done in {end_time - start_time}')


parser = Img_parser()
parser.load_region('map_zoom_13', URL, (left_up_x, left_up_y, right_down_x, right_down_y), 13)
