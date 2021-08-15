import os
from PIL import Image

if not os.path.exists('./map_png'):
    os.mkdir('./map_png')
path_dir = {'Bel_Tiles/lte': './map_png/bel_lte.png',
            'Bel_Tiles/3g':  './map_png/bel_3g.png',
            'Map_Tiles/Map': './map_png/map.png',
            'Meg_Tiles/3g':  './map_png/meg_3g.png',
            'Meg_Tiles/lte': './map_png/meg_lte.png',
            'Mtc_Tiles/3g':  './map_png/mtc_3g.png',
            'Mtc_Tiles/lte': './map_png/mtc_lte.png',
            'Tel_Tiles/3g':  './map_png/tel_3g.png',
            'Tel_Tiles/lte': './map_png/tel_lte.png'}
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

    new_im = Image.new('RGBA', (total_width, max_height))


    x_offset = 0
    y_offset = 0

    for i, im in enumerate(images):
        if i % y_len == 0 and i!= 0:
            y_offset = 0
            x_offset += im.size[0]

        new_im.paste(im, (x_offset, y_offset))
        y_offset += im.size[1]


    new_im.save(path_dir[path])
