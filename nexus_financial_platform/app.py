from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/risk')
def risk():
    return render_template('risk.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/market_data')
def market_data():
    return render_template('market_data.html')

@app.route('/performance')
def performance():
    return render_template('performance.html')

@app.route('/ml')
def ml():
    return render_template('ml.html')

@app.route('/compliance')
def compliance():
    return render_template('compliance.html')

if __name__ == '__main__':
    app.run(debug=True)
