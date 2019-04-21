# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 21:29:38 2018

@author: Administrator
"""

from PIL import Image, ImageDraw
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import sys
import cv2, os
import numpy as np
from matplotlib import pyplot as plt
im_path = "/media/lirun/04962EB6962EA7DE/tju/data/UAV/VOCdevkit2007/VOC2007/JPEGImages"
xml_path = "/media/lirun/04962EB6962EA7DE/tju/data/UAV/VOCdevkit2007/VOC2007/Annotations"
index = "/media/lirun/04962EB6962EA7DE/tju/data/UAV/VOCdevkit2007/VOC2007/ImageSets/Main/test.txt"
with open(index, 'r') as f:
    lines = f.readlines()

for line in lines:
    im_file = os.path.join(im_path, line.replace("\n", ".jpg"))
    im = cv2.imread(im_file)

    fig = plt.figure()

    f=os.path.join(xml_path, line.replace("\n", ".xml"))
    tree = ET.parse(f)
    root = tree.getroot()
    for object in root.findall("object"):
        name = object.find('name').text
        occlusion=object.find('pose').text
        truncated=object.find('truncated').text
        bndbox=object.find('bndbox')
        xmin = int(bndbox.find('xmin').text)
        ymin = int(bndbox.find('ymin').text)
        xmax = int(bndbox.find('xmax').text)
        ymax = int(bndbox.find('ymax').text)
        cv2.rectangle(im, (xmin, ymin), (xmax, ymax), (255, 0, 0), 2)
        cv2.putText(im, name, (xmax, ymin), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255))
    im = cv2.resize(im, (1000, 500))
    cv2.imshow("1", im)
    cv2.waitKey(0)

    

