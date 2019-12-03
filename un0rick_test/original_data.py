import json
import os

import matplotlib.pyplot as plt
import numpy as np
import sys

from un0rick_test.json_proc import us_json

data_dir = "D:\\workspace\\Python\\2. Befs_un0ric\\Befs_Un0rick_modify"
json_dir = os.path.join(data_dir, "json")
file_name = "20191201a-1.json"
json_file = os.path.join(json_dir, file_name)
print(json_file)
# print(file, type(file))

class MYAPP():
    def JsonShow(self, json_file):
        with open(json_file) as json_file:
            json_data = json.load(json_file)
            data = json_data["data"]

            plt.plot(data)
            plt.show()

    def process(self, data_dir):
        image_folder = os.path.join(data_dir, "images")

        if not os.path.exists(image_folder):
            os.makedirs(image_folder)
            print("'images' folder created")

        for MyDataFile in os.listdir(data_dir):
            if os.path.splitext(MyDataFile)[1] == ".json":
                print(os.path.dirname(MyDataFile))
                y = us_json()
                y.show_images = True
                y.JSONprocessing(os.path.join(data_dir, MyDataFile))
                y.create_fft()
                y.save_npz()
                y.mkImg()
    def save_npz(self):
        """
           Saves the dataset as an NPZ, in the data folder.
        """
        path_npz = "data/"+self.iD+"-"+str(self.N)+".npz" # @todo: create folder if not.
        np.savez(path_npz, self)
APP = MYAPP()
APP.JsonShow(json_file)
APP.process(json_dir)