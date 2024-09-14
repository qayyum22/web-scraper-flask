from flask import Flask, request, jsonify, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hi')
def greet():
    return "Hi, How are you?"

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form.get('url')
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.prettify()
        # Here you would typically parse the soup to extract data
        # For simplicity, let's just return the title of the page
        title = soup.title.string if soup.title else "No title found"
        return jsonify({"title": title})
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
    