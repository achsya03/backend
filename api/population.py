
import re
import csv
import pandas as pd
from pymongo import MongoClient
from data.daerah import Daerah
import data.mongo_setup as mongo_setup

#CSV to JSON Conversion
class Population():
    result={}

    def add_population(self):
        mongo_setup.global_init()
        header= [ "nama_provinsi", "nama_kabupaten_kota", "nama_kecamatan", "nama_kelurahan",  "laki_laki", "perempuan"]
        csvfile = open('data_jkt.csv', 'r')
        reader = csv.DictReader( csvfile )
        #mongo_client=MongoClient("db", 27017)
        #db=mongo_client.test1
        #db.segment.drop()

        #val = 'DIY'
        #daerah = Daerah()
        #daerah.nama_provinsi=val
        #daerah.save()
        #obj = Daerah.objects(nama_provinsi=val) \
        #    .first()
        result = ""
        for each in reader:
            row={}
            daerah = Daerah()
            daerah.nama_provinsi = each[header[0]]
            daerah.nama_kabupaten_kota = each[header[1]]
            daerah.nama_kecamatan = each[header[2]]
            daerah.nama_kelurahan = each[header[3]]
            daerah.laki_laki = each[header[4]]
            daerah.perempuan = each[header[5]]

            result = daerah.save()

        return str(result)#str(res)

    def get_population(self,area):
        header= [ "nama_provinsi", "nama_kabupaten_kota", "nama_kecamatan", "nama_kelurahan",  "laki_laki", "perempuan"]
        mongo_client=MongoClient("db", 27017)
        db=mongo_client.test1_jkt_population
        _items = db.test1_jkt_population.find({'nama_kelurahan': str(area['neighbourhood'].upper())})
        items = [item for item in _items]
        result = {}
        for val in header:
            result[val] = items[0][val]

        return result
