import os
import cv2
import shutil

def show_image(data_path, result_path):
    video_lists = os.listdir(data_path)
    num_uav = 1
    for video_list in video_lists:
        video_path = os.path.join(data_path, video_list, 'img')
        write_path = os.path.join(result_path, video_list)
        if not os.path.exists(write_path):
            os.makedirs(write_path)
        gt_path = os.path.join(data_path, video_list, 'groundtruth.txt')
        with open(gt_path, 'r') as fgt:
            groundtruths = fgt.readlines()
        images = os.listdir(video_path)
        num = 1
        for image in images:
            im = cv2.imread(os.path.join(video_path, image))
            groundtruth = groundtruths[num-1].split(',')
            xmin = round(float(groundtruth[0]))
            ymin = round(float(groundtruth[1]))
            xmax = round(float(groundtruth[0])) + round(float(groundtruth[2]))
            ymax = round(float(groundtruth[1])) + round(float(groundtruth[3].replace("\n", '')))
            cv2.rectangle(im, (xmin, ymin), (xmax, ymax), (0, 0, 255), 2)
            text = "uav-{0}:{1}".format(num_uav, num)
            cv2.putText(im, text, (50, 100), cv2.FONT_HERSHEY_TRIPLEX, 2, (0, 0, 255), 2, 4)
            cv2.imshow("image", im)
            cv2.imwrite(os.path.join(write_path, image), im)
            cv2.waitKey(1)
            num += 1
        num_uav += 1

def get_first(image_path, first_path, train_test='train', vis=True):
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
            img = os.path.join(video, 'img', '000001.jpg')
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

if __name__ == '__main__':
    data_path = "E:/multi-drone/data/MDOT/test/md046"
    result_path = "E:/multi-drone/data/MDOT_withgt/test/md046"
    show_image(data_path, result_path)
