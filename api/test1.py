from data.aduan import Aduan
from flask import request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image
import requests
from io import BytesIO
import numpy as np
from efficientnet.tfkeras import EfficientNetB4


import data.mongo_setup as mongo_setup

class Report():


    def reshape(imgs_arr):
        return np.stack(imgs_arr, axis=0)

    
    def preprocess(img, input_size):
        nimg = img.convert('RGB').resize(input_size, resample= 0)
        img_arr = (np.array(nimg))/255
        return img_arr
    
    
    def add_report(self):
        mongo_setup.global_init()
        result = {}

        #foto = request.files("foto")


        input_size = (150,150)
        MODEL_PATH = 'model/mdl.h5'
        model = load_model(MODEL_PATH,compile=False)

        image1 = 'test1/flood.jpg'

        im = Image.open(image1)

        img = image.load_img(image1, target_size=(150,150))
        #imgplot = plt.imshow(img)

        X = Report.preprocess(im,input_size)
        X = Report.reshape([X])
        y = model.predict(X)
        ls=['paper', 'rock', 'scissors']
        lbl=list(ls)
        res = str(np.argmax(y))+"-"+str(np.max(y))
        #res = lbl[np.argmax(y)], np.max(y)
        # read image
        #files = ['test1/flood.jpg','test1/flood1.jpg']

        #im = Image.open(files[0])

        #img = image.load_img(files[0], target_size=(150,150))
        #imgplot = plt.imshow(img)

        #nimg = img.convert('RGB').resize(3, resample= 0)
        #img_arr = (np.array(im))/255

        #X = np.stack(img_arr, axis=0)

        #X = preprocess(im,4)
        #X = reshape([X])
        #y = model.predict(X)
        #labels = ['flood', 'landslide', 'earthquake', "hurricane"]
        #lbl=list(labels)
        #res = lbl[np.argmax(y)], np.max(y) 
        
        return res