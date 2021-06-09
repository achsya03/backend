import mongoengine

#Provinsi
class Daerah(mongoengine.Document):
    nama_provinsi = mongoengine.StringField(required=True)
    nama_kabupaten_kota = mongoengine.StringField(required=True)
    nama_kecamatan = mongoengine.StringField(required=True)
    nama_kelurahan = mongoengine.StringField(required=True)
    laki_laki = mongoengine.IntField(required=True)
    perempuan = mongoengine.IntField(required=True)

    #penanggungjawab
    id_pengguna = mongoengine.ListField()

    meta = {
        'db_alias': 'core',
        'collection': 'daerah'
    }
