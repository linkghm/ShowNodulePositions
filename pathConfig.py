# -*- coding: utf-8 -*-
# @Time    : 2019/9/21 14:30
# @Author  : GUO Huimin
# @Email   : guohuimin2619@foxmail.com
# @FileName: pathConfig.py

from pathlib import Path

pathConfig = {
    # MHD or DCM
    # "raw_data_path": str(Path(r'')),
    # Numpy array
    "numpy_image_path": str(Path(r'C:\Users\GHM\Desktop\singleTest\preprocess\singleTest\512678_clean.npy')),
    # Label
    "label_path": str(Path(r'C:\Users\GHM\Desktop\singleTest\preprocess\singleTest\512678_label.npy')),
}
pathConfig_local = {
    # MHD or DCM
    # "raw_data_path": str(Path(r'')),
    # Numpy array
    "numpy_image_path": str(Path(r'C:/Users/GHM/Desktop/tmp/CropImage3931.npy')),
    # Label
    "label_path": str(Path(r'C:/Users/GHM/Desktop/tmp/Label3931.npy')),
}
