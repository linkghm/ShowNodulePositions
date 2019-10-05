# -*- coding: utf-8 -*-
# @Time    : 2019/9/21 14:36
# @Author  : GUO Huimin
# @Email   : guohuimin2619@foxmail.com
# @FileName: main.py

from pathConfig import pathConfig, pathConfig_local
from showUtils import *

if __name__ == '__main__':
    numpy_image = pathConfig_local["numpy_image_path"]
    labels = np.load(pathConfig_local["label_path"])
    info = []
    labels = [labels]
    for label in labels:
        z, y, x, diameter_y, diameter_x = label[0], label[1], label[2], label[4], \
                                          label[5]
        info.append((z, y, x, diameter_y, diameter_x))

    showPosition(image_path=numpy_image, info=info)
