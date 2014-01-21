from flask import Flask, render_template
from sfapp.blueprint import sfapp

app = Flask(__name__)
app.register_blueprint(sfapp)


@app.route('/', methods=['GET'])
def index():
    return render_template('sfapp/flask/_demo.html')


if __name__ == '__main__':
    app.run(debug=True, port=8000)
