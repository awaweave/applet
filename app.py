from flask import Flask, render_template, request
from models import User,db

app = Flask(__name__, static_url_path='/')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weave.db'
db.init_app(app)

@app.route('/talk', methods=["GET", "POST"])
def talk():
    for a in User.query.all():
        print(a.name)

    if request.method == "GET":
        return render_template("talk_view.html")
    else:
        return request.form["mytext"]



if __name__ == "__main__":
    app.run()

