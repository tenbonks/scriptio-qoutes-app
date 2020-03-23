import os, bcrypt
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

@app.route("/post_qoute")
def post_qoute():
        return render_template("post_qoute.html", categories=mongo.db.categories.find())

# The function below will be called when submitting the form in post_qoute
@app.route("/insert_qoute", methods=["POST"])
def insert_qoute():
    qoutes = mongo.db.posts
    qoutes.insert_one(request.form.to_dict())
    # redirect to get qoutes, which will render get_qoutes.html
    return redirect(url_for("get_qoutes"))

@app.route('/edit_qoute/<qoute_id>')
def edit_qoute(qoute_id):
    the_qoute = mongo.db.posts.find_one({"_id": ObjectId(qoute_id)})
    all_categories = mongo.db.categories.find()
    return render_template("edit_qoute.html", qoute=the_qoute, categories=all_categories)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=(os.environ.get("PORT")),
    debug=True)