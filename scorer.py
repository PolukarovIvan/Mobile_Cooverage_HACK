import cv2, time

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


if __name__ == '__main__':
    #print(coverage_score('image.jpg'))
    pass