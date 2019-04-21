import os
import cv2


def space2comma_txt(src, dst):
    with open(src, 'r') as f:
        lines = f.readlines()
    new_lines = []
    for line in lines:
        rect = line.split(' ')
        new_rect = "%s,%s,%s,%s" % (rect[0], rect[1], rect[2], rect[3])
        new_lines.append(new_rect)
    with open(dst, 'w+', newline='\n') as w:
        w.writelines(new_lines)


if __name__ == '__main__':
    a_txt = 'E:/visdrone/2018/sot/VisDrone2018-SOT_toolkit/data/VisDrone2018/VisDrone2018-SOT-test-challenge/annotations/uav0000244_00479_s.txt'
    b_txt = 'E:/visdrone/2018/sot/VisDrone2018-SOT_toolkit/data/VisDrone2018/VisDrone2018-SOT-test-challenge/uav0000244_00479_s.txt'
    space2comma_txt(a_txt, b_txt)
