# -*- coding: utf-8 -*-
# @Time    : 2019/9/22 13:52
# @Author  : GUO Huimin
# @Email   : guohuimin2619@foxmail.com
# @FileName: showUtils.py

# Related functions
import numpy as np
import cv2
from pathlib import Path
from matplotlib import pyplot as plt
from matplotlib.patches import Ellipse


def showPosition(image_path, info):
    '''
    Show positions of nodules
    :param image_path: Image path
    :param info: List, [(z,y,x,d), ...]
    :return: Images, show positions of nodules
    '''
    image_path = str(Path(rf'{image_path}').as_posix())
    image = np.load(image_path).squeeze()
    print(f"There are {len(info)} nodules\n")
    for idx, singlePosition in enumerate(info):
        z, y, x, diameter_y, diameter_x = singlePosition[0], singlePosition[1], singlePosition[2], singlePosition[3], \
                                          singlePosition[4]
        plt.imshow(image[np.int(z), :, :], cmap='gray')
        plt.gca().add_patch(
            Ellipse(xy=(x, y), height=(diameter_x), width=(diameter_y), edgecolor='r', fill=False)
            # plt.Circle(xy=(x, y), radius=(diameter_x / 2), edgecolor='r', fill=False)
            # plt.Rectangle(xy=(x, y), height=(diameter_x / 2), width=(diameter_y / 2), edgecolor='r', fill=False)
        )
        plt.show()
        print(
            f"Index:{idx}| Coordinates: coord_z {z}, coord_y {y}, coord_x {x}| Diameter: dia_y {diameter_y}, dia_x {diameter_x}")
    pass


if __name__ == '__main__':
    image_path = r"C:\Users\GHM\Desktop\singleTest\preprocess\singleTest\320831_clean.npy"
    label_path = r'C:\Users\GHM\Desktop\singleTest\preprocess\singleTest\320831_label.npy'
    labels = np.load(label_path)
    info = []
    for label in labels:
        z, y, x, diameter_y, diameter_x = label[0], label[1], label[2], label[4], \
                                          label[5]
        info.append((z, y, x, diameter_y, diameter_x))
    showPosition(image_path, info)
