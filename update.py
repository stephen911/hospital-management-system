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
                                                                                                global detections 
                                                                                                        (h, w) = frame.shape[:2]
                                                                                                                blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300),(104.0, 177.0, 123.0))
                                                                                                                
                                                                                                                        ~ pass the blob through the network and obtain the face detections
                                                                                                                                faceNet.setInput(blob)
                                                                                                                                "