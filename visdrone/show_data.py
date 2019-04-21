import os
from PreProcess.Show_Image_Label import paint_video_txt


if __name__ == '__main__':
    path = 'E:/visdrone/2018/sot/VisDrone2018-SOT_toolkit/data/VisDrone2018/VisDrone2018-SOT-test-dev'
    sequences_path = os.path.join(path, 'sequences')
    annotations_path = os.path.join(path, 'annotations')
    sequences = os.listdir(sequences_path)
    a = 35
    for s in range(a-1, a):
        sequence = sequences[s]
        print(sequence)
        video_path = os.path.join(sequences_path, sequence)
        annotations_txt = os.path.join(annotations_path, sequence + '.txt')
        paint_video_txt(video_path, annotations_txt, show_anno=1)
