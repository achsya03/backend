import mongoengine
import datetime

class Aduan(mongoengine.Document):
    waktu_aduan = mongoengine.DateTimeField(default=datetime.datetime.now)

    jenis_bencana = mongoengine.StringField(required=True)
    gambar_uri = mongoengine.StringField(required=True)
    waktu_bencana = mongoengine.DateTimeField(required=True)
    judul = mongoengine.StringField(required=True)
    kronologi = mongoengine.StringField(required=True)
    lat_long = mongoengine.StringField(required=True)
    sender_wa_number = mongoengine.StringField(required=True)

    #validasi
    validator_wa_number = mongoengine.StringField()

    meta = {
        'db_alias': 'core',
        'collection': 'aduan'
    }