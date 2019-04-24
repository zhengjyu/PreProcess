import os
from PreProcess.show_image_label import paint_video_txt, paint_video_xml


def show_data_txt():
    path = 'E:/visdrone/2019/data/VisDrone2019-SOT-test-challenge'
    sequences_path = os.path.join(path, 'sequences')
    annotations_path = os.path.join(path, 'annotations')
    sequences = os.listdir(sequences_path)
    for s in range(len(sequences)):
        sequence = sequences[s]
        print(sequence)
        video_path = os.path.join(sequences_path, sequence)
        annotations_txt = os.path.join(annotations_path, sequence + '.txt')
        paint_video_txt(video_path, annotations_txt, show_anno=1)


def show_data_xml():
    path = 'E:/visdrone/2019/data/visdrone2019_sot/sequences'
    sequences_path = os.path.join(path, 'sequences')
    annotations_path = os.path.join(path, 'annotations_xml')
    sequences = os.listdir(sequences_path)
    for s in range(len(sequences)):
        sequence = sequences[s]
        print(sequence)
        video_path = os.path.join(sequences_path, sequence)
        xml_path = os.path.join(annotations_path, sequence)
        paint_video_xml(video_path, xml_path, show_anno=1)


if __name__ == '__main__':
    show_data_txt()
    # show_data_xml()
