import pandas as pd
import numpy as np
import json
import csv


class QueryProcessing:

    def __int__(self, operand1, operand2, operator):
        op1 = operand1
        op2 = operand2
        op = operator

    def discount_diff(self, subset_from_competition, op, op2, competing_id):
        result = []
        for p in subset_from_competition:
            basket_price_NAP = p['price']['basket_price']['value']
            basket_price_comp = ['similar_products']['website_results'][competing_id]['meta']['avg_price']['basket']
            disc = (basket_price_NAP - basket_price_comp) * 100 / basket_price_NAP
            if op == "==" and disc == op2:
                result.append(p)
            elif op == ">" and disc > op2:
                result.append(p)
            elif op == "<" and disc < op2:
                result.append(p)
        return result

    def competition(self, subset, op2):
        result = []
        for p in subset:
            comp_data = p['similar_products']['website_results'][op2]
            if comp_data['meta']['total_results'] != 0:
                result.append(p)
        return result

    def brandname(self, subset, op2):
        result = []
        for p in subset:
            brand_name = p['brand']['name']
            if brand_name == op2:
                result.append(p)

        return result

    def discount(self, subset, op, op2):
        result = []
        for p in subset:
            reg_price = p['price']['regular_price']['value']
            off_price = p['price']['offer_price']['value']
            disc = (reg_price - off_price) * 100 / reg_price
            if op == "==" and disc == op2:
                result.append(p)
            elif op == ">" and disc > op2:
                result.append(p)
            elif op == "<" and disc < op2:
                result.append(p)

        return result
