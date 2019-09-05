# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import cv2
import os


# paint video with an annotation txt
def paint_video_txt(video_path, annotations_txt, show_anno=1):
    images = os.listdir(video_path)
    if show_anno:
        with open(annotations_txt, 'r') as f:
            annotations = f.readlines()
    for i in range(len(images)):
        image = images[i]
        rect = annotations[i].strip('\n').split(',')
        im = cv2.imread(os.path.join(video_path, image))
        if show_anno:
            x1 = int(rect[0])
            y1 = int(rect[1])
            x2 = int(rect[0]) + int(rect[2])
            y2 = int(rect[1]) + int(rect[3])
            cv2.rectangle(im, (x1, y1), (x2, y2), (0, 0, 255), 2)
        im = cv2.resize(im, (1280, 720))
        cv2.imshow("image", im)
        cv2.waitKey(5)
    pass


# paint image with an annotation xml
def paint_image_xml(image_file, annotations_file, show_anno=1, is_video=0):
    image = cv2.imread(image_file)
    if show_anno:
        annotations_tree = ET.parse(annotations_file)
        annotations_root = annotations_tree.getroot()
        objects = annotations_root.findall("object")
        for object in objects:
            name = object.find('name').text
            if name != 'person':
                print("2")
                print(annotations_file)
            occluded = object.find('occluded')
            # print(occluded)
            if occluded is not None:
                occluded = int(occluded.text)
                if occluded == 1:
                    print(annotations_file)
            bndbox = object.find('bndbox')
            xmin = int(bndbox.find('xmin').text)
            ymin = int(bndbox.find('ymin').text)
            xmax = int(bndbox.find('xmax').text)
            ymax = int(bndbox.find('ymax').text)
            cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (255, 0, 0), 2)
            cv2.putText(image, name, (xmax, ymin), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255))
        image = cv2.resize(image, (1000, 500))
        cv2.imshow("image", image)
    if is_video:
        cv2.waitKey(5)
    else:
        cv2.waitKey(0)


def paint_video_xml(video_path, annotations_path, show_anno=1):
    images = os.listdir(video_path)
    for i in range(len(images)):
        image = images[i]
        xml = image.replace('jpg', 'xml')
        image_file = os.path.join(video_path, image)
        xml_file = os.path.join(annotations_path, xml)
        paint_image_xml(image_file, xml_file, 1, 1)
