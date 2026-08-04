from asset import Asset
from portofolio import Portofolio
import json
import os
def load_data():
    if not os.path.exists('portofolio.json'):
        portofolio=Portofolio()
        simpan_data(portofolio)
        return portofolio
    with open('portofolio.json','r') as file:
        data = json.load(file)
    portofolio = Portofolio()
    for item in data:
        aset = Asset(
            item['nama'],
            item['modal'],
            item['harga'],
            item['harga sekarang']
      )
        portofolio.aset.append(aset)
    return portofolio
def simpan_data(portofolio):
    data = portofolio.to_dict()
    with open('portofolio.json','w') as file:
        json.dump(data,file,indent=4)