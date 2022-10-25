import json
import os
PATH = os.getcwd()
DIR_DATA = PATH + '{0}data{0}'.format(os.sep)
from shipment_details import Shipment_details


class Shipment_detailsController(object):

    def __init__(self):
        self.file = '{0}{1}'.format(DIR_DATA, 'shipments_details.json')

    def add(self, shipment_deatils: Shipment_details = Shipment_details()) -> str:
        with open(self.file, 'r+') as f:
            data = json.load(f)
        f.close()
        with open(self.file, 'w') as f:    
            data['shipment_details'].append(shipment_deatils.diccionario())
            f.seek(0)
            json.dump(data, f)
        f.close()
        return shipment_deatils.__str__()

    def show(self):
        # Opening JSON file
        with open(self.file, 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
        return json_object