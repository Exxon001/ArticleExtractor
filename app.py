from flask import Flask, render_template, request
import requests
from ArticalExtractor import extract

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        try:
            content = extract(url)
            return render_template('index.html', content=content)
        except requests.exceptions.RequestException as e:
            return render_template('index.html', error=str(e))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
