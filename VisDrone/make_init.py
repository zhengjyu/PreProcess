import os


if __name__ == '__main__':
    data_path = 'E:/visdrone/2019/data/VisDrone2019-SOT-test-challenge'
    annotations_path = os.path.join(data_path, 'annotations')
    initialization_path = os.path.join(data_path, 'initialization')
    annotations = os.listdir(annotations_path)
    for annotation in annotations:
        anno_file = os.path.join(annotations_path, annotation)
        with open(anno_file, 'r') as f:
            annos = f.readlines()
        init = annos[0]
        init_file = os.path.join(initialization_path, annotation)
        with open(init_file, 'w', newline='\n') as w:
            w.writelines(init)
