"""
This python module creates a personal web api using the Flask framework
"""
from flask import Flask, jsonify

app = Flask(__name__)

## two pages for the API
# 1) Home page with the documentation of our API
@app.route('/')
def home():
    return '<h1>Currrency Rate API</h1> <p>Example URL: /api/v1/usd-eur</p>'

def get_currency_rate(in_cur, out_cur):
    url=f'https://www.x-rates.com/calculator/?from={in_cur}&to={out_cur}&amount=1'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    rate = soup.find(id="content").find("div", class_="ccOutputBx").find("span",class_="ccOutputRslt")
    rate = rate.text
    rate = float(rate.split(" ")[0])
    return rate

@app.route('/api/v1/<in_cur>-<out_cur>')
def api(in_cur, out_cur):
    rate = get_currency_rate(in_cur, out_cur)
    result_dictionary = {'input_currency':in_cur, 'output_currency':out_cur, 'rate':rate}
    return jsonify(result_dictionary)

app.debug = True

app.run()