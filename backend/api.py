"""
Simple API to return similar brands.
This is just a prototype, so no worries about the details of the file.
"""

import json
from typing import List
from flask import Flask, jsonify
from flask_cors import CORS

# define some functions

# get brand suggestions for one brand
def get_similar_brands(brand_id: int):
    return mocked_brand_suggestions[str(brand_id)]

# get information about one brand
def get_brand_info(brand_id: int):
    return mocked_brand_infos[str(brand_id)]

# get all brand ids with available suggestions in brands.json
def get_all_brand_ids() -> List[int]:
    brand_id_list = []
    for brand_id in mocked_brand_suggestions:
        brand_id_list.append(int(brand_id))
    return brand_id_list

# get content of brands.json
def get_all_brands():
    return mocked_brand_suggestions

app = Flask(__name__)
CORS(app)

# define some api endpoints

# get brand recommendations
@app.route('/brands/<int:brand_id>/similar')
def similar_brands(brand_id: int):
    try:
        return jsonify(get_similar_brands(brand_id))
    except KeyError:
        return jsonify(error=404,
                       message="The brand is not found in the test index")

# get all available brands with recommendations
@app.route('/brands')
def all_brands():
    try:
        return jsonify(get_all_brands())
    except KeyError:
        return jsonify(error=404,
                       message="No contents are found")

# get information about one brand
@app.route('/brandinfo/<int:brand_id>')
def brand_info(brand_id: int):
    try:
        return jsonify(get_brand_info(brand_id))
    except KeyError:
        return jsonify(error=404,
                       message="No info available for brand")

# save the rating for one recommendation
@app.route('/saverating/<int:brand_id>/<int:rating>')
def save_rating(brand_id: int, rating: int):
    try:
        mocked_brand_suggestions[str(brand_id)]['rating'] = str(rating)
        with open('brands.json', 'w') as outfile:
            json.dump(mocked_brand_suggestions, outfile)
        return jsonify(mocked_brand_suggestions[str(brand_id)])
    except KeyError:
        return jsonify(error=404,
                       message="could not save the rating")

if __name__ == '__main__':
    with open('brands.json') as jf:
        mocked_brand_suggestions = json.load(jf)
    with open('brand-info.json') as jf:
        mocked_brand_infos = json.load(jf)

    app.run(host='0.0.0.0')
