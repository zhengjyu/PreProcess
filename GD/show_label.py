import os
import cv2
import pandas as pd

defect_name2label = {
    '破洞': 1, '水渍': 2, '油渍': 3, '污渍': 4, '三丝': 5, '结头': 6, '花板跳': 7, '百脚': 8, '毛粒': 9,
    '粗经': 10, '松经': 11, '断经': 12, '吊经': 13, '粗维': 14, '纬缩': 15, '浆斑': 16, '整经结': 17, '星跳': 18, '跳花': 19,
    '断氨纶': 20, '稀密档': 21, '浪纹档': 22, '色差档': 23, '磨痕': 24, '轧痕': 25, '修痕': 26, '烧毛痕': 27, '死皱': 28, '云织': 29,
    '双纬': 30, '双经': 31, '跳纱': 32, '筘路': 33, '纬纱不良': 34,
}

def show_label(images_path, annos_name):
    images = os.listdir(images_path)
    annos = pd.read_json(open(annos_name, "r"))
    for image in images:
        img_anno = annos[annos["name"] == image]
        bboxs = img_anno["bbox"].tolist()
        defect_names = img_anno["defect_name"].tolist()
        img_path = os.path.join(images_path, image)
        im = cv2.imread(img_path)
        for bbox, defect_name in zip(bboxs, defect_names):
            print(bbox, defect_name)
            xmin = round(bbox[0])
            ymin = round(bbox[1])
            xmax = round(bbox[2])
            ymax = round(bbox[3])
            label = defect_name2label[defect_name]
            center = (int((xmin + xmax) / 2), int((ymin + ymax) / 2))
            cv2.rectangle(im, (xmin, ymin), (xmax, ymax), (0, 0, 255), 2)
            cv2.putText(im, str(label), center, cv2.FONT_HERSHEY_TRIPLEX, 2, (0, 0, 255), 2, 4)
        im = cv2.resize(im, (1280, 720))
        cv2.imshow("image", im)
        cv2.waitKey(0)


if __name__ == '__main__':
    images_path = "G:/aliyun/data/guangdong1_round1_train1_20190818/defect_Images"
    annos_name = "G:/aliyun/data/guangdong1_round1_train1_20190818/Annotations/anno_train.json"
    show_label(images_path, annos_name)
