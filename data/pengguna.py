import mongoengine
import random

from data.aduan import Aduan

class Pengguna(mongoengine.Document):

    id_pengguna = mongoengine.StringField(required=True)
    nama = mongoengine.StringField(required=True)
    alamat = mongoengine.StringField(required=True)
    jenis_kelamin = mongoengine.IntField(default=0)
    nomor_wa = mongoengine.StringField(required=True)
    jenis_pengguna = mongoengine.StringField(required=True)

    #aduans = mongoengine.ListField()

    meta = {
        'db_alias': 'core',
        'collection': 'pengguna'
    }