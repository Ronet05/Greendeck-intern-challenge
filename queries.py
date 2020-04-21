import json
import numpy as np
import csv


class QueryProcessing:
    '''def competition_discount_diff_list(self, subset, filters):'''

    def expensive_list(self, subset):
        ids = []
        for p in subset:
            flag = 0
            for comp in p['similar_products']['website_results']:
                if p['similar_products']['website_results'][comp]['meta']['total_results'] != 0:

                    # pick minimum price because then there is atleast 1 listing that is at minimum cost on that website
                    comp_price = p['similar_products']['website_results'][comp]['meta']['min_price']['basket']
                    nap_price = p['price']['basket_price']['value']
                    if (nap_price - comp_price) > 0:
                        flag = 1
                        break
            if flag == 1:
                ids.append(p['_id']['$oid'])

        return ids

    def discounted_product_list(self, subset):
        ids = []
        for p in subset:
            # next statement because general condition for discount. if filter already exists, then this condition is
            # already true. Filter gives an additional parameter of discount percentage or brandname etc.
            if p['price']['offer_price'] < p['price']['regular_price']:
                ids.append(p['_id']['$oid'])
        return ids

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
