from flask import Flask, render_template, request, url_for, json, jsonify
import flask
import requests
import csv

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['POST'])
def home():
    return render_template("index.html")


# Contains all the data
product_json = []

with open('netaporter_gb_similar.json', encoding='utf-8') as fp:
    for product in fp.readlines():
        product_json.append(json.loads(product))


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
