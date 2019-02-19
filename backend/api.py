"""
Simple API to return similar brands.
This is just a prototype, so no worries about the details of the file.
"""

import json
from typing import List
from flask import Flask, jsonify
from flask_cors import CORS

# define some functions 
def get_similar_brands(brand_id: int) -> List[int]:
    """Run a `complicated` ML model to suggest brands"""
    return mocked_brand_suggestions[str(brand_id)]

def get_all_brand_ids():
    """return all brand ids inside the brands.json"""
    brand_id_list = []
    for brand_id in mocked_brand_suggestions:
        brand_id_list.append(int(brand_id))
    return brand_id_list

def get_all_brands():
    """return all brand data"""
    return mocked_brand_suggestions

app = Flask(__name__)
CORS(app)

# define some api endpoints
@app.route('/brands/<int:brand_id>/similar')
def similar_brands(brand_id: int):
    """Return similar brands."""
    try:
        return jsonify(get_similar_brands(brand_id))
    except KeyError:
        return jsonify(error=404,
                       message="The brand is not found in the test index")

@app.route('/brands')
def all_brands():
    """Return all available brands."""
    try:
        return jsonify(get_all_brands())
    except KeyError:
        return jsonify(error=404,
                       message="No contents are found")

if __name__ == '__main__':
    with open('brands.json') as jf:
        mocked_brand_suggestions = json.load(jf)


    app.run(host='0.0.0.0')
