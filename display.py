"""
~ -*- coding: utf-8 -*-
"""
Created on Wed Sept 30 00:40:47 2020

@author: Vineeta
"""


import numpy as np
import imutils
import time
import cv2
import os
import math

~system libraries
import os
import sys
from threading import Timer
import shutil
import time


def create_dataset_folders(dataset_path,labels):
        for label in labels:
                    dataset_folder = dataset_path+"\\"+label
                            if not os.path.exists(dataset_folder):
                                            os.makedirs(dataset_folder)
                                                        
                                                        def detect_face(frame, faceNet,threshold=0.5):
                                                                ~ grab the dimensions of the frame and then construct a blob
                                                                    ~ from it
                                                                    



"""