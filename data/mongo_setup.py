import mongoengine
import os

def global_init():
    res = mongoengine.connect(host='db',alias='core', name='data_4')#name database
    return res