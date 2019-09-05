import os
import cv2
import shutil
import xml.etree.ElementTree as ET


def getFrame(image_path, videoname):
    video = cv2.VideoCapture(videoname)
    frame_num = 1
    image_num = 1
    while(video.isOpened()):
        ret, frame = video.read()
        if ret:
            frame_num += 1
            if frame_num % 2 != 0:
                # print frame_num
                continue
            frame = cv2.resize(frame, (1280, 720))
            # cv2.imshow("frame", frame)
            frame_name = os.path.join(image_path, "%08d.jpg" % image_num)
            # print frame_name
            cv2.imwrite(frame_name, frame)
            image_num += 1
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     break
        else:
            break
    video.release()
    pass


def getFrame_func():
    for path_num in range(1, 63):
        path_name = "md%03d" % path_num
        ext_num = [["MOV", "MP4"], ["MOV", "MOV"]]
        for video_num in range(1, 3):
            image_path = "E:/first/data/SOT/{0}/{1}".format(path_name, video_num)
            if path_num >= 18 and path_num <= 36 or path_num >= 50:
                ext = ext_num[1]
            else:
                ext = ext_num[0]
            video_name = os.path.join("E:/first/data/A/{0}/{1}-{2}.{3}".format(path_name, path_num, video_num, ext[video_num - 1]))
            print(image_path)
            print(video_name)
            os.makedirs(image_path)
            getFrame(image_path, video_name)


def change_name(file_path):
    files = os.listdir(file_path)
    image_num = 1
    for file_name in files:
        new_file_name = "%06d.jpg" % image_num
        image_num += 1

        file = os.path.join(file_path, file_name)
        new_file = os.path.join(file_path, new_file_name)
        os.rename(file, new_file)
    pass


def max_file(file_path):
    num = 0
    max_num = 0
    file_dirs = os.listdir(file_path)
    for file_dir in file_dirs:
        file_video1 = os.path.join(file_path, file_dir, "1")
        file_video2 = os.path.join(file_path, file_dir, "2")
        num1 = len(os.listdir(file_video1))
        num2 = len(os.listdir(file_video2))
        num = num + num1 + num2
        max_num = max(num1, num2, max_num)
    print(max_num, num)


def task_make():
    file_path = "E:/first/data/task"
    image_path = "E:/first/data/SOT"
    record_txt = "E:/first/data/record.txt"
    # f = open(record_txt, "r")
    # records = f.readlines()
    for path_num in range(1, 63):
        path_name = "md%03d" % path_num
        path = os.path.join(file_path, path_name)
        # os.makedirs(path)
        first = os.path.join(image_path, path_name, "1.jpg")
        second = os.path.join(image_path, path_name, "2.jpg")
        first_new = os.path.join(path, "1.jpg")
        second_new = os.path.join(path, "2.jpg")
        shutil.copy(first, first_new)
        shutil.copy(second, second_new)

        # record_num = 2 * path_num - 1
        # file_new = os.path.join(path, "{0}.txt".format(path_name))
        # w = open(file_new, "w")
        # w.write(records[record_num - 1])
        # w.write(records[record_num])
        # w.close()
        # print records[record_num]
        # print file_new
    # f.close()


def make_dir(file_path):
    for path_num in range(1, 63):
        path_name = "md%03d" % path_num
        path1 = os.path.join(file_path, path_name, '1')
        path2 = os.path.join(file_path, path_name, '2')
        os.makedirs(path1)
        os.makedirs(path2)


def xml_equal_img(img_path, xml_path, tmp_path):
    images = os.listdir(img_path)
    num = 0
    numt = 0
    for image in images:
        for video_num in range(1, 3):
            video_p = os.path.join(img_path, image, str(video_num))
            xml_p = os.path.join(xml_path, image, str(video_num))
            tmp_p = os.path.join(tmp_path, image, str(video_num))
            if not tmp_p:
                os.makedirs(tmp_p)
            video_files = os.listdir(video_p)
            xml_files = os.listdir(xml_p)
            for xml_file in xml_files:
                xml_name = os.path.join(xml_p, xml_file)
                video_name = xml_file.replace('xml', 'jpg')
                tmp_name = os.path.join(tmp_p, xml_file)
                if video_name not in video_files:
                    shutil.move(xml_name, tmp_name)
                    num += 1
                    print(xml_name, video_name)
                else:
                    numt += 1
    print(num, numt)


def check_data(img_path, xml_path, tmp_path):
    images = os.listdir(img_path)
    for image in images:
        example1 = os.path.join(img_path, image, '1.jpg')
        example2 = os.path.join(img_path, image, '2.jpg')
        video_1 = os.path.join(img_path, image, '1')
        video_2 = os.path.join(img_path, image, '2')
        tmp_1 = os.path.join(tmp_path, image, '1.jpg')
        tmp_2 = os.path.join(tmp_path, image, '2.jpg')
        xml_1 = os.path.join(xml_path, image, '1')
        xml_2 = os.path.join(xml_path, image, '2')
        if os.path.exists(example1):
            shutil.move(example1, tmp_1)
        if os.path.exists(example2):
            shutil.move(example2, tmp_2)
        if len(os.listdir(video_1)) != len(os.listdir(video_2)):
            print(video_1, video_2)
        if len(os.listdir(xml_1)) != len(os.listdir(xml_2)):
            print(xml_1, xml_2)


def move_dir(img_path):
    images = os.listdir(img_path)
    for image in images:
        for video_num in range(1, 3):
            video_p = os.path.join(img_path, image, str(video_num))
            video_new = os.path.join(img_path, image, "{0}-{1}".format(image, video_num))
            video_pnew = os.path.join(video_new, "img")
            if not os.path.exists(video_new):
                os.makedirs(video_new)
            shutil.move(video_p, video_pnew)


def obj2tracking(object_path, tracking_path):
    set_name = set()
    objects = os.listdir(object_path)
    for object in objects:
        for video_num in range(1, 3):
            txt_path = os.path.join(tracking_path, object, "{0}-{1}".format(object, video_num))
            groundtruth_t = os.path.join(txt_path, "groundtruth.txt")
            out_of_view = os.path.join(txt_path, "out_of_view.txt")
            occlusion_t = os.path.join(txt_path, "occlusion.txt")
            if os.path.exists(groundtruth_t):
                os.remove(groundtruth_t)
            if os.path.exists(out_of_view):
                os.remove(out_of_view)
            if os.path.exists(occlusion_t):
                os.remove(occlusion_t)
            fg = open(groundtruth_t, 'w+')
            fout = open(out_of_view, 'w+')
            foc = open(occlusion_t, 'w+')
            xml_path = os.path.join(object_path, object, str(video_num))
            xml_files = os.listdir(xml_path)
            for xml_file in xml_files:
                xml = os.path.join(xml_path, xml_file)
                outside = 0
                occlusion = 0
                tree = ET.parse(xml)
                root = tree.getroot()
                obj = root.find("object")
                name = obj.find('name').text
                set_name.add(name)
                if name == 'Person' or name == 'person' or name == 'Persona':
                    # obj.find('name').text = 'Person'
                    bndbox = obj.find('bndbox')
                    xmin = int(bndbox.find('xmin').text)
                    ymin = int(bndbox.find('ymin').text)
                    xmax = int(bndbox.find('xmax').text)
                    ymax = int(bndbox.find('ymax').text)
                elif name == 'Outside':
                    xmin, ymin, xmax, ymax = 1, 1, 1, 1
                    outside = 1
                else:
                    bndbox = obj.find('bndbox')
                    xmin = int(bndbox.find('xmin').text)
                    ymin = int(bndbox.find('ymin').text)
                    xmax = int(bndbox.find('xmax').text)
                    ymax = int(bndbox.find('ymax').text)
                    occlusion = 1
                groundtruth = "{0},{1},{2},{3}\n".format(xmin, ymin, xmax - xmin, ymax - ymin)
                outofview = "{0}\n".format(outside)
                occlusion_txt = "{0}\n".format(occlusion)
                fg.write(groundtruth)
                fout.write(outofview)
                foc.write(occlusion_txt)
            fg.close()
            fout.close()
            foc.close()
    print(set_name)
    pass


def rename(img_path, xml_path):
    images = os.listdir(img_path)
    for image in images:
        for video_num in range(1, 3):
            video_p = os.path.join(img_path, image, "{0}-{1}".format(image, video_num), 'img')
            xml_p = os.path.join(xml_path, image, str(video_num))
            videos = os.listdir(video_p)
            num = 1
            for video in videos:
                video_file = os.path.join(video_p, video)
                xml_file = os.path.join(xml_p, video.replace('jpg', 'xml'))
                video_new = os.path.join(video_p, "%08d.jpg" % num)
                xml_new = os.path.join(xml_p, "%08d.xml" % num)
                num += 1
                os.rename(video_file, video_new)
                os.rename(xml_file, xml_new)
                print(video_file, video_new)
                print(xml_file, xml_new)
    pass


