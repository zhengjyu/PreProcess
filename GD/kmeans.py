import os
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np

def load_data(annos_file):
    annos = pd.read_json(open(annos_file, "r"))
    bboxs = annos["bbox"].tolist()
    ratios = []
    for bbox in bboxs:
        width = bbox[2] - bbox[0]
        height = bbox[3] - bbox[1]
        ratios.append([width / height])
        # if height > width:
        #     ratios.append([height / width])
        # else:
        #     ratios.append([width / height])
    return ratios


def kmeans(data, n_clusters):
    clf = KMeans(n_clusters=n_clusters)
    s = clf.fit(data)
    cluster_centers_indices = clf.cluster_centers_
    labels = clf.labels_
    for i in range(n_clusters):
        print("{0}: {1} :{2}".format(i, cluster_centers_indices[i], len(labels[labels == i])))


if __name__ == '__main__':
    annos_file = "G:/aliyun/data/guangdong1_round1_train1_20190818/Annotations/anno_train.json"
    print("load data")
    ratios = load_data(annos_file)
    print("kmeans")
    kmeans(ratios, 3)

