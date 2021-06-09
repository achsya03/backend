from data.pengguna import Pengguna
from flask import request
from api.wa_twilio import Whatsapp

import re
import random
import datetime

import data.mongo_setup as mongo_setup
    


class Account():
    def rand_token():
        rand1 = random.randrange(100, 1000, 3)
        rand2 = random.randrange(100, 1000, 3)
        return str(rand1)+str(rand2)

    def add_account(self):

        mongo_setup.global_init()
        result = {}

        id = datetime.datetime.now()
        stat = False

        heads = ['nama', 'alamat', 'jenis_kelamin', 'nomor_wa', 'jenis_pengguna']
        for head in heads:
            result[head]=request.form.get(head)

        result['id'] = re.sub(r'[\-|\:|\ |\.]', '',str(id))
        result['token'] = rand_token()

        pengguna = Pengguna()
        
        pengguna.id_pengguna = result['id']
        pengguna.nama = result[heads[0]]
        pengguna.alamat = result[heads[1]]
        pengguna.jenis_kelamin = result[heads[2]]
        pengguna.nomor_wa = result[heads[3]]
        pengguna.jenis_pengguna = result[heads[4]]
        objs = Pengguna.objects()
        for obj in objs:
            #test.append(n_wa.nomor_wa)
            if obj.nomor_wa == result[heads[3]]:
                result.clear()
                stat = False
                return "Error : Redundant whatsapp number"
        
        #result['status'] = "Success"
        wa = Whatsapp()
        status = wa.send("+14155238886",result[heads[3]], result['token'])

        result["send"] = status

        if status == "Success":
            res = pengguna.save()
            stat = True

        #id = re.sub(r'[\-|\:|\ |\.]', '',str(id))
        #wa = WABot()
        #x=wa.send_message(str(pengguna.nomor_wa)+"@c.us", result['token'], result[heads[3]])

        

        return result

    def get_account(self, nomor_wa):

        mongo_setup.global_init()

        head = ["id_pengguna", "nama", "alamat", "jenis_kelamin",  "nomor_wa", "jenis_pengguna"]

        pengguna = Pengguna()
        result = {}
        objs = Pengguna.objects(nomor_wa=nomor_wa).first()
        

        token = rand_token()
        
        #result['status'] = "Success"
        wa = Whatsapp()
        status = wa.send("+14155238886",nomor_wa, token)
        result["nomor_wa"] = nomor_wa
        result["send"] = status
        result["token"] = token
        #res = pengguna.save()
        #else:
            #result['status'] = "Error : Wrong number"

        return result