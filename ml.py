#pip install tensorflow
#pip install tflearn
#pip install tqdm

import  cv2
import numpy as np
import os
from random import shuffle
from tqdm import tqdm

TRAIN_DIR = ''
TEST_DIR = ''
IMG_SIZE = 50
LR = 1e-3

MODEL_NAME = 'dogsvscats-{}-{}.model'.format(LR,'2conv-basic')

def label_img(img):
  word_label = img.split('.')[-3]
  if word_label == 'cat':return [1,0]
  elif word_label == 'dog':return [0,1]