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
    # target mongoDB posts, insert data from form into target
    qoutes = mongo.db.posts
    qoutes.insert_one(request.form.to_dict())
    # redirect to get qoutes, which will render get_qoutes.html
    return redirect(url_for("get_qoutes"))


# this route will be called when a user want to edit a qoute
@app.route('/edit_qoute/<qoute_id>')
def edit_qoute(qoute_id):
    # set a var to store the target post, targeted by _id
    the_qoute = mongo.db.posts.find_one({"_id": ObjectId(qoute_id)})
    # used to display all categories on the select element
    all_categories = mongo.db.categories.find()
    return render_template("edit_qoute.html", qoute=the_qoute, categories=all_categories)


# this route will be called when submitting edit_qoute form 
@app.route("/update_qoute/<qoute_id>", methods=["POST"])
def update_qoute(qoute_id):
    qoutes = mongo.db.posts
    # use update to first target the document which has the same "_id", then update the fields with supplied values from the form
    qoutes.update( {"_id": ObjectId(qoute_id)},
    {
        "qoute" : request.form.get("qoute"),
        "said_by" : request.form.get("said_by"),
        "category_name" : request.form.get("category_name")
    })
    return redirect(url_for("get_qoutes"))


# this route will be called when firing delete button on edit_qoute.html
@app.route("/delete_qoute/<qoute_id>")
def delete_qoute(qoute_id):
    # remove post with matching id, then redirect to get_qoutes
    mongo.db.posts.remove({"_id": ObjectId(qoute_id)})
    return redirect(url_for("get_qoutes"))

@app.route("/get_categories")
def get_categories():
    return render_template("get_categories.html", categories=mongo.db.categories.find())

@app.route("/filter_qoutes/<category_name>")
def filter_qoutes(category_name):
    qoutes = mongo.db.posts
    return render_template("filter_qoutes.html", posts=qoutes.find({"category_name": category_name}))
    

@app.route("/qoutes_by/<said_by>")
def qoutes_by(said_by):
    qoutes = mongo.db.posts
    return render_template("qoutes_by.html", posts=qoutes.find({"said_by": said_by}), page_title="Filtering qoutes by name : " + said_by)

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=(os.environ.get("PORT")),
    debug=True)