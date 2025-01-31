import json
import csv


class QueryProcessing:
    def expensive_list(self, subset):
        ids = []
        for p in subset:
            flag = 0
            if 'similar_products' in p:
                for comp in p['similar_products']['website_results']:
                    if p['similar_products']['website_results'][comp]['meta']['total_results'] != 0:

                        # pick minimum price because then there is atleast 1 listing that is at minimum cost on that
                        # website so a customer will definitely would want to purchase the cheapest option,
                        # so that can become the comparison point

                        comp_price = p['similar_products']['website_results'][comp]['meta']['min_price']['basket']
                        nap_price = p['price']['basket_price']['value']
                        if (nap_price - comp_price) > 0:
                            flag = 1
                            break
                if flag == 1:
                    ids.append(p['_id']['$oid'])

        return ids

    def competition_discount_diff_list(self, subset, filters):
        ids = []
        flag_d = 0
        flag_c = 0
        for f in filters:
            op1 = f['operand1']
            if op1 == "competition":
                flag_c += 1
            elif op1 == "discount_diff":
                flag_d += 1
        if not (flag_d >= 1 and flag_c >= 1):
            # should actually return error in browser
            return "Not Selected Competition or Discount Difference amount"

        for p in subset:
            ids.append(p['_id']['$oid'])

        return ids

    def discounted_products_list(self, subset):
        ids = []
        for p in subset:
            # next statement because general condition for discount. if filter already exists, then this condition is
            # already true. Filter gives an additional parameter of discount percentage or brandname etc.
            if p['price']['offer_price']['value'] < p['price']['regular_price']['value']:
                ids.append(p['_id']['$oid'])
        return ids

    def avg_discount(self, subset):
        sum_discounts = 0
        for p in subset:
            offer_price = p['price']['offer_price']['value']
            regular_price = p['price']['regular_price']['value']
            discount = (regular_price - offer_price) * 100 / regular_price
            sum_discounts += discount
        try:
            avg_discount = sum_discounts / len(subset)
        except ZeroDivisionError:
            return "Returned a null file. Average discount throws ZeroDivisionError!"

        return avg_discount

    def discounted_products_count(self, subset):
        ids = []
        for p in subset:
            # next statement because general condition for discount. if filter already exists, then this condition is
            # already true. Filter gives an additional parameter of discount percentage or brandname etc.
            if p['price']['offer_price']['value'] < p['price']['regular_price']['value']:
                ids.append(p['_id']['$oid'])
        return len(ids)
