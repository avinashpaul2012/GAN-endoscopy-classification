# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 21:17:10 2020

@author: LEGION
"""


import os
import numpy as np
import shutil

# # Creating Train / Val / Test folders (One time use)
root_dir = 'data2'
benCls = '/Benign_BW'
malCls = '/Malignant_BW'

os.makedirs(root_dir +'/train' + benCls)
os.makedirs(root_dir +'/train' + malCls)
os.makedirs(root_dir +'/val' + benCls)
os.makedirs(root_dir +'/val' + malCls)
os.makedirs(root_dir +'/test' + benCls)
os.makedirs(root_dir +'/test' + malCls)

# Creating partitions of the data after shuffeling
currentCls = benCls
src = "Data2"+currentCls # Folder to copy images from

allFileNames = os.listdir(src)
np.random.shuffle(allFileNames)
train_FileNames, val_FileNames, test_FileNames = np.split(np.array(allFileNames),
                                                          [int(len(allFileNames)*0.4), int(len(allFileNames)*0.8)])


train_FileNames = [src+'/'+ name for name in train_FileNames.tolist()]
val_FileNames = [src+'/' + name for name in val_FileNames.tolist()]
test_FileNames = [src+'/' + name for name in test_FileNames.tolist()]

print('Total images: ', len(allFileNames))
print('Training: ', len(train_FileNames))
print('Validation: ', len(val_FileNames))
print('Testing: ', len(test_FileNames))

# Copy-pasting images
for name in train_FileNames:
    shutil.copy(name, "Data2/train"+currentCls)

for name in val_FileNames:
    shutil.copy(name, "Data2/val"+currentCls)

for name in test_FileNames:
    shutil.copy(name, "Data2/test"+currentCls)