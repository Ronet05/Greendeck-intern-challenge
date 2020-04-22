from flask import Flask, render_template, request, url_for, json, jsonify
import data_processing
import flask
import requests
import csv

app = Flask(__name__)
app.config['DEBUG'] = True


def prepare_dataset():
    product_json = []
    with open('json/netaporter_gb_similar.json', encoding='utf-8') as fp:
        for product in fp.readlines():
            product_json.append(json.loads(product))
    return product_json


@app.route('/')
def home():
    dataset = prepare_dataset()
    return jsonify(dataset[:5])


@app.route('/v1/api/test', methods=['POST'])
def process_query():
    post_request = request.get_json(force=True)
    dataset = prepare_dataset()
    response = data_processing.request_processing(dataset, post_request)
    return response


# Contains all the data


@app.route('/api/v1/resources/products/all', methods=['GET'])
def api_all():
    return jsonify(product_json)


@app.route('/api/v1/resources/products', methods=['POST'])
def product_id():
    if 'queries' in request.args:
        queries = str(request.args.get('queries'))
    else:
        return "Error: No query field provided. Please specify a pid."
    filters = request.args.get('filters')
    query_list = queries.split("|")
    results = {"queries": query_list, "filters": filters}
    return jsonify(results)


app.run()
