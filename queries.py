import json
import numpy as np
import csv


class QueryProcessing:
    '''def competition_discount_diff_list(self, subset):

    def expensive_list(self, subset):

    def discounted_product_list(self, subset):'''

    # should work without filter as well, therefore generalize it for entire dataset
    def avg_discount(self, subset):
        sum_discounts = 0
        for p in subset:
            offer_price = p['price']['offer_price']['value']
            regular_price = p['price']['regular_price']['value']
            discount = (offer_price - regular_price) * 100 / regular_price
            sum_discounts += discount
        avg_discount = sum_discounts / len(subset)
        return avg_discount

    # should work without filter as well, therefore generalize it for entire dataset
    def discounted_product_count(self, subset):
        ids = []
        for p in subset:
            # next statement because general condition for discount. if filter already exists, then this condition is
            # already true. Filter gives an additional parameter of discount percentage or brandname etc.
            if p['price']['offer_price'] < p['price']['regular_price']:
                ids.append(p['_id']['$oid'])
        return len(ids)
