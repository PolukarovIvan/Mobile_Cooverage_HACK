import cv2, time, os

def coverage_score(img_path, threshold = 1, verbose = False):
    start_time = time.time()
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    size = gray.shape[0]
    square_count = size**2
    count = len([elem for elem in gray.reshape(square_count) if elem > threshold])
    score = count/square_count
    end_time = time.time()
    if verbose:
        print(f'Done in {end_time-start_time} s')
    return score

dir_path = os.path.join(os.curdir, 'scores')
if not os.path.exists(dir_path):
    os.mkdir(dir_path)

dir_path = './scores'

path_dir = ['/Bel_Tiles/lte',
            '/Bel_Tiles/3g',
            '/Meg_Tiles/3g',
            '/Meg_Tiles/lte',
            '/Mtc_Tiles/3g',
            '/Mtc_Tiles/lte',
            '/Tel_Tiles/3g',
            '/Tel_Tiles/lte']

start = time.time()
for path in path_dir:
    files_path = os.listdir('.'+path)
    with open('./scores'+ path + '/scores.txt', 'w') as file:
        file.write('')

    for file_path in files_path:
        path_to_file = '.'+path + '/' + file_path
        print(path_to_file)
        cur_score = coverage_score(path_to_file)
        #print(cur_score)
        if file_path[4:6] == '3g':
            output =  file_path[:3] + ' ' + file_path[4:6] + ' ' + file_path[7:11] + ' ' +  file_path[12: 16] + ' ' + str(cur_score) + '\n'
        else:
            output = file_path[:3] + ' ' + file_path[4:7] + ' ' + file_path[8:12] + ' ' + file_path[13: 17] + ' ' + str(
                cur_score) + '\n'
        #print(output)
        #print('./scores'+ path + '/scores.txt')
        with open('./scores'+ path + '/scores.txt', 'a') as file:
            file.write(output)


end = time.time()
print(f'Done in {end - start}')