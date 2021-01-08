import xml.etree.ElementTree as Et
import platform
from product import Product
import openpyxl as xl

xml_file = 'xml\\text.xml' if platform.system() == 'Windows' else 'xml/text.xml'
table_location = 'excel\\a.xlsx' if platform.system() == 'Windows' else 'excel/a.xlsx'
wb = xl.Workbook()
sh = wb[wb.sheetnames[0]]
products = []


def remove_none(d_list, is_text = False):
    for i in d_list:
        if i is not None:
            if is_text:
                return i.text
            else:
                return i


product_tree = Et.parse(xml_file)

root = product_tree.getroot()

for each_product in root.findall('PRODUCT'):
    product_details = each_product.find('PRODUCT_DETAILS')
    product_order_details = each_product.find('PRODUCT_ORDER_DETAILS')
    product_price_details = each_product.find('PRODUCT_PRICE_DETAILS')
    product_price = product_price_details.find('PRODUCT_PRICE')
    mime_info = each_product.find('MIME_INFO')
    user_defined_extensions = each_product.find('USER_DEFINED_EXTENSIONS')
    packing_units = user_defined_extensions.find('UDX.EDXF.PACKING_UNITS')
    packing_unit = remove_none([unit if unit.find('UDX.EDXF.QUANTITY_MIN').text == '1' else None for unit in
                                packing_units])

    product_id = each_product.find('SUPPLIER_PID').text
    international_pid = product_details.find('INTERNATIONAL_PID').text
    manufacturer_pid = product_details.find('MANUFACTURER_PID').text
    short_description = product_details.findall(".//DESCRIPTION_SHORT[@lang='eng']")[0].text
    long_description = product_details.findall(".//DESCRIPTION_LONG[@lang='eng']")[0].text
    manufacturer_name = product_details.find('MANUFACTURER_NAME').text
    manufacturer_type_descr = product_details.find('MANUFACTURER_TYPE_DESCR').text
    meta_key_words_list = product_details.findall(".//KEYWORD[@lang='eng']")
    meta_key_words = ', '.join([keyword.text for keyword in meta_key_words_list])

    order_unit = product_order_details.find('ORDER_UNIT').text
    content_unit = product_order_details.find('CONTENT_UNIT').text
    number_cu_per_ou = product_order_details.find('NO_CU_PER_OU').text
    price_quantity = product_order_details.find('PRICE_QUANTITY').text
    quantity_min = product_order_details.find('QUANTITY_MIN').text
    quantity_interval = product_order_details.find('QUANTITY_INTERVAL').text
    price_amount = product_price.find('PRICE_AMOUNT').text
    price_currency = product_price.find('PRICE_CURRENCY').text
    tax = product_price.find('TAX').text
    photo_normal = remove_none([mime.find('MIME_SOURCE') if (mime.find('MIME_PURPOSE').text == 'normal') else None for
                                mime in mime_info], True)
    photo_detail = remove_none([mime.find('MIME_SOURCE') if (mime.find('MIME_PURPOSE').text == 'detail') else None for
                                mime in mime_info], True)
    data_sheet = remove_none([mime.find('MIME_SOURCE') if (mime.find('MIME_PURPOSE').text == 'data_sheet') and (
            'locale=en_GB' in mime.find('MIME_SOURCE').text) else None for
                              mime in mime_info], True)
    volume = packing_unit.find('UDX.EDXF.VOLUME').text
    weight = packing_unit.find('UDX.EDXF.WEIGHT').text
    length = packing_unit.find('UDX.EDXF.LENGTH').text
    width = packing_unit.find('UDX.EDXF.WIDTH').text
    depth = packing_unit.find('UDX.EDXF.DEPTH').text
    products.append(
        Product(product_id = product_id, international_pid = international_pid, manufacturer_pid = manufacturer_pid,
                short_description = short_description, long_description = long_description,
                manufacturer_name = manufacturer_name, manufacturer_type_descr = manufacturer_type_descr,
                meta_key_words = meta_key_words, order_unit = order_unit, content_unit = content_unit,
                number_cu_per_ou = number_cu_per_ou, price_quantity = price_quantity, quantity_min = quantity_min,
                quantity_interval = quantity_interval, price_amount = price_amount, price_currency = price_currency,
                tax = tax, photo_normal = photo_normal, photo_detail = photo_detail, data_sheet = data_sheet,
                volume = volume, weight = weight, length = length, width = width, depth = depth))

columns = ['Product ID', 'International PID', 'Manufacturer PID', 'Short Description', 'Long Description',
           'Manufacturer Name', 'Manufacturer Type Description', 'Meta Key Words', 'Order Unit', 'Content Unit',
           'Number Cu per Ou', 'Price Quantity', 'Quantity Min', 'Quantity Interval', 'Price', 'Currency', 'Tax',
           'Photo', 'Photo Detail', 'Data Sheet', 'Volume', 'Weight', 'Length', 'Width', 'Depth']

row = 2

for column in range(1, len(columns) + 1):
    sh.cell(1, column).value = columns[column - 1]
    for prod in products:
        cols = [prod.product_id, prod.international_pid, prod.manufacturer_pid, prod.short_description,
                prod.long_description, prod.manufacturer_name, prod.manufacturer_type_descr, prod.meta_key_words,
                prod.order_unit, prod.content_unit, prod.number_cu_per_ou, prod.price_quantity, prod.quantity_min,
                prod.quantity_interval, prod.price_amount, prod.price_currency, prod.tax, prod.photo_normal,
                prod.photo_detail, prod.data_sheet, prod.volume, prod.weight, prod.length, prod.width, prod.depth]

        sh.cell(row, column).value = cols[column - 1]
        print(f'column: {column},row: {row}')
        row += 1
    row = 2
wb.save(table_location)
