from api import get_result, currencies
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__, static_folder='static')
bootstrap = Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html', currencies=currencies)
    if request.method == "POST":
        from_currency = request.form['fromCurrency']
        to_currency = request.form['toCurrency']
        amount = float(request.form['amount'])
        result = get_result(from_currency, to_currency, amount)
        return render_template('index.html', currencies=currencies, context=result)


if __name__ == '__main__':
    app.run()



















