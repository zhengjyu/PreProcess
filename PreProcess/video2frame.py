import os
import cv2


# transform video to frame
def get_frame(video_name, video_path, image_path, video_ext='mov', image_ext='jpg', interval=1):
    if not os.path.exists(os.path.join(image_path, video_name)):
        os.makedirs(os.path.join(image_path, video_name))
    video = cv2.VideoCapture(os.path.join(video_path, '%s.%s' % (video_name, video_ext)))
    frame_num = 0
    while(video.isOpened()):
        ret, frame = video.read()
        if ret:
            frame_num = frame_num + 1
            print(frame_num)
            if frame_num % interval != 0:
                continue
            frame_name = os.path.join(image_path, video_name, '%08d.%s' % (frame_num, image_ext))
            frame = cv2.resize(frame, (1080, 720))
            cv2.imshow('image', frame)
            cv2.waitKey(3)
            cv2.imwrite(frame_name, frame)
        else:
            break
    video.release()
    print('********************end********************')


if __name__ == '__main__':
    video_name = '10'
    video_path = 'E:/visdrone/2019/data/visdrone2019_sot_video'
    image_path = 'E:/visdrone/2019/data/visdrone2019_sot'
    get_frame(video_name, video_path, image_path, video_ext='MOV')
