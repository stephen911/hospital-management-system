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
                                                                                                                                        detections = faceNet.forward()
                                                                                                                                        
                                                                                                                                                ~ initialize our list of faces, their corresponding locations,
                                                                                                                                                        ~ and the list of predictions from our face mask network
                                                                                                                                                                locs = []
                                                                                                                                                                        ~ loop over the detections
                                                                                                                                                                                for i in range(0, detections.shape[2]):
                                                                                                                                                                                                        ~ extract the confidence (i.e., probability) associated with
                                                                                                                                                                                                                        confidence = detections[0, 0, i, 2]
                                                                                                                                                                                                                        
                                                                                                                                                                                                                                        ~ filter out weak detections by ensuring the confidence is
                                                                                                                                                                                                                                                        ~ greater than the minimum confidence
                                                                                                                                                                                                                                                                        if confidence > threshold:
                                                                                                                                                                                                                                                                                                        ~ compute the (x, y)-coordinates of the bounding box for
                                                                                                                                                                                                                                                                                                                                ~ the object
                                                                                                                                                                                                                                                                                                                                                        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                                                                                                                                                                                                                                                                                                                                                                                (startX, startY, endX, endY) = box.astype("int")
                                                                                                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                                                                                                                        ~ ensure the bounding boxes fall within the dimensions of
                                                                                                                                                                                                                                                                                                                                                                                                                                ~ the frame
                                                                                                                                                                                                                                                                                                                                                                                                                                                        (startX, startY) = (max(0, startX), max(0, startY))
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                (endX, endY) = (min(w - 1, endX), min(h - 1, endY))
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            "