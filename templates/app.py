from flask import Flask, render_template, url_for

app = Flask(__name__)


jobs = [
    {
        'id': 1,
        'title': 'Data Scientist',
        'location': 'Nairobi'
    },
    {
        'id': 1,
        'title': 'Data Scientist',
        'location': 'Nairobi'
    },
    {
        'id': 1,
        'title': 'Data Scientist',
        'location': 'Nairobi'
    },
    {
        'id': 1,
        'title': 'Data Scientist',
        'location': 'Nairobi'
    },
]


@app.route('/')
def home():
    banner_img_url = url_for('static', filename='banner.jpg')
    return render_template('home.html', banner_img_url=banner_img_url, jobs=jobs)


if __name__ == "__main__":
    app.run(debug=True)
