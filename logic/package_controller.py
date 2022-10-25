import json
import os

from package import Package
PATH = os.getcwd()
DIR_DATA = PATH + '{0}data{0}'.format(os.sep)

class PackageController(object):

    def __init__(self):
        self.file = '{0}{1}'.format(DIR_DATA, 'package.json')

    def add(self, package: Package = Package()) -> str:
        with open(self.file, 'r+') as f:
            data = json.load(f)
        f.close()
        with open(self.file, 'w') as f:
            data['package'].append(package.diccionario())
            f.seek(0)
            json.dump(data, f)
        f.close()
        return package.__str__()

    def show(self):
        # Opening JSON file
        with open(self.file, 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
        return json_object
