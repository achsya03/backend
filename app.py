import os

import requests

from api.weather import Weather 
from api.population import Population
from api.location_find import Location_Find
from api.account import Account
from api.report import Report

from data.aduan import Aduan
from data.daerah import Daerah
from data.pengguna import Pengguna

import data.mongo_setup as mongo_setup

from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("db", 27017)
db = client.test1
#mongo_setup.global_init()

@app.route('/')
def show():

  url="https://aa4150006c80.ngrok.io/"
  return render_template('note.html', url=url)

@app.route('/area/show')
def todo():
  mongo_setup.global_init()
  test=[]
  daerah = Daerah.objects()
  items = daerah
  head = ["nama_provinsi", "nama_kabupaten_kota", "nama_kecamatan", "nama_kelurahan",  "laki_laki", "perempuan"]
  #for i in daerah:
  #  test.append(i)
  length = len(items)
  return render_template('todo.html', items=items, head=head)

@app.route('/weather/<lat>/<long>', methods=['GET'])
def weather(lat,long):

  _weather = Weather()
  _result = _weather.get_weather(lat,long)

  _location_find = Location_Find()
  result = _location_find.find(lat,long)
  result["weather"] = _result
  return result

@app.route('/population/add', methods=['GET'])
def population_add():

  _population = Population()
  result = _population.add_population()
  

  #db.tododb.insert_one(item_doc)

  return result

@app.route('/report/view', methods=['GET'])
def report():

  return render_template('foto.html')

@app.route('/report/add', methods=['POST'])
def report_add():
  _report = Report()
  result = _report.add_report()
  

  return result

@app.route('/account/add', methods=['POST'])
def account_add():

  _account = Account()
  result = _account.add_account()
  

  #db.tododb.insert_one(item_doc)

  return result

@app.route('/account/get/<wa>', methods=['GET'])
def account_get(wa):

  _account = Account()
  result = _account.get_account(wa)
  

  #db.tododb.insert_one(item_doc)

  return result

@app.route('/account/show', methods=['GET'])
def view():
  mongo_setup.global_init()
  test=[]
  pengguna = Pengguna.objects()
  items = pengguna
  head = ["id_pengguna", "nama", "alamat", "jenis_kelamin",  "nomor_wa", "jenis_pengguna"]
  #for i in daerah:
  #  test.append(i)
  length = len(items)
  return render_template('view1.html', items=items, head=head)

@app.route('/location/<lat>/<long>', methods=['GET'])
def location_find(lat,long):

  _location= Location_Find()
  _result = _location.find(lat,long)

  _population = Population()
  __result = _population.get_population(_result) 

  #db.tododb.insert_one(item_doc)

  return __result

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
