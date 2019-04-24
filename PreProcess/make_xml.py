# -*- coding utf-8 -*-
import os
from xml.dom.minidom import Document
import cv2


# transform txt to xml
def generate_xml(xml_config, objects):
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
    append_xml_node_attr('folder', parent=annotation, text=xml_config['folder'])
    append_xml_node_attr('filename', parent=annotation, text=xml_config['filename'])
    source = append_xml_node_attr('source', parent=annotation)
    append_xml_node_attr('database', parent=source, text=xml_config['database'])
    size = append_xml_node_attr('size', annotation)
    append_xml_node_attr('width', size, xml_config['width'])
    append_xml_node_attr('height', size, xml_config['height'])
    append_xml_node_attr('depth', size, xml_config['depth'])
    append_xml_node_attr('segmented', parent=annotation, text=xml_config['segmented'])

    # create objects
    for object in objects:
        obj = append_xml_node_attr('object', parent=annotation)
        append_xml_node_attr('name', parent=obj, text=object['name'])
        append_xml_node_attr('pose', parent=obj, text=object['pose'])
        append_xml_node_attr('truncated', parent=obj, text=object['truncated'])
        append_xml_node_attr('difficult', parent=obj, text=object['difficult'])
        bb = append_xml_node_attr('bndbox', parent=obj)
        append_xml_node_attr('xmin', parent=bb, text=object['xmin'])
        append_xml_node_attr('ymin', parent=bb, text=object['ymin'])
        append_xml_node_attr('xmax', parent=bb, text=object['xmax'])
        append_xml_node_attr('ymax', parent=bb, text=object['ymax'])
    return doc


def make_xml(xml_name, xml_config, objects):
    doc = generate_xml(xml_config, objects)
    # print(doc.toprettyxml(indent=' '))
    with open(xml_name, 'w') as f:
        f.write(doc.toprettyxml(indent=' '))


