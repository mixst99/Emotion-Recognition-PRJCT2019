import torch
from torch.utils.data import Dataset
import os
import cv2
import numpy as np
import json


class DetectDataset(Dataset):
    """Face detection dataset"""
    dir_ = os.path.dirname(__file__)

    def __init__(self, path='../data/detection/'):
        self.datadir = os.path.join(self.dir_, path, 'images')
        self.images = np.array(os.listdir(self.datadir))
        self.ground_tr_dir = os.path.join(self.dir_, path, 'dict_metadata.txt')

        with open(self.ground_tr_dir, 'r') as file:
            self.ground_tr = json.load(file)

    def __getitem__(self, item):
        if torch.is_tensor(item):
            item = item.tolist()

        img_name = os.path.join(self.datadir, self.images[item])
        image = cv2.imread(img_name)

        face_rect = self.ground_tr[self.images[item][:16]]
        sample = (image, face_rect)

        return sample

    def __len__(self):
        return len(self.images)
