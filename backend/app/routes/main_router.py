from flask import Blueprint, jsonify

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/main', methods=['GET'])
def main():
    data = {'test': '1', 'test2':'2'}

    return jsonify(data)