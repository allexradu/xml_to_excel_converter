import xml.etree.ElementTree as Et
import platform
import openpyxl as xl
import json

xml_file = 'xml\\a.xml' if platform.system() == 'Windows' else 'xml/a.xml'
table_location = 'excel\\atrib.xlsx' if platform.system() == 'Windows' else 'excel/atrib.xlsx'
json_file = 'json\\etim.json' if platform.system() == 'Windows' else 'json/etim.json'

with open(json_file) as f:
    etim = json.load(f)

product_tree = Et.parse(xml_file)
root = product_tree.getroot()
catalog = root.find('T_NEW_CATALOG')
wb = xl.Workbook()
sh = wb[wb.sheetnames[0]]

current_col = 2
current_row = 2

for each_product in catalog.findall('PRODUCT'):
    product_id = each_product.find('SUPPLIER_PID').text if each_product.find('SUPPLIER_PID') is not None else 'n/a'
    print('row: ', current_row)
    sh.cell(current_row, 1).value = product_id

    features = each_product.find('PRODUCT_FEATURES').findall('FEATURE')
    for feature in features:
        feature_name = feature.find('FNAME')
        sh.cell(current_row, current_col).value = etim['features'][feature_name.text] if feature_name.text not in [
            '-'] else feature_name.text
        values_tags = feature.findall('FVALUE')
        values = []
        for value in values_tags:
            if value.text[:2] == 'EV':
                values.append(etim['values'][value.text])
            else:
                values.append(value.text)
        final_value = '<br>'.join(values)
        sh.cell(current_row, current_col + 1).value = final_value
        current_col += 2
    current_col = 2
    current_row += 1

wb.save(table_location)