# isLF = true win2unix  false  unixtowin
def to_lf(path, isLF, encoding='utf-8'):
    newline = '\n' if isLF else '\r\n'
    with open(path, newline=None, encoding=encoding) as infile:
        str = infile.readlines()
        with open(path, 'w', newline=newline, encoding=encoding) as outfile:
            outfile.writelines(str)


def change_encode(path):
    images = os.listdir(path)
    for image in images:
        for video_num in range(1, 3):
            video_p = os.path.join(path, image, "{0}-{1}".format(image, video_num))
            files = os.listdir(video_p)
            for file in files:
                file_name = os.path.join(video_p, file)
                if os.path.isfile(file_name):
                    to_lf(file_name, True)
    pass


def show_image(image_path, showgt):
    video_twos = os.listdir(image_path)
    for video_two in video_twos:
        for video_num in range(1, 3):
            video = os.path.join(image_path, video_two, "{0}-{1}".format(video_two, video_num))
            print("1: ", video)
            gt = os.path.join(video, 'groundtruth.txt')
            with open(gt, 'r') as fr:
                groundtruths = fr.readlines()
            occ = os.path.join(video, 'occlusion.txt')
            with open(occ, 'r') as focc:
                occlusions = focc.readlines()
            out = os.path.join(video, 'out_of_view.txt')
            with open(out, 'r') as fout:
                outsides = fout.readlines()
            images = os.listdir(os.path.join(video, 'img'))
            num = 0
            for image in images:
                # print(os.path.join(video, 'img', image))
                im = cv2.imread(os.path.join(video, 'img', image))
                groundtruth = groundtruths[num].split(',')
                xmin = int(groundtruth[0])
                ymin = int(groundtruth[1])
                xmax = int(groundtruth[0]) + int(groundtruth[2])
                ymax = int(groundtruth[1]) + int(groundtruth[3].replace("\n", ''))
                # print(xmin, ymin, xmax, ymax)
                cv2.rectangle(im, (xmin, ymin), (xmax, ymax), (255, 0, 0), 2)
                cv2.putText(im, occlusions[num].replace("\n", ""), (30, 50), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255))
                cv2.putText(im, outsides[num].replace("\n", ""), (1, 50), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0))
                cv2.imshow("image", im)
                cv2.waitKey(10)
                num += 1
    pass


def make_test(image_path):
    video_list = os.listdir(image_path)
    train = os.path.join(image_path, '..', 'train.txt')
    test = os.path.join(image_path, '..', 'test.txt')
    with open(train, 'r') as ftr:
        train_lines = ftr.readlines()
    fte = open(test, 'w+')
    for video in video_list:
        if (video + '\n') not in train_lines:
            fte.write(video + '\n')
            print(video)
    fte.close()
    pass



def get_first_txt(image_path, first_path, train_test='train', vis=False):
    obj_path = os.path.join(first_path, train_test)
    if not os.path.exists(obj_path):
        os.makedirs(obj_path)
    txt = os.path.join(image_path, train_test + '.txt')
    with open(txt, 'r') as ft:
        lines = ft.readlines()
    for line in lines:
        videos_path = os.path.join(image_path, 'data', line.replace('\n', ''))
        for video_num in range(1, 3):
            video = os.path.join(videos_path, "{0}-{1}".format(line.replace('\n', ''), video_num))
            img = os.path.join(video, 'img', '00000001.jpg')
            img_new = os.path.join(obj_path, "{0}-{1}.jpg".format(line.replace('\n', ''), video_num))
            if vis:
                gt = os.path.join(video, 'groundtruth.txt')
                with open(gt, 'r') as fr:
                    groundtruths = fr.readlines()
                im = cv2.imread(img)
                groundtruth = groundtruths[0].split(',')
                xmin = int(groundtruth[0])
                ymin = int(groundtruth[1])
                xmax = int(groundtruth[0]) + int(groundtruth[2])
                ymax = int(groundtruth[1]) + int(groundtruth[3].replace("\n", ''))
                cv2.rectangle(im, (xmin, ymin), (xmax, ymax), (0, 0, 255), 2)
                cv2.imwrite(img_new, im)
            else:
                shutil.copy(img, img_new)


def make_anno(data_path, anno_path):
    datas = os.listdir(data_path)
    for data in datas:
        for i in range(1, 3):
            groundtruth = os.path.join(data_path, data, "{0}-{1}".format(data, i), "occlusion.txt")
            groundtruth_object_path = os.path.join(anno_path, "occlusion", data)
            if not os.path.exists(groundtruth_object_path):
                os.makedirs(groundtruth_object_path)
            groundtruth_object = os.path.join(groundtruth_object_path, "{0}-{1}.txt".format(data, i))
            shutil.copy(groundtruth, groundtruth_object)
            print(groundtruth, groundtruth_object)

    pass


