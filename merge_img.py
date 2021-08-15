import os
from PIL import Image

if not os.path.exists('./map'):
    os.mkdir('./map')
path_dir = {'Bel_Tiles/lte': './map/bel_lte.jpg',
            'Bel_Tiles/3g':  './map/bel_3g.jpg',
            'Map_Tiles/Map': './map/map.jpg',
            'Meg_Tiles/3g':  './map/meg_3g.jpg',
            'Meg_Tiles/lte': './map/meg_lte.jpg',
            'Mtc_Tiles/3g':  './map/mtc_3g.jpg',
            'Mtc_Tiles/lte': './map/mtc_lte.jpg',
            'Tel_Tiles/3g':  './map/tel_3g.jpg',
            'Tel_Tiles/lte': './map/tel_lte.jpg'}
#manual parameter
x_len = 27#61#28
y_len = 33#70#34

for path in path_dir.keys():
    print(path)
    path_to_images  = os.path.join(os.curdir, path)
    images = os.listdir(path_to_images)
    images = [os.path.join(path_to_images, img) for img in images]
    images = [Image.open(x) for x in images]

    total_width = images[0].size[0] * x_len
    max_height = images[0].size[0] * y_len

    new_im = Image.new('RGB', (total_width, max_height))


    x_offset = 0
    y_offset = 0

    for i, im in enumerate(images):
        if i % y_len == 0 and i!= 0:
            y_offset = 0
            x_offset += im.size[0]

        new_im.paste(im, (x_offset, y_offset))
        y_offset += im.size[1]


    new_im.save(path_dir[path])
