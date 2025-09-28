from requests import get
from flask import Flask, render_template
app = Flask(__name__)

all_data = get(f"https://api.npoint.io/c790b4d5cab58020d391")
all_data.raise_for_status()
all_data = all_data.json()

@app.route('/')
def home():
    return render_template("index.html", data = all_data)

@app.route('/blog/<id>')
def read_post(id):
    title = all_data[int(id) - 1]['title']
    subtitle = all_data[int(id) - 1]['subtitle']
    body = all_data[int(id) - 1]['body']
    return render_template('post.html', id=id, title=title, subtitle=subtitle, body=body)

if __name__ == "__main__":
    app.run(debug=True)
