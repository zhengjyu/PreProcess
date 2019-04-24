import os
from PreProcess.get_data_xml import get_data_xml


if __name__ == '__main__':
    data_path = 'E:/visdrone/2019/data/visdrone2019_sot/annotations_xml'
    new_path = 'E:/visdrone/2019/data/visdrone2019_sot/annotations'
    xml_paths = os.listdir(data_path)
    for xml_path in xml_paths:
        lines = []
        xmls = os.listdir(os.path.join(data_path, xml_path))
        for xml in xmls:
            xml_config, objects = get_data_xml(os.path.join(data_path, xml_path, xml))
            print(os.path.join(data_path, xml_path, xml))
            assert len(objects) == 1
            object = objects[0]
            xmin = int(object['xmin'])
            ymin = int(object['ymin'])
            xmax = int(object['xmax'])
            ymax = int(object['ymax'])
            w = xmax - xmin
            h = ymax - ymin
            line = "%d,%d,%d,%d\n" % (xmin, ymin, w, h)
            lines.append(line)
        new_file = os.path.join(new_path, xml_path + '.txt')
        with open(new_file, 'w+', newline='\n') as w:
            w.writelines(lines)

