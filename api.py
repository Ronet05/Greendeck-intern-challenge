from flask_cors import CORS
from flask import request, json, jsonify
import data_processing
import gdown
import flask
import os
from zipfile import ZipFile

# it should be noted that the Heroku server currently running uses the demo dataset, i.e. netaporter_gb_similar.json.
# Due to limitations in the server, I could not get the test data running on the Heroku server. it might probably
# work with a premium server, but I tried on the free community version; therefore, results may vary.

# google drive link to download the test file
url = 'https://drive.google.com/a/greendeck.co/uc?id=19r_vn0vuvHpE-rJpFHvXHlMvxa8UOeom&export=download'

# below is the google drive link to download the compressed version of the test file. please note, due to limited
# timeout setting of 30 secs on Heroku, the json was not being able to download, and was neither able to extract into
# a json list on memory. Thus, I thought of using a compressed file, and then unziping when the APP is initialized.
# Turns out, that causes a timeout error too

url_compressed = 'https://drive.google.com/uc?id=1I4S305lTPkiTpyAJzZ49kgiwRkJkHuGK'

# Create Flask application
app = flask.Flask(__name__)
app.config['DEBUG'] = True
CORS(app)

# the following function will download and store the file in the dumps file. If you want to download the raw json,
# change the extension of file to .json in the dump_path
def init_files(dump_path='dumps/netaporter_gb.zip'):
    if dump_path.split('/')[0] not in os.listdir():
        os.mkdir(dump_path.split('/')[0])
    if os.path.exists(dump_path):
        pass
    else:
        gdown.download(url=url_compressed, output=dump_path, quiet=False)


# if you want to try using the zipped file, please extract using this method below
def extract_zip(path='dumps/netaporter_gb.zip'):
    with ZipFile(path, 'r') as file:
        file.extractall('dumps/')


# the below function is for taking the json file and converting into a list (essentially a json object) for querying

def prepare_dataset(path):
    product_json = []
    with open(path, encoding='utf-8') as fp:
        for product in fp.readlines():
            product_json.append(json.loads(product))
    return product_json


'''please uncomment the below 2 lines if you want encorporate downloading and extracting zip files, or simply 
downloading the raw json data and storing  it '''
# init_files('dumps/netaporter_gb.zip')
#extract_zip('dumps/netaporter_gb.zip')
dataset = prepare_dataset('dumps/netaporter_gb_similar.json')


@app.route('/', methods=['POST'])
def process_query():
    post_request = request.get_json(force=True)
    response = data_processing.request_processing(dataset, post_request)
    return response


if __name__ == "__main__":
    app.run()
