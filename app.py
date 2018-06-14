from flask import Flask, render_template, request, jsonify
from os import environ

app = Flask(__name__)
from subarrays import subarrays, parse_string


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


def create_app():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    if environ.get('ENV') == 'HEROKU':
        app.run(debug=False)
    else:
        app.run()


if __name__ == '__main__':
    create_app()

