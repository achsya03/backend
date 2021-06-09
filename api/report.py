import os
import re
import datetime

from data.aduan import Aduan
from flask import request
import urllib.request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

import numpy as np
from efficientnet.tfkeras import EfficientNetB4

from google.cloud import storage
from werkzeug.utils import secure_filename

import data.mongo_setup as mongo_setup

class Report():


    def reshape(imgs_arr):
        return np.stack(imgs_arr, axis=0)

    
    def preprocess(img, input_size):
        nimg = img.convert('RGB').resize(input_size, resample= 0)
        img_arr = (np.array(nimg))/255
        return img_arr

    def classifier(files):
        input_size = (150,150)
        MODEL_PATH = 'model/mdl.h5'

        model = load_model(MODEL_PATH,compile=False)

        image1 = files

        urllib.request.urlretrieve(files, "test.jpg")

        im = Image.open("test.jpg")

        img = image.load_img("test.jpg", target_size=(150,150))
        #imgplot = plt.imshow(img)

        X = Report.preprocess(im,input_size)
        X = Report.reshape([X])
        y = model.predict(X)
        ls=['Cyclone', 'Earthquake', 'Flood', 'Wildfire']
        lbl=list(ls)
        #res = str(np.argmax(y))+"-"+str(np.max(y))

        return str(ls[np.argmax(y)])
    
    def upload_to_bucket(name, uploaded_file, bucket_name):
        try:
            storage_client = storage.Client()
            # Get the bucket that the file will be uploaded to.
            bucket = storage_client.get_bucket(bucket_name)

            id = datetime.datetime.now()

            id = re.sub(r'[\-|\:|\ |\.]', '',str(id))

            # Create a new blob and upload the file's content.
            ext = uploaded_file.filename.split(".")
            uploaded_file.filename='sub/'+str(name)+"-"+str(id)+"."+str(ext[-1])
            blob = bucket.blob(uploaded_file.filename)

            blob.upload_from_string(
                uploaded_file.read(),
                content_type=uploaded_file.content_type
            )

            # The public URL can be used to directly access the uploaded file via HTTP.
            return blob.public_url
        except Exception as e:
            return "ERROR : "+str(e)
    
    def add_report(self):
        mongo_setup.global_init()
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] =  "credential.json"
        CLOUD_STORAGE_BUCKET = 'foto_laporan'
        result = {}

        #+62XXXX
        wa_number = request.form.get("nomor_wa")
        uploaded_file = request.files.get("foto")
        disaster_time = request.form.get("waktu_bencana")
        caption = request.form.get("judul")
        desc = request.form.get("kronologi")
        #-7.XX,110.XX
        lat_long = request.form.get("lat_long")

        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "credential.json"

        storage_client = storage.Client()
        #split = uploaded_file.filename.split(".")

        gambar_uri = Report.upload_to_bucket(wa_number, uploaded_file, CLOUD_STORAGE_BUCKET)

        _gambar_uri = gambar_uri

        jenis = Report.classifier(_gambar_uri)

        aduan = Aduan()
        
        aduan.jenis_bencana = str(jenis)
        aduan.gambar_uri = str(_gambar_uri)
        aduan.waktu_bencana = disaster_time
        aduan.judul = caption
        aduan.kronologi = desc
        aduan.lat_long = str(lat_long)
        aduan.sender_wa_number = wa_number

        result={}
        for item in aduan:


        try:
            #aduan.save()
            return True
        except Exception as e:
            return "ERROR : "+str(e)

        # The public URL can be used to directly access the uploaded file via HTTP.
        #return str(jenis)

    def get_report(self):

        mongo_setup.global_init()

        header = ["waktu_aduan", "jenis_bencana", "gambar_uri", "waktu_bencana",  "judul", "kronologi", "lat_long", "sender_wa_number"]

        aduan = Aduan()
        result = {}
        _items = Aduan.objects()
        
        result = {}

        items = [item for item in _items]

        for val in header:
            result[val] = items[0][val]

        return result