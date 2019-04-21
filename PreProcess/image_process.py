# -*- coding:utf-8 -*
import cv2
import numpy as np


# Flip
def ImageFlip(src, select):
    """
    图像翻转
    :param src
    :param select 1:Horizontally 2:Vertically else:all
    :return dst
    """
    #  Flipped Horizontally
    if select==1:
        dst = cv2.flip(src, 1)
    #  Flipped Vertically
    elif select==2:
        dst = cv2.flip(src, 0)
    #  Flipped Vertivally Horizontally
    else:
        dst = cv2.flip(src, -1)
    return dst


# Rotate
def ImageRotate(src, angle):
    """
    图像旋转
    :param src
    :param angle
    :return dst
    """
    h, w = src.shape[:2]
    center = (w / 2, h / 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)

    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))
    M[0, 2] += (nW / 2) - center[0]
    M[1, 2] += (nH / 2) - center[1]
    dst = cv2.warpAffine(src, M, (nW, nH))

    return dst


# enhance
def ImageEnhance(src, rate):
    """
    图像增强
    :param src
    :param rate
    :return dst
    """
    dst = np.power(src / 255.0, rate)
    max = np.max(dst)
    dst = dst / max * 255.0
    return dst


# shape
def ImageShape(src, select, rate):
    """
    上下左右形变
    :param src
    :param select: 1:down 2:up 3:left else:right
    :param rate
    :return dst
    """
    h, w = src.shape[:2]
    srcpoint = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]])
    #down
    if select == 1:
        dstpoint = np.float32(
            [[0, 0], [w * rate, h - 1], [w - 1 - w * rate, h - 1],
             [w - 1, 0]])
    #up
    elif select == 2:
        dstpoint = np.float32([[w * rate, 0], [0, h - 1], [w - 1, h - 1],
                                 [w - 1 - w * rate, 0]])
    #left
    elif select == 3:
        dstpoint = np.float32(
            [[0, h * rate], [0, h - 1 - h * rate], [w - 1, h - 1],
             [w - 1, 0]])
    #right
    else:
        dstpoint = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1 - h * rate],
                                    [w - 1, h * rate]])
    warp_mat = cv2.getPerspectiveTransform(srcpoint, dstpoint)
    # dst = cv2.warpPerspective(src, warp_mat, (w, h), borderMode=cv2.BORDER_REPLICATE)
    dst = cv2.warpPerspective(src, warp_mat, (w, h))
    return dst


# resize
def ImageResize(src, long):
    """
     调整大小到长边为long
     :param src
     :param long
     :return dst
     """
    h, w = src.shape[:2]
    if w > h:
        scale = long / float(w)
        dst = cv2.resize(src,(long, np.int(h*scale)),interpolation=cv2.INTER_AREA);
    else:
        scale = long / float(h)
        dst = cv2.resize(src,(np.int(w*scale),long),interpolation=cv2.INTER_AREA);
    return dst


# crop
def ImageCrop(src):
    """
     图像裁剪
     :param src
     :return dst
     """
    h, w = src.shape[:2]
    hl = np.random.randint(0, h - 1)
    while hl > h - 3:
        hl = np.random.randint(0, h - 1)
    hr = np.random.randint(hl + 1, h - 1)
    wl = np.random.randint(0, w - 1)
    while wl > w - 3:
        wl = np.random.randint(0, w - 1)
    wr = np.random.randint(wl + 1, w - 1)
    dst = src[hl:hr, wl:wr, :]
    return dst


# Black
def ImageBlack(src):
    """
     图像涂黑
     :param src
     :return dst
     """
    dst = src.copy()
    h, w = src.shape[:2]
    hl = np.random.randint(0, h - 1)
    while hl > h - 3:
        hl = np.random.randint(0, h - 1)
    hr = np.random.randint(hl + 1, h - 1)
    wl = np.random.randint(0, w - 1)
    while wl > w - 3:
        wl = np.random.randint(0, w - 1)
    wr = np.random.randint(wl + 1, w - 1)
    # for i in range(wl, wr):
    #     for j in range(hl - 1, hr):
    for i in range(19, 157):
        for j in range(217, 358):
            color = (0, 0, 0)
            dst[j, i] = color
    return dst


if __name__ == '__main__':
    image = cv2.imread("src.jpg")
    cv2.imshow("Original", image)
    # dst = ImageFlip(image, 3)
    # dst = ImageRotate(image, 275)
    # dst = ImageEnhance(image, 0.5)
    # dst = ImageShape(image, 4, 0.1)
    dst = ImageCrop(image)