def get_anno(data_path, obj_path):
    txt_name = ['groundtruth.txt', 'occlusion.txt', 'out_of_view.txt']
    videos = os.listdir(data_path)
    for video in videos:
        video_names = os.listdir(os.path.join(data_path, video))
        for video_name in video_names:
            for i in range(3):
                new_path = os.path.join(obj_path, video, video_name)
                if not os.path.exists(new_path):
                    os.makedirs(new_path)
                file_old = os.path.join(data_path, video, video_name, txt_name[i])
                file_new = os.path.join(new_path, txt_name[i])
                shutil.copy(file_old, file_new)


def get_first(videos_path, store_path, vis=False):
    videos = os.listdir(videos_path)
    for video in videos[46:47]:
        print(video)
        obj_path = os.path.join(store_path, video)
        if not os.path.exists(obj_path):
            os.makedirs(obj_path)
        video_nums = os.listdir(os.path.join(videos_path, video))
        for video_num in video_nums:
            img = os.path.join(videos_path, video, video_num, '00000001.jpg')
            img_new = os.path.join(obj_path, "{0}.jpg".format(video_num))
            if vis:
                gt = os.path.join(video, 'groundtruth.txt')
                with open(gt, 'r') as fr:
                    groundtruths = fr.readlines()
                im = cv2.imread(img)
                groundtruth = groundtruths[0].split(',')
                xmin = int(groundtruth[0])
                ymin = int(groundtruth[1])
                xmax = int(groundtruth[0]) + int(groundtruth[2])
                ymax = int(groundtruth[1]) + int(groundtruth[3].replace("\n", ''))
                cv2.rectangle(im, (xmin, ymin), (xmax, ymax), (0, 0, 255), 2)
                cv2.imwrite(img_new, im)
            else:
                shutil.copy(img, img_new)


def make_data(images_path, videos_path):
    videos = os.listdir(videos_path)
    for video in videos[46:47]:
        for i in range(1, 4):
            video_name = os.path.join(videos_path, video, str(i) + '.MP4')
            image_path = os.path.join(images_path, video, video + '-' + str(i))
            os.makedirs(image_path)
            print(video_name, image_path)
            getFrame(image_path, video_name)
    pass

if __name__ == '__main__':
    # file_path = "E:/first/data/SOT/md032/2"
    # change_name(file_path)

    # images_path = "G:/multi-drone-sot/data/MDOT_NV/data/three_drone/image"
    # videos_path = "G:/multi-drone-sot/data/MDOT_NV/used/three"
    # make_data(images_path, videos_path)

    data_path = "G:/multi-drone-sot/data/MDOT_NV/data/three_drone/image"
    store_path = "G:/multi-drone-sot/data/MDOT_NV/data/three_drone/object"
    get_first(data_path, store_path)

    # image_path = "E:/first/data/SOT/md017/2"
    # video_name = "E:/first/data/md017/17-2.MP4"
    # os.makedirs(image_path)
    # getFrame(image_path, video_name)

    # file_path = "E:/first/data/SOT"
    # max_file(file_path)

    # file_path = "E:/first/data/task"
    # image_path = "E:/first/data/SOT"
    # make_dir(file_path)

    # img_path = "E:/first/data/MDOT"
    # xml_path = "E:/first/data/unused/xml"
    # tmp_path = "E:/first/data/SOT/tmp"
    # xml_equal_img(img_path, xml_path, tmp_path)
    # check_data(img_path, xml_path, tmp_path)
    # move_dir(img_path)
    # obj2tracking(xml_path, img_path)
    # change_encode(img_path)
    # rename(img_path, xml_path)

    # image_path = "E:/first/data/MDOT/data"
    # make_test(image_path)
    # show_image(image_path, True)

    # image_path = "E:/first/data/MDOT"
    # first_path = "E:/first/data/description"
    # get_first(image_path, first_path)

    # data_path = 'E:/first/data/MDOT/data'
    # anno_path = 'E:/first/result/MDOT_Evaluation_Toolkit/annos'
    # make_anno(data_path, anno_path)

    # data_path = 'E:/multi-drone/data/MDOT/data'
    # obj_path = 'E:/multi-drone/code/MDOT_toolkit/data'
    # get_anno(data_path, obj_path)
