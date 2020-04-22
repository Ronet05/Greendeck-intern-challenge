import queries as qr
import filters as fl


def request_processing(product_json, request):
    queries = request['query_type'].split('|')
    filters = request['filters']

    # reordering the filters list to shift discount_diff to the end, as if competition is present,
    # it will automatically be in front
    for i in range(len(filters)):
        op1 = filters[i]['operand1']
        if op1 == "discount_diff":
            temp = filters[i]
            filters[i] = filters[-1]
            filters[-1] = temp
            break

    # first apply the filters
    subset = product_json
    comp_id = None
    for i in filters:
        op1 = i['operand1']
        op2 = i['operand2']
        op = i['operator']

        if op1 == "discount":
            subset = fl.discount(subset, op, op2)
        elif op1 == "brand.name":
            subset = fl.brandname(subset, op2)
        elif op1 == "competition":
            subset = fl.competition(subset, op2)
            comp_id = op2
        elif op1 == "discount_diff":
            # can put a try-catch block here to check for comp_id
            try:
                if comp_id is not None:
                    subset = fl.discount_diff(subset, op, op2, comp_id)
            except:
                return "Discount difference filter used without competition filter"

    # the query with the filters
    result = {}
    for query in queries:
        if query == "discounted_products_list":
            result["discounted_products_list"] = qr.discounted_products_list(subset)
        elif query == "avg_discount":
            result["avg_discount"] = qr.avg_discount(subset)
        elif query == "discounted_products_count":
            result["discounted_products_count"] = qr.discounted_products_count(subset)
        elif query == "expensive_list":
            result["expensive_list"] = qr.expensive_list(subset)
        elif query == "competition_discount_diff_list":
            result["competition_discount_diff_list"] = qr.competition_discount_diff_list(subset, filters)

    return result
