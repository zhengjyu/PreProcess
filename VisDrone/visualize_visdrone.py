import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
import glob
import shutil as sh

root = '/home/mawenya/code/data/visdrone_fig/'
img = os.path.join(root, 'images')
ann = os.path.join(root, 'annotations')
dpnet = os.path.join(root, 'dpnet')
res_path = '/home/mawenya/code/visdrone_fig/fig/'


def getrec(ann):
    result = np.loadtxt(ann, delimiter=',')
    # print(result)
    rec = result[:, :4]
    #  print(rec)
    return rec


def getcat(ann):
    ann_dirs = glob.glob(ann + '/*.txt')
    flag = np.zeros(11)
    for ann in ann_dirs:
        for i in range(11):
            if flag[i] > 3:
                continue
            res = np.loadtxt(ann, delimiter=',', dtype=int)
            print(flag[i])
            if len(res.shape) == 1:
                continue
            if (res[:, 5] == int(i + 1)).any() and (res[:, 5] != 0).all():
                # sh.copy(ann.replace('annotations','images').replace('.txt','.jpg'),'./result/'+str(i)+'.jpg')
                img_dir = ann.replace('annotations', 'images').replace('.txt', '.jpg')
                res_dir = ann.replace('annotations', 'dpnet')
                save_dir = './result/' + str(i) + '-' + str(int(flag[i])) + '.jpg'
                showrec(img_dir, ann, res_dir, save_dir)
                flag[i] += 1
                break


def showrec(img_dir, ann_dir, res_dir, save_dir):
    recs = getrec(ann_dir)
    img = cv2.imread(img_dir)
    recs_res = getrec(res_dir)
    for rec in recs:
        #   print((float(rec[0]),float(rec[1])))
        if int(rec[2]) * int(rec[3]) < 1000:
            img = cv2.rectangle(img, (int(rec[0]), int(rec[1])), (int(rec[0] + rec[2]), int(rec[1] + rec[3])),
                                (0, 0, 255), 4)
        else:
            img = cv2.rectangle(img, (int(rec[0]), int(rec[1])), (int(rec[0] + rec[2]), int(rec[1] + rec[3])),
                                (0, 0, 255), 7)
    for rec in recs_res:
        img = cv2.rectangle(img, (int(rec[0]), int(rec[1])), (int(rec[0] + rec[2]), int(rec[1] + rec[3])), (0, 255, 0),
                            2)
    #     cv2.imshow('vis',img)
    # cv2.waitKey(10000)
    #      print(img_dir)
    cv2.imwrite(save_dir, img)


def vis(img, ann):
    img_dirs = glob.glob(img + '/*.jpg')
    ann_dirs = glob.glob(ann + '/*.txt')
    # print(ann_dirs)
    # print(img_dirs)
    for i in range(len(img_dirs)):
        # /home/mawenya/code/data/visdrone_fig/images/9999936_00000_d_0000009.jpg
        img_dir = img_dirs[i]
        prefix = img_dir.split('/')[-1].split('.')[0]
        ann_dir = os.path.join(ann, prefix + '.txt')
        result = os.path.join(dpnet, prefix + '.txt')
        '''
        for dirs in ann_dirs:
         #   print(img_dir.split('/')[-1].split('.')[0])
            if img_dir.split('/')[-1].split('.')[0] == dirs.split('/')[-1].split('.')[0]:
               ann_dir = dirs
               break
        '''
        print(img_dir, ': ', ann_dir)
        if img_dir.split('/')[-1].split('.')[0] != ann_dir.split('/')[-1].split('.')[0]:
            break
            print('Error: img dont match anntation file', img_dir)
        recs = getrec(ann_dir)
        recs_res = getrec(result)
        img = cv2.imread(img_dir)
        for rec in recs:
            #   print((float(rec[0]),float(rec[1])))
            img = cv2.rectangle(img, (int(rec[0]), int(rec[1])), (int(rec[0] + rec[2]), int(rec[1] + rec[3])),
                                (0, 0, 255), 8)
        for rec in recs_res:
            img = cv2.rectangle(img, (int(rec[0]), int(rec[1])), (int(rec[0] + rec[2]), int(rec[1] + rec[3])),
                                (0, 255, 0), 2)
        cv2.imshow('vis', img)
        # cv2.waitKey(10000)
        print(img_dir)
        cv2.imwrite('./result/' + prefix + '.jpg', img)


