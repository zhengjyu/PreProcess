import os
from PreProcess.rename import rename


# data_path = 'G:/multi-drone-sot/data/MDOT_NV/data/three_drone/image'
data_path = 'E:/test'
videos_path = os.listdir(data_path)
for videos_name in videos_path:
    drones_name = os.listdir(os.path.join(data_path, videos_name))
    for drone_name in drones_name:
        path = os.path.join(data_path, videos_name, drone_name)
        print(path)
        rename(path, path)
