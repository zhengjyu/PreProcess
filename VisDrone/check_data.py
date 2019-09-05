import os
import cv2


def check_init(data_path):
    sequences_path = os.path.join(data_path, 'sequences')
    initialization_path = os.path.join(data_path, 'initialization')
    object_path = os.path.join(data_path, 'objects')

    sequences = os.listdir(sequences_path)
    for sequence in sequences:
        print(sequence)
        images = os.listdir(os.path.join(sequences_path, sequence))
        image = images[0]
        with open(os.path.join(initialization_path, sequence + '.txt'), 'r') as f:
            lines = f.readlines()
        rect = lines[0].split(',')
        im = cv2.imread(os.path.join(sequences_path, sequence, image))
        x1 = int(rect[0])
        y1 = int(rect[1])
        x2 = int(rect[0]) + int(rect[2])
        y2 = int(rect[1]) + int(rect[3])
        cv2.rectangle(im, (x1, y1), (x2, y2), (0, 0, 255), 2)
        im = cv2.resize(im, (1280, 720))
        first_image = os.path.join(object_path, sequence + '.jpg')
        cv2.imwrite(first_image, im)


def check_anno(data_path):
    sequences_path = os.path.join(data_path, 'sequences')
    annotations_path = os.path.join(data_path, 'annotations')
    sequences = os.listdir(sequences_path)
    for sequence in sequences:
        print(sequence)
        images = os.listdir(os.path.join(sequences_path, sequence))
        with open(os.path.join(annotations_path, sequence + '.txt'), 'r') as f:
            lines = f.readlines()
        assert len(images) == len(lines)


if __name__ == '__main__':
    data_path = 'E:/visdrone/2019/data/VisDrone2019-SOT-test-challenge'
    # check_anno(data_path)
    check_init(data_path)