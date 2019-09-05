import os
import cv2

if __name__ == '__main__':
    data_path = "F:/visdrone/2019/data/VisDrone2019-SOT-test-challenge"
    sequences_path = os.path.join(data_path, "sequences")
    anno_path = os.path.join(data_path, "annotations")
    obj_path = "F:/visdrone/2019/results/challenge_results/sot/paper/first_frame"
    sequences = os.listdir(sequences_path)
    for sequence in sequences[:35]:
        images = os.listdir(os.path.join(sequences_path, sequence))
        annos = os.path.join(anno_path, sequence + '.txt')
        with open(annos, "r") as f:
            gts = f.readlines()
        image = cv2.imread(os.path.join(sequences_path, sequence, images[0]))
        rect = gts[0].strip('\n').split(',')
        x1 = int(rect[0])
        y1 = int(rect[1])
        x2 = int(rect[0]) + int(rect[2])
        y2 = int(rect[1]) + int(rect[3])
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 5)
        image = cv2.resize(image, (1280, 720))
        # cv2.imshow("image", image)
        new_path = os.path.join(obj_path, sequence + ".jpg")
        cv2.imwrite(new_path, image)
        # cv2.waitKey(0)


