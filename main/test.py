'''
Author: hibana2077 hibana2077@gmail.com
Date: 2023-12-15 15:45:43
LastEditors: hibana2077 hibana2077@gmail.com
LastEditTime: 2023-12-15 15:55:15
FilePath: \plant-disease-research\main\test.py
Description: This is a test file to check if CUDA is available
'''
from torch import cuda
import tensorflow as tf

if cuda.is_available():
    print("CUDA is available")
else:
    print("CUDA is not available")

if tf.test.gpu_device_name():
    print("Default GPU Device: {}".format(tf.test.gpu_device_name()))
else:
    print("Please install GPU version of TF")