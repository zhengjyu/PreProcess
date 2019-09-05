import os


if __name__ == '__main__':
    det_path = "E:/visdrone/2018/mot/fpn_result/test"
    mot_path = "E:/visdrone/2018/mot/det_fpn"
    det_results = os.listdir(det_path)
    for det_result in det_results:
        mot_name = det_result[:18]
        with open(os.path.join(det_path, det_result), "r") as fr:
            lines = fr.readlines()
        for line in lines:
            x = line.strip("\n").split(",")
            w = int(x[4])
            h = int(x[5])
            if w == 0 or h == 0:
                print(x)
                print(mot_name)
        with open(os.path.join(mot_path, mot_name + '.txt'), "a+", newline="\n") as fw:
            fw.writelines(lines)
        print(mot_name)



