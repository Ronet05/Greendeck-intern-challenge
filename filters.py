import json
import csv


def discount_diff(subset_from_competition, op, op2, competing_id):
    result = []
    for p in subset_from_competition:
        if 'similar_products' in p:
            basket_price_NAP = p['price']['basket_price']['value']
            basket_price_comp = p['similar_products']['website_results'][competing_id]['meta']['avg_price']['basket']
            disc = (basket_price_NAP - basket_price_comp) * 100 / basket_price_NAP
            if op == "==" and disc == op2:
                result.append(p)
            elif op == ">" and disc > op2:
                result.append(p)
            elif op == "<" and disc < op2:
                result.append(p)
    return result


def competition(subset, op2):
    result = []
    for p in subset:
        if 'similar_products' in p:
            comp_data = p['similar_products']['website_results'][op2]
            if comp_data['meta']['total_results'] != 0:
                result.append(p)
    return result


def brandname(subset, op2):
    result = []
    for p in subset:
        brand_name = p['brand']['name']
        if brand_name == op2:
            result.append(p)

    return result


def discount(subset, op, op2):
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

