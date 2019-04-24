import os
import cv2
from PreProcess.make_xml import make_xml


if __name__ == '__main__':
    data_path = "E:/visdrone/2019/data/VisDrone2019-SOT-test-challenge"
    sequence = 'uav0000094_02070_s'
    txt = os.path.join(data_path, 'annotations', sequence + '.txt')
    image_path = os.path.join(data_path, 'sequences', sequence)
    with open(txt, 'r') as f:
        lines = f.readlines()
    for i in range(len(lines)):
        image_num = i + 1
        print(image_num)
        file_name = "img%07d" % image_num
        line = lines[i].split(',')
        xml_config = {}
        xml_config['folder'] = sequence
        xml_config['filename'] = file_name + '.jpg'
        xml_config['database'] = 'visdrone'
        xml_config['segmented'] = '0'
        image = cv2.imread(os.path.join(image_path, file_name + '.jpg'))
        im_sz = image.shape
        xml_config['width'] = str(im_sz[1])
        xml_config['height'] = str(im_sz[0])
        xml_config['depth'] = str(im_sz[2])

        objects = []
        object = {}
        object['name'] = 'person'
        object['pose'] = 'top'
        object['truncated'] = '0'
        object['difficult'] = '0'
        object['xmin'] = line[0]
        object['ymin'] = line[1]
        object['xmax'] = str(int(line[0]) + int(line[2]))
        object['ymax'] = str(int(line[1]) + int(line[3]))
        objects.append(object)
        xml_path = os.path.join(data_path, 'annotations_xml', sequence)
        if not os.path.exists(xml_path):
            os.makedirs(xml_path)
        xml_name = os.path.join(xml_path, file_name + '.xml')
        make_xml(xml_name, xml_config, objects)


