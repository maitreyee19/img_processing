import numpy as np
import cv2
import os
import time
from neirestUtil import nearestFeatures
from config import *
import sys

configuration =get_config()
pathToSaveDir = ''
if pathToSaveDir != '':
    pathToSaveDir = pathToSaveDir + '/'
resolution = (375, 500)
rotated_resolution = (500, 375)


def checkPageInfo(payload):
    global page_info
    sift = cv2.xfeatures2d.SIFT_create()
    print("Loading datas...")
    start = time.time()
    try:
        print(configuration["feature_data_dir"] +os.sep+ 'featuresDB.npy')
        featuresDB = np.load(configuration["feature_data_dir"] +os.sep+ 'featuresDB.npy')
        featuresIndex = np.load(configuration["feature_data_dir"] +os.sep+ 'featuresIndex.npy')
    except:
        print('Database not found. Considere running CreateDB.py first, '
              'or check the path to the save directory.')

    featuresIndex = np.ndarray.tolist(featuresIndex)
    end = time.time()
    print("Done in {:.4f} seconds.".format(end - start))

    start = time.time()
    print(payload)
    queryPic = cv2.imread(payload)
    if queryPic is not None:
        if queryPic.shape[1] < queryPic.shape[0]:
            queryPic = cv2.resize(queryPic, resolution)
        else:
            queryPic = cv2.resize(queryPic, rotated_resolution)
        _, descriptors = sift.detectAndCompute(queryPic, None)
        nearest = nearestFeatures(descriptors, featuresDB, featuresIndex)
        end = time.time()
        page_info = nearest
        print("This is the page number {}.".format(nearest))
        print("Query time : {:.4f} seconds.".format(end - start))
    else:
        print('This path is not valid.')
        page_info = "NO PAGE FOUND"

    print('Terminated.')
    return page_info


if __name__ == '__main__':
    checkPageInfo()
