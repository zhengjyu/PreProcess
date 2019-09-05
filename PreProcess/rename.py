import os


def rename(old_path, new_path, str_num=8, start=1, ext='jpg'):
    data_num = start
    old_names = os.listdir(old_path)
    for old_name in old_names:
        old_file = os.path.join(old_path, old_name)
        new_name = "%0{0}d.{1}".format(str_num, ext) % int(data_num)
        new_file = os.path.join(new_path, new_name)
        os.rename(old_file, new_file)
        data_num += 1


if __name__ == '__main__':
    path = "E:/test"
    rename(path, path)
