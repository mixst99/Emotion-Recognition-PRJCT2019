import numpy as np
import pandas as pd
import os
from PIL import Image
from torchvision import transforms

fer_data = pd.read_csv('fer2013.csv')

resize = transforms.Resize(448)
path_to_save = 'data/fer/'

emotions = {0, 6, 5, 1}
emo_map = {0: 'Anger', 1: 'Disgust', 5: 'Surprise', 6: 'Neutral'}

fer_data = fer_data[fer_data['emotion'].isin(emotions)]
fer_data['emotion'] = fer_data['emotion'].map(emo_map)
fer_data.drop('Usage', axis=1, inplace=True)
fer_data.reset_index(drop=True, inplace=True)


def save_fer_img():
    for index, row in fer_data.iterrows():
        pixels = np.asarray(list(row['pixels'].split(' ')), dtype=np.uint8)
        img = pixels.reshape((48, 48))
        img = Image.fromarray(img)
        img = resize(img)
        img.save(os.path.join(path_to_save, row['emotion'], str(index) + '.jpg'))


save_fer_img()
