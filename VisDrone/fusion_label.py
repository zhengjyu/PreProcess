import os
import xml.etree.ElementTree as ET
from PreProcess.get_data_xml import get_data_xml
from PreProcess.make_xml import make_xml


if __name__ == '__main__':
    file = "E:/visdrone/2019/data/single/single-30"
    xml_path = 'E:/visdrone/2019/data/single_label/single-30/Annotations'
    new_xml_path = 'E:/visdrone/2019/data/visdrone2019_sot/annotations_xml/30'
    tree1 = ET.parse(file)
    root1 = tree1.getroot()
    # print(root1[0][0][0].text)
    xmls = os.listdir(xml_path)
    for i in range(len(xmls)):
        xml = xmls[i]
        xml_config, objects = get_data_xml(os.path.join(xml_path, xml))
        if objects[0]['name'] == 'person':
            objects[0]['name'] = root1[0][i][0].text
        else:
            print(xml)
            print(i+1)

        if not os.path.exists(new_xml_path):
            os.makedirs(new_xml_path)
        new_file_name = "img%07d.xml" % (i+1)
        xml_name = os.path.join(new_xml_path, new_file_name)
        make_xml(xml_name, xml_config, objects)
