import os
import cv2
import shutil


def video_txt2frame_txt(sequence_path, anno_path):
    sequences = os.listdir(sequence_path)
    for sequence in sequences:
        images_name = os.listdir(os.path.join(sequence_path, sequence))
        video_txt_name = os.path.join(anno_path, sequence + '.txt')
        with open(video_txt_name, 'r') as fr:
            lines = fr.readlines()
        new_anno_path = os.path.join(anno_path, sequence)
        if not os.path.exists(new_anno_path):
            os.makedirs(new_anno_path)
        for image_name in images_name:
            image_name = (image_name.split('.'))[0]
            frame_num = int(image_name)
            objects = [x for x in lines if
                       ((x.split(','))[0] == str(frame_num) and (x.split(','))[7] != "0" and (x.split(','))[7] != "11")]
            new_anno_name = os.path.join(new_anno_path, image_name + '.txt')
            with open(new_anno_name, "w+", newline='\n') as fw:
                fw.writelines(objects)
            print(new_anno_name)


def rename(old_path, new_path):
    sequences = os.listdir(old_path)
    for sequence in sequences:
        images = os.listdir(os.path.join(old_path, sequence))
        for image in images:
            old_name = os.path.join(old_path, sequence, image)
            new_name = os.path.join(new_path, sequence + '_' + image)
            print(old_name, new_name)
            shutil.move(old_name, new_name)


if __name__ == '__main__':
    # sequence_path = "E:/data/mot/VisDrone2018-MOT-test-dev/sequences"
    # anno_path = "E:/data/mot/VisDrone2018-MOT-test-dev/annotations"
    # video_txt2frame_txt(sequence_path, anno_path)
    old_path = "E:/data/mot/VisDrone2018-MOT-test-dev/sequences"
    new_path = "E:/data/mot/VisDrone2018-MOT-test-dev/JPEGImages"
    rename(old_path, new_path)

