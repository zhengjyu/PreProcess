import os


def image_rename(file_path):
    files = os.listdir(file_path)
    image_num = 1
    for file_name in files:
        new_file_name = "img%07d.jpg" % image_num
        image_num += 1
        file = os.path.join(file_path, file_name)
        new_file = os.path.join(file_path, new_file_name)
        os.rename(file, new_file)


def image_motify_name(file_path):
    files = os.listdir(file_path)
    for file in files:
        file_name = file.split('.')
        image_num = int(file_name[0])
        new_file_name = "img%07d.jpg" % image_num
        old_file = os.path.join(file_path, file)
        new_file = os.path.join(file_path, new_file_name)
        os.rename(old_file, new_file)


def xml_motify_name(file_path):
    files = os.listdir(file_path)
    for file in files:
        file_name = file.split('.')
        image_num = int(file_name[0])
        new_file_name = "img%07d.xml" % image_num
        old_file = os.path.join(file_path, file)
        new_file = os.path.join(file_path, new_file_name)
        os.rename(old_file, new_file)


def motify_etc(file_path):
    files = os.listdir(file_path)
    for file in files:
        file_name = file.split('.')
        image_num = file_name[0]
        new_file_name = "%s.xml" % image_num
        # print(new_file_name)
        old_file = os.path.join(file_path, file)
        new_file = os.path.join(file_path, new_file_name)
        os.rename(old_file, new_file)


def rename_visdrone(path):
    sequences = os.listdir(path)
    for sequence in sequences:
        old_name = os.path.join(path, sequence)
        # uav0000011_00345_s
        name = "uav%07d_%05d_s" % ((int(sequence) + 370), 1)
        new_name = os.path.join(path, name)
        os.rename(old_name, new_name)
        print(old_name, new_name)


if __name__ == '__main__':
    file_path = 'E:/visdrone/2019/data/visdrone2019_sot/sequences'
    xml_path = 'E:/visdrone/2019/data/visdrone2019_sot/annotations_xml'
    rename_visdrone(xml_path)
    # names = os.listdir(xml_path)
    # for name in names:
    #     print(name)
        # image_rename(os.path.join(file_path, name))
        # image_motify_name(os.path.join(file_path, name))
        # xml_motify_name(os.path.join(xml_path, name))
        # motify_etc(os.path.join(xml_path, name))
    # path = "E:/visdrone/2019/data/visdrone2019_sot/sequences/26"
    # image_rename(path)