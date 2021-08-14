def get_link_by_coordinates(z, x, y, operator='Map',
                            type_of_net='lte'):
    url = ''
    params = {}

    if operator == 'Map':
        params = {'l': 'map',
                  'v': '21.08.12-2-b210701140430',
                  'x': str(x),
                  'y': str(y),
                  'z': str(z),
                  'scale': 1,
                  'lang': 'ru_RU'}

        url = "https://core-renderer-tiles.maps.yandex.net/tiles"

    elif operator == 'Meg':
        # https://coverage-map.megafon.ru/11/1236/650.png?layers=3g
        url = 'https://coverage-map.megafon.ru/'
        url += '/'.join(map(str, (z, x, y)))
        url += '.png'

        params = {'layers': type_of_net}

    elif operator == 'Mtc':
        # https://tiles.qsupport.mts.ru/g3_New/12/2476/1304
        url = 'https://tiles.qsupport.mts.ru/'
        if type_of_net == 'lte':
            type_of_net = 'lte_New'
        elif type_of_net == '3g':
            type_of_net = 'g3_New'
        else:
            raise ValueError

        url += type_of_net
        url += '/'
        url += '/'.join(map(str, (z, x, y)))

    elif operator == 'Bel':
        # https://static.beeline.ru/upload/tiles/3G/current/14/9903/5137.png
        # https://static.beeline.ru/upload/tiles/4G/current/12/2474/1278.png
        url = 'https://static.beeline.ru/upload/tiles/'
        if type_of_net == 'lte':
            url += '4G'
        elif type_of_net == '3g':
            url += '3G'
        else:
            raise ValueError

        url += '/current/'
        url += '/'.join(map(str, (z, x, y)))
        url += '.png'

    elif operator == 'Tel':
        # https://msk.tele2.ru/maps/_4g/12/2474/1286.png
        url = 'https://msk.tele2.ru/maps/_'

        if type_of_net == 'lte':
            url += '4g/'
        elif type_of_net == '3g':
            url += '3g/'
        else:
            raise ValueError

        url += '/'.join(map(str, (z, x, y)))
        url += '.png'

    else:
        raise ValueError

    return {'url': url, 'params': params}


if __name__ == '__main__':
    z, x, y = 12, 2580, 1273

    operators = ['Meg', 'Mtc', 'Bel', 'Tel']
    connection_types = ['3g', 'lte']

    for operator in operators:
        for connection_type in connection_types:
            print(operator, connection_type)
            print(get_link_by_coordinates(z, x, y,
                                          operator=operator,
                                          type_of_net=connection_type))
