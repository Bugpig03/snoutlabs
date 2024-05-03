from flask import Flask, render_template
import json
import os

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():

    json_file_path = os.path.join(app.root_path, 'data', 'news.json')

    with open(json_file_path) as f:
        news = json.load(f)
    return render_template('home.html', news=news['articles'])

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

if __name__ == '__main__':
    app.run(port=5001)