import xml.etree.ElementTree as ET


def get_data_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    xml_config = {}
    xml_config['folder'] = root.find("folder").text
    xml_config['filename'] = root.find("filename").text
    source = root.find('source')
    xml_config['database'] = source.find('database').text
    size = root.find('size')
    xml_config['width'] = size.find('width').text
    xml_config['height'] = size.find('height').text
    xml_config['depth'] = size.find('depth').text
    xml_config['segmented'] = root.find("segmented").text
    objects = []
    objs = root.findall('object')
    for obj in objs:
        object = {}
        object['name'] = obj.find('name').text
        object['pose'] = obj.find('pose').text
        object['truncated'] = obj.find('truncated').text
        object['difficult'] = obj.find('difficult').text
        bndbox = obj.find('bndbox')
        object['xmin'] = bndbox.find('xmin').text
        object['ymin'] = bndbox.find('ymin').text
        object['xmax'] = bndbox.find('xmax').text
        object['ymax'] = bndbox.find('ymax').text
        objects.append(object)
    #     print(object)
    # print(xml_config)
    return xml_config, objects

if __name__ == '__main__':
    xml_file = "E:/visdrone/2019/data/VisDrone2018-SOT-test-challenge/xml/uav0000191_00000_s/img0000001.xml"
    get_data_xml(xml_file)
