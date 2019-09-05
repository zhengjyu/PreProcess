import os
import cv2
from PreProcess.make_xml import make_xml


if __name__ == '__main__':
    name = {'1': 'pedestrian',
            '2': "people",
            '3': "bicycle",
            '4': "car",
            '5': "van",
            '6': "truck",
            '7': "tricycle",
            '8': "awning-tricycle",
            '9': "bus",
            '10': "motor"}
    data_path = "E:/data/mot/VisDrone2018-MOT-test-dev"
    sequences_path = os.path.join(data_path, 'sequences')
    anno_path = os.path.join(data_path, 'annotations')
    sequences = os.listdir(sequences_path)
    for sequence in sequences:
        images = os.listdir(os.path.join(sequences_path, sequence))
        xml_path = os.path.join(data_path, 'annotations_xml', sequence)
        if not os.path.exists(xml_path):
            os.makedirs(xml_path)
        for image in images:
            image_name = (image.split("."))[0]
            txt = os.path.join(anno_path, sequence, image_name + '.txt')
            file_name = os.path.join(sequences_path, sequence, image_name + '.jpg')
            xml_config = {}
            xml_config['folder'] = sequence
            xml_config['filename'] = sequence + "_" + image
            xml_config['database'] = 'visdrone2018_mot'
            xml_config['segmented'] = '0'
            im = cv2.imread(file_name)
            im_sz = im.shape
            xml_config['width'] = str(im_sz[1])
            xml_config['height'] = str(im_sz[0])
            xml_config['depth'] = str(im_sz[2])

            with open(txt, 'r') as f:
                lines = f.readlines()
            objects = []
            for i in range(len(lines)):
                line = lines[i].split(',')
                object = {}
                object['name'] = name[line[7]]
                object['pose'] = 'top'
                object['truncated'] = '0'
                object['difficult'] = '0'
                object['xmin'] = line[2]
                object['ymin'] = line[3]
                object['xmax'] = str(int(line[2]) + int(line[4]))
                object['ymax'] = str(int(line[3]) + int(line[5]))
                objects.append(object)
            xml_name = os.path.join(xml_path, image_name + '.xml')
            make_xml(xml_name, xml_config, objects)

