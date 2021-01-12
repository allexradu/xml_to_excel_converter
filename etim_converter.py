import xml.etree.ElementTree as Et
import platform
import json

etim = {'features': {}, 'values': {}}

xml_file = 'xml\\etim.xml' if platform.system() == 'Windows' else 'xml/etim.xml'
json_file = 'json\\etim.json' if platform.system() == 'Windows' else 'json/etim.json'

etim_tree = Et.parse(xml_file)

root = etim_tree.getroot()

units = root.find('Features')

for unit in units:
    code = unit.find('Code').text
    translations = unit.find('Translations')
    description = translations.findall(".//Translation[@language='EN']")[0].find('Description').text
    etim['features'].update({code: description})
    print(description)

values = root.find('Values')

for value in values:
    code = value.find('Code').text
    translations = value.find('Translations')
    description = translations.findall(".//Translation[@language='EN']")[0].find('Description').text
    etim['values'].update({code: description})

with open(json_file, "w") as outfile:
    json.dump(etim, outfile, indent = 4)
