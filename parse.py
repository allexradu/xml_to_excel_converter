import xml.etree.ElementTree as Et
import platform

xml_file = 'xml\\text.xml' if platform.system() == 'Windows' else 'xml/text.xml'


def remove_none(d_list, is_text):
    for i in d_list:
        # print(i)
        if i is not None:
            if is_text:
                return i.text
            else:
                return i


product_tree = Et.parse(xml_file)

root = product_tree.getroot()

for product in root.findall('PRODUCT'):
    product_details = product.find('PRODUCT_DETAILS')
    product_order_details = product.find('PRODUCT_ORDER_DETAILS')
    product_price_details = product.find('PRODUCT_PRICE_DETAILS')
    product_price = product_price_details.find('PRODUCT_PRICE')
    mime_info = product.find('MIME_INFO')
    user_defined_extensions = product.find('USER_DEFINED_EXTENSIONS')
    packing_units = user_defined_extensions.find('UDX.EDXF.PACKING_UNITS')
    packing_unit = remove_none([unit if unit.find('UDX.EDXF.QUANTITY_MIN').text == '1' else None for unit in
                                packing_units], False)

    pid = product.find('SUPPLIER_PID').text
    product_details_text = product_details.text
    short_description = product_details.findall(".//DESCRIPTION_SHORT[@lang='eng']")[0].text
    long_description = product_details.findall(".//DESCRIPTION_LONG[@lang='eng']")[0].text
    international_pid = product_details.find('INTERNATIONAL_PID').text
    manufacturer_pid = product_details.find('MANUFACTURER_PID').text
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

    print(long_description)
    # print(mime_info[0].findall('MIME'))
