import os
import numpy as np


def divide(old_path, new_path):
    files = os.listdir(old_path)
    for file in files:
        with open(os.path.join(old_path, file), 'r') as fr:
            lines = fr.readlines()
        for i in range(1, 11):
            new_lines = []
            for line in lines:
                category = int(line.strip("\n").split(',')[7])
                if i == category:
                    new_lines.append(line)
            if len(new_lines) != 0:
                with open(os.path.join(new_path, file.split('.')[0] + "_" + str(i) + ".txt"), "w+", newline="\n") as fw:
                    fw.writelines(new_lines)
            print(os.path.join(new_path, file.split('.')[0] + "_" + str(i) + ".txt"))


def merge(old_path, new_path, det_path):
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    files = os.listdir(det_path)

    for file in files:
        new_lines = []
        for i in range(1, 11):
            if not os.path.exists(os.path.join(old_path, file.split('.')[0] + "_" + str(i) + ".txt")):
                continue
            with open(os.path.join(old_path, file.split('.')[0] + "_" + str(i) + ".txt"), 'r') as fr:
                lines = fr.readlines()
            for line in lines:
                line_split = line.strip("\n").split(",")
                # line_split = line.strip("\n").split(" ")
                ids = int(line_split[1]) + 20000 * (i - 1)
                new_lines.append("%s,%d,%s,%s,%s,%s,%s,%s,%s,%s\n" % (line_split[0], ids, line_split[2], line_split[3],line_split[4],
                                                                    line_split[5],line_split[6],line_split[7],line_split[8],line_split[9]))
        with open(os.path.join(new_path, file), 'w', newline="\n") as fw:
            fw.writelines(new_lines)


if __name__ == '__main__':
    # old_path = "E:/visdrone/2018/mot/VisDrone2018-MOT-test-dev/det_fpn"
    # new_path = "E:/visdrone/2018/mot/VisDrone2018-MOT-test-dev/det_fpn_category"
    # divide(old_path, new_path)

    det_path = "F:/visdrone/2018/mot/VisDrone2018-MOT-test-dev/det_fpn"
    old_path = "F:/visdrone/VisDrone-MOT-toolkit/trackers/CMOT/output"
    new_path = "F:/visdrone/VisDrone-MOT-toolkit/trackers/CMOT/output_new"
    merge(old_path, new_path, det_path)