#    cv2.destroyAllWindows()
def combine(res_path):
    split = np.zeros([765, 5, 3])
    split[:, :, 0] = 255
    split[:, :, 1] = 255
    split[:, :, 2] = 255
    split2 = np.zeros([5, 4090, 3])
    split2[:, :, 0] = 255
    split2[:, :, 1] = 255
    split2[:, :, 2] = 255
    dirs = glob.glob(res_path + '*.jpg')
    i = 0
    # print
    for dir in dirs:
        img = cv2.imread(dir)
        #       print(img.shape)
        img = cv2.resize(img, (1360, 765), interpolation=cv2.INTER_CUBIC)
        # row = np.hstack([row,split,img])
        if i == 0:
            row = img
        else:
            if i % 3 == 0:
                if i == 3:
                    clo = row
                else:
                    print(clo.shape, split2.shape, row.shape)
                    clo = np.vstack([clo, split2, row])

                row = img
            else:
                print(row.shape, split.shape, img.shape)
                print(i, ':', row.shape)
                row = np.hstack((row, split, img))
        i += 1
    clo = np.vstack([clo, split2, row])
    cv2.imwrite('./result.jpg', clo)


def matplot18():
    success_18 = [68.0, 62.8, 61.9, 60.5, 56.9, 56.3, 56.2, 55.2, 53.6, 52.8]
    precision_18 = [92.9, 82, 87.1, 77.5, 77.3, 77.4, 75.4, 74.1, 72.1, 66.8]
    name_18 = ['LZZ-ECO', 'VITALD', 'STAPLE SRCA', 'BTT', 'DeCoM', 'SDRCO', 'AST', 'CFCNN', 'C3DT', 'DCST']
    # success_19 = [63.5, 61.7, 59.4, 59.3, 57.9, 56.8, 55.3, 54.4, 54.1, 53.2]
    # precision_19 = [90.0, 84.2, 81.6, 83.3, 76.8, 79.3, 76.5, 76.1, 74.1, 69.8]
    # name_19 = ['ED-ATOM', 'ATOMFR', 'SMILE', 'Siam-OM', 'DR-V-LT', 'SOT-SiamRPN++', 'TIOM', 'PTF', 'DATOM_AC', 'ACNT']
    success_19 = [75.5, 73.9, 73.2, 71.9, 71.0, 68.1, 67.5, 66.8, 66.2, 66.1]
    precision_19 = [94.7, 95.8, 89.1, 93.0, 86.6, 86.8, 84.1, 81.6, 78.5, 83.6]
    name_19 = ['ATOMFR', 'ED-ATOM', 'ACNT', 'Siam-OM', 'SMILE', 'TIOM', 'SOT-SiamRPN++', 'DR-V-LT', 'SiamFCOT', 'PTF']
    # color_18 = 'orangered'
    # color_19 = 'deepskyblue'

    plt.figure(figsize=(17.5, 15))
    plt.xlabel('success', fontsize=30)
    plt.ylabel('precision', fontsize=30)
    plt.xticks(np.arange(50, 81, 5), fontsize=25)
    plt.yticks(np.arange(50, 101, 10), fontsize=25)
    plt.xlim((50, 80))
    plt.ylim((50, 100))
    plt.grid(linestyle=':')

    # ec_18 = ['w', 'orangered', 'orangered', 'orangered', 'orangered', 'orangered', 'w', 'orangered', 'orangered', 'orangered']
    # ec_19 = ['w', 'deepskyblue', 'deepskyblue', 'deepskyblue', 'deepskyblue', 'deepskyblue', 'w',
    #          'deepskyblue', 'deepskyblue', 'deepskyblue']
    # markers = ['P', '>', '<', '*', 'v', 'o', 'X', 's', 'd', '^']
    # c_18 = ['orangered', 'w', 'w', 'w', 'w', 'w', 'orangered', 'w', 'w', 'w']
    # c_19 = ['deepskyblue', 'w', 'w', 'w', 'w', 'w', 'deepskyblue', 'w', 'w', 'w']

    ec_18 = ['w', 'brown', 'red', 'red', 'salmon', 'darksalmon', 'w', 'mistyrose', 'tomato', 'lightcoral']
    ec_19 = ['w', 'cyan', 'darkblue', 'blue', 'mediumblue', 'royalblue', 'w',
             'dodgerblue', 'lightskyblue', 'deepskyblue']
    markers = ['P', '>', '<', '*', 'v', 'o', 'X', 's', 'd', '^']
    c_18 = ['lightcoral', 'w', 'w', 'w', 'w', 'w', 'sienna', 'w', 'w', 'w']
    c_19 = ['deepskyblue', 'w', 'w', 'w', 'w', 'w', 'cornflowerblue', 'w', 'w', 'w']

    # ec_18 = ['orangered']
    # ec_19 = ['dodgerblue']
    # markers = ['P', '>', '<', '*', 'v', 'o', 'X', 's', 'd', '^']
    # c_18 = ['r']
    # c_19 = ['deepskyblue']
    lw = [4, 4.5, 4.5, 4.5, 4.5, 4.5, 4, 4.5, 4.5, 4.5]
    # markers = ['o', '>', 'v', '<', '^', '1', '2', '3', '4', '+']
    s = [450, 450, 450, 600, 450, 450, 450, 350, 350, 450]
    for i in range(10):
        f18 = plt.scatter(success_18[i], precision_18[i], marker=markers[i], edgecolors='red', linewidths=lw[i], color='orangered', s=s[i],
                              label=name_18[i])
    for i in range(10):
        f19 = plt.scatter(success_19[i], precision_19[i], marker=markers[i], edgecolors=ec_19[7], linewidths=lw[i], color=c_19[0], s=s[i],
                              label=name_19[i])

    plt.legend(bbox_to_anchor=(0., 1, 1, 0.17), columnspacing=160, loc='upper right',
               ncol=5, mode='expand', scatterpoints=1, frameon=False, fontsize=20)
    plt.savefig(os.path.join('F:/visdrone/2019/results/challenge_results', 'sot18.png'))

    plt.close()


