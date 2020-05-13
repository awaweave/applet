from flask import Flask, render_template, request
from models import User,db

app = Flask(__name__, static_url_path='/')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weave.db'
db.init_app(app)

@app.route('/talk', methods=["GET", "POST"])
def talk():

    if request.method == "POST":
        return request.form["mytext"]
    else:
        return render_template("talk_view.html")

if __name__ == "__main__":
    app.run()

