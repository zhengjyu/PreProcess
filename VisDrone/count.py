import os
import math

image_path = 'F:/visdrone/2019/data/VisDrone2019-SOT-test-challenge/sequences'
dirs = os.listdir(image_path)
num = 0
for dir in dirs:
    print(dir)
    images = os.listdir(os.path.join(image_path, dir))
    num = num + len(images)

print(num)


# anno_path = 'F:/visdrone/2019/data/VisDrone2019-SOT-test-challenge/annotations'
# dirs = os.listdir(anno_path)
# num = 0
# all_scale = 0.0
# for dir in dirs[:35]:
#     annos = os.path.join(anno_path, dir)
#     with open(annos, "r") as f:
#         gts = f.readlines()
#     for gt in gts:
#         rect = gt.strip('\n').split(',')
#         w = int(rect[2])
#         h = int(rect[3])
#         scale = math.sqrt(w * h)
#         all_scale = all_scale + scale
#         num = num + 1
#
# print(all_scale / num)

