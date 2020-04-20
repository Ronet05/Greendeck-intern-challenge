import json
import numpy as np
import csv

class process_data:

    def discount_plist(self, filters):
        '''here, op1 can be 'discount','brand.name' and 'competition'.
        op which is the operator can be '>','<','=='.
        op2 depends on op1 whether it is a string or a float '''

        op1 = filters[0]
        op = filters[1]
        op2 = filters[2]

        # force the user to input int in form against discount in html
        ids = []
        if (op1 == 'discount'):
            d_perc = op2
            for p in product_json:
                reg_price = p['price']['regular_price']['value']
                off_price = p['price']['offer_price']['value']
                disc = (reg_price - off_price) * 100 / reg_price
                if (op == "==" and disc == op2):
                    ids.append(p['_id']['$oid'])
                elif (op == ">" and disc > op2):
                    ids.append(p['_id']['$oid'])
                elif (op == "<" and disc < op2):
                    ids.append(p['_id']['$oid'])

        # force the user to input str in form against brand.name in html
        elif (op1 == "brand.name"):
            for p in product_json:
                brand_name = p['brand']['name']
                if (brand_name == op2):
                    reg_price = p['price']['regular_price']['value']
                    off_price = p['price']['offer_price']['value']
                    if (off_price - reg_price < 0):
                        ids.append(p['_id']['$oid'])

        return ids