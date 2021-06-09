
import pandas as pd
from pymongo import MongoClient

#CSV to JSON Conversion
class Population():
    result={}

    def add_population(self):
        csvfile = open('data_jkt.csv', 'r')
        reader = csv.DictReader( csvfile )
        mongo_client=MongoClient("db", 27017)
        db=mongo_client.test1_jkt_population
        #db.segment.drop()
        header= [ "nama_provinsi", "nama_kabupaten_kota", "nama_kecamatan", "nama_kelurahan",  "laki_laki", "perempuan"]

        
        list1=[]
        dict1={}
        for each in reader:
            row={}
            for field in header:
                row[field]=each[field]
            res = db.test1_jkt_population.insert(row)

        return str(res)

    def get_population(self,area):
        mongo_client=MongoClient("db", 27017)
        db=mongo_client.test1_jkt_population
        result=[]
        _items = db.test1_jkt_population.find({'nama_kelurahan': str(area['neighbourhood'].upper())})
        items = [item for item in _items]

        return items[0]
