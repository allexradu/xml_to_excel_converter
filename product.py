class Product(object):

    def __init__(self, product_id, international_pid, manufacturer_pid, short_description, long_description,
                 manufacturer_name, manufacturer_type_descr, meta_key_words, order_unit, content_unit,
                 number_cu_per_ou, price_quantity, quantity_min, quantity_interval, price_amount, price_currency, tax,
                 photo_normal, photo_detail, data_sheet, volume, weight, length, width, depth):
        self.product_id = product_id
        self.international_pid = international_pid
        self.manufacturer_pid = manufacturer_pid
        self.short_description = short_description
        self.long_description = long_description
        self.manufacturer_name = manufacturer_name
        self.manufacturer_type_descr = manufacturer_type_descr
        self.meta_key_words = meta_key_words
        self.order_unit = order_unit
        self.content_unit = content_unit
        self.number_cu_per_ou = number_cu_per_ou
        self.price_quantity = price_quantity
        self.quantity_min = quantity_min
        self.quantity_interval = quantity_interval
        self.price_amount = price_amount
        self.price_currency = price_currency
        self.tax = tax
        self.photo_normal = photo_normal
        self.photo_detail = photo_detail
        self.data_sheet = data_sheet
        self.volume = volume
        self.weight = weight
        self.length = length
        self.width = width
        self.depth = depth
