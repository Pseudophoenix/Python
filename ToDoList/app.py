from flask import Flask, render_template
from flask import Response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///todo.db"
db=SQLAlchemy(app)

class Todo(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    Title=db.Column(db.String(200),nullable=False)
    desc=db.Column(db.String(500),nullable=False)
    time=db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.Title}"
# python 
# from app import db, app
# app.app_context().push()
# db.create_all()
@app.route("/")
def hello_world():
    todo=Todo(Title="Bicycle",desc="Go to Track for bicycling")
    db.session.add(todo)
    db.session.commit()
    return render_template("index.html")


@app.route("/welcome")
def home():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)