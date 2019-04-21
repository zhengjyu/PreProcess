# -*- coding utf-8 -*-
import os
from xml.dom.minidom import Document
import cv2
import numpy as np


# transform txt to xml
def generate_xml(img_name, lines, img_size, name_class):
    doc = Document()

    def append_xml_node_attr(child, parent=None, text=None):
        ele = doc.createElement(child)
        if not text is None:
            text_node = doc.createTextNode(text)
            ele.appendChild(text_node)
        parent = doc if parent is None else parent
        parent.appendChild(ele)
        return ele

    # create header
    annotation = append_xml_node_attr('annotation')
    append_xml_node_attr('folder', parent=annotation, text='UAV')
    append_xml_node_attr('filename', parent=annotation, text=img_name)
    source = append_xml_node_attr('source', parent=annotation)
    append_xml_node_attr('database', parent=source, text='UAV')
    append_xml_node_attr('annotation', parent=source, text='UAV')
    append_xml_node_attr('image', parent=source, text='UAV')
    append_xml_node_attr('flickrid', parent=source, text='000000')
    owner = append_xml_node_attr('owner', parent=annotation)
    append_xml_node_attr('url', parent=owner, text='UAV')
    size = append_xml_node_attr('size', annotation)
    append_xml_node_attr('width', size, str(img_size[1]))
    append_xml_node_attr('height', size, str(img_size[0]))
    append_xml_node_attr('depth', size, str(img_size[2]))
    append_xml_node_attr('segmented', parent=annotation, text='0')

    # create objects
    objs = []
    for line in lines:
        splitted_line = line.strip().lower().split(',')

        cls = name_class[splitted_line[5]]
        occlusion = int(splitted_line[7])

        x1, y1, x2, y2 = int(splitted_line[0]), int(splitted_line[1]), int(splitted_line[0]) + int(
            splitted_line[2]), int(splitted_line[1]) + int(splitted_line[3])
        truncation = int(splitted_line[6])
        difficult = 0
        truncted = 0 if truncation < 1 else 1
        obj = append_xml_node_attr('object', parent=annotation)
        append_xml_node_attr('name', parent=obj, text=cls)
        append_xml_node_attr('pose', parent=obj, text="top")
        append_xml_node_attr('truncated', parent=obj, text=str(truncted))
        append_xml_node_attr('difficult', parent=obj, text=str(int(difficult)))
        bb = append_xml_node_attr('bndbox', parent=obj)
        append_xml_node_attr('xmin', parent=bb, text=str(x1))
        append_xml_node_attr('ymin', parent=bb, text=str(y1))
        append_xml_node_attr('xmax', parent=bb, text=str(x2))
        append_xml_node_attr('ymax', parent=bb, text=str(y2))
    return doc


if __name__ == '__main__':
    annpath = "/media/lirun/04962EB6962EA7DE/tju/data/VisDrone2018-DET-val/annotations"
    imagepath = "/media/lirun/04962EB6962EA7DE/tju/data/UAV/VOCdevkit2007/VOC2007/JPEGImages"
    xmlpath = "/media/lirun/04962EB6962EA7DE/tju/data/UAV/VOCdevkit2007/VOC2007/XML"

    name_class = {'0': 'ignored', '1': 'pedestrian', '2': 'people', '3': 'bicycle', '4': 'car', '5': 'van', '6': 'truck',
              '7': 'tricycle', '8': 'van-like-tricycle', '9': 'bus', '10': 'motor', '11': 'others'}

    txtfiles = os.listdir(annpath)
    num = 0
    # numignore = 0
    # txtfiles = ['9999955_00000_d_0000072.txt']
    for txtfile in txtfiles:
        num += 1
        print(num)
        txt = os.path.join(annpath, txtfile)
        with open(txt, 'r') as f:
            lines = f.readlines()

    #     for line in lines:
    #         splitted_line = line.strip().lower().split(',')
    #         cls = name_class[splitted_line[5]]
    #         if cls == '0' or cls == '11':
    #             numignore += 1
    #         num += 1

        img = cv2.imread(os.path.join(imagepath, txtfile.replace('txt', 'jpg')))
        img_size = img.shape
        doc = generate_xml(txtfile.replace('txt', 'jpg'), lines, img_size, name_class)

        xmlfile = os.path.join(xmlpath, txtfile.replace('txt', 'xml'))
        # print doc.toprettyxml(indent=' ')
        with open(xmlfile, 'w') as f:
            f.write(doc.toprettyxml(indent=' '))
