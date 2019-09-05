import os
import cv2

def show_image(data_path, result_path, dataset='test', showgt=False):
    with open(os.path.join(data_path, dataset+'.txt')) as f:
        video_lists = f.readlines()
    for video_list in video_lists:
        video_list = video_list.replace("\n", "")
        # print(video_list)
        for video_num in range(1, 3):
            print("{0}-{1}".format(video_list, video_num))
            video = os.path.join(data_path, 'data', video_list, "{0}-{1}".format(video_list, video_num))
            gt = os.path.join(result_path, video_list, "{0}-{1}_result.txt".format(video_list, video_num))
            with open(gt, 'r') as fgt:
                groundtruths = fgt.readlines()
            images = os.listdir(os.path.join(video, 'img'))
            num = 0
            size = (1280, 720)
            videoWriter = cv2.VideoWriter('{0}-{1}.avi'.format(video_list, video_num), cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'), 24, size)
            for image in images:
                # print(os.path.join(video, 'img', image))
                im = cv2.imread(os.path.join(video, 'img', image))
                groundtruth = groundtruths[num].split(',')
                xmin = round(float(groundtruth[0]))
                ymin = round(float(groundtruth[1]))
                xmax = round(float(groundtruth[0])) + round(float(groundtruth[2]))
                ymax = round(float(groundtruth[1])) + round(float(groundtruth[3].replace("\n", '')))
                # print(xmin, ymin, xmax, ymax)
                cv2.rectangle(im, (xmin, ymin), (xmax, ymax), (255, 0, 0), 2)
                cv2.imshow("image", im)
                videoWriter.write(im)
                cv2.waitKey(1)
                num += 1
            cv2.waitKey(0)


