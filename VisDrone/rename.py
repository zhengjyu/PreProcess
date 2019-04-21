import os


def rename(file_path):
    files = os.listdir(file_path)
    image_num = 1
    for file_name in files:
        new_file_name = "%08d.jpg" % image_num
        image_num += 1
        file = os.path.join(file_path, file_name)
        new_file = os.path.join(file_path, new_file_name)
        os.rename(file, new_file)


if __name__ == '__main__':
    file_path = 'E:/multi-drone-mot/data/data'
    names = os.listdir(file_path)
    for name in names:
        rename(os.path.join(file_path, name))
