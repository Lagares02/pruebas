from http import client
import json
import os
PATH = os.getcwd()
DIR_DATA = PATH + '{0}data{0}'.format(os.sep)
from client import Client


class ClientController(object):

    def __init__(self):
        self.file = '{0}{1}'.format(DIR_DATA, 'client.json')

    def add(self, client: Client = Client()) -> str:
        with open(self.file, 'r+') as f:
            data = json.load(f)
        f.close()
        with open(self.file, 'w') as f:    
            data['client'].append(client.diccionario())
            f.seek(0)
            json.dump(data, f)
        f.close()
        return client.__str__()

    def show(self):
        # Opening JSON file
        with open(self.file, 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
        return json_object