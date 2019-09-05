import cv2
import os
import json

def save_coco_json(instance, save_path):
    import json
    with open(save_path, 'w') as fp:
        json.dump(instance, fp, indent=1, separators=(',', ': '))

def make_image(image_path):
    instance = {}
    images_name = os.listdir(image_path)
    images = []
    img_id = 0
    for img_name in images_name:
        image = {}
        img = cv2.imread(os.path.join(image_path, img_name))
        h, w, c = img.shape
        image['height'] = h
        image['width'] = w
        image['id'] = img_id
        image['file_name'] = img_name
        images.append(image)
        print(img_name)
        img_id = img_id + 1
    instance['images'] = images
    return instance

if __name__ == '__main__':
    image_path = "G:/aliyun/data/guangdong1_round1_testA_20190818"
    print(image_path)
    # instance = make_image(image_path)
    # save_coco_json(instance, "./instances_test.json")