def matplot19():
    success_19 = [63.5, 61.7, 59.4, 59.3, 57.9, 56.8, 55.3, 54.4, 54.1, 53.2]
    precision_19 = [90.0, 84.2, 81.6, 83.3, 76.8, 79.3, 76.5, 76.1, 74.1, 69.8]
    name_19 = ['ED-ATOM', 'ATOMFR', 'SMILE', 'Siam-OM', 'DR-V-LT', 'SOT-SiamRPN++', 'TIOM', 'PTF', 'DATOM_AC', 'ACNT']
    # color_19 = ['lightcoral', 'brown', 'red', 'red', 'salmon', 'darksalmon', 'sienna', 'mistyrose', 'tomato', 'coral']
    # color_19 = ['springgreen', 'mediumaquamarine', 'aquamarine', 'paleturquoise', 'cyan', 'deepskyblue', 'skyblue',
    #          'dodgerblue', 'teal', 'palegreen']
    color_19 = ['orange', 'chartreuse', 'red', 'yellow', 'cyan', 'mediumblue', 'aqua', 'magenta', 'deeppink', 'lime']
    # color_19 = ['deepskyblue']
    plt.figure(figsize=(9, 6.5), dpi=300)

    plt.xlabel('success', fontsize=15)
    plt.ylabel('precision', fontsize=15)
    plt.xticks(np.arange(50, 71, 4), fontsize=15)
    plt.yticks(np.arange(50, 101, 10), fontsize=15)
    plt.xlim((50, 70))
    plt.ylim((50, 100))
    markers = ['d', '>', 'h', '*', 'p', 'o', 'X', 's', 'H', '^']
    #    plt.figure(figsize=(5,6),dpi=60)
    for i in range(10):
        f19 = plt.scatter(success_19[i], precision_19[i], marker=markers[i], edgecolors='black', color=color_19[i], s=50,
                              label=name_19[i])

    # plt.subplot(212)
    plt.legend(bbox_to_anchor=(0., 1.1, 1, 0.01), columnspacing=160, loc='upper right',
               ncol=5, mode='expand', scatterpoints=1, frameon=False, fontsize='medium')
    # plt.annotate(model[i], (model_size[i] - horizontal[i], acc[i] + vertical[i]), fontsize=20)
    plt.savefig(os.path.join('F:/visdrone/2019/results/challenge_results', 'sot19.png'))

    plt.close()


if __name__ == '__main__':
    matplot18()
    # matplot19()
# getcat(ann)
# combine(res_path)
# vis(img,ann)