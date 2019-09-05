import json
import cPickle as pickle
with open('/root/Detectron-Cascade-RCNN/output/cascade/test/coco_test/generalized_rcnn/detections.pkl') as fin:
    d = pickle.load(fin)
boxes = d['all_boxes']

NUM = 1000
CLASS_NUM = 21
id2image = {}
with open('/root/test.json') as fin:
    j = json.load(fin)['images']
for i in range(NUM):
    id2image[j[i]['id']] = j[i]['file_name']

result=[]
for img_id in range(NUM):
    image_name = id2image[img_id]
    for cls_id in range(1, CLASS_NUM):
        for i in range(boxes[cls_id][img_id].shape[0]):
            bbox = [float(boxes[cls_id][img_id][i][j]) for j in range(4)]
            score = float(boxes[cls_id][img_id][i][-1])
            result.append({'name': image_name,'category': cls_id,'bbox':bbox,'score': score})

with open('result.json', 'w') as fp:
     json.dump(result, fp, indent=4, separators=(',', ': '))