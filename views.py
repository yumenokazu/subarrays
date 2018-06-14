from subarrays import subarrays, parse_string
from flask import render_template, request, jsonify
from app import app


@app.route('/')
@app.route('/index.html')
def index():
    return render_template("index.html")


@app.route('/', methods=['POST'])
@app.route('/index.html', methods=['POST'])
def get_subarrays():

    numbers = request.form['numbers']
    target = request.form['target']
    try:
        numbers=parse_string(numbers)
        target=int(target)
        result = subarrays(numbers, target)
        return jsonify({'status': 'success',
                        'data': render_template("list_items.html", object_list=result)})
    except ValueError as e:
        return jsonify({'status': 'fail', 'data': e})