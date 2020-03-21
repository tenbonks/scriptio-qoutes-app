import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# set config variables for mongodb connection
app.config["MONGO_DBNAME"] = "scriptio"
app.config["MONGO_URI"] = os.environ.get("MONGODB_URI")

mongo = PyMongo(app)

@app.route("/")
@app.route("/get_qoutes")
def get_qoutes():
     return render_template("qoutes.html", posts=mongo.db.posts.find())

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=(os.environ.get("PORT")),
    debug=True)