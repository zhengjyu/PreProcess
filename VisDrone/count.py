import os


image_path = 'E:/visdrone/2019/data/visdrone2019_sot/sequences'
dirs = os.listdir(image_path)
num = 0
for dir in dirs:
    images = os.listdir(os.path.join(image_path, dir))
    num = num + len(images)

print(num)
