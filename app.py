import os
from flask import Flask, render_template, redirect, request, url_for, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# set config variables for mongodb connection
app.config["MONGO_DBNAME"] = "scriptio"
app.config["MONGO_URI"] = os.environ.get("MONGODB_URI")

# mongo instance, that will use config vars above
mongo = PyMongo(app)

# this route is for the homepage, its called get_quotes because thats the main function of the page
@app.route("/")
@app.route("/get_quotes")
def get_quotes():

    quotes = mongo.db.posts

    offset = int(request.args["offset"])
    limit = int(request.args["limit"])

    starting_id = quotes.find().sort("_id", -1)
    last_id = starting_id[offset]["_id"] 

    total_quotes = quotes.count()
    sort_quotes = quotes.find({"_id" : {"$lte" : last_id}}).sort("_id", -1).limit(limit)
    

    output = []

    for i in sort_quotes:
        output.append({"_id" : i["_id"],"quote" : i["quote"], "said_by": i["said_by"], "category_name": i["category_name"]})
        
    next_url = "/?limit=" + str(limit) + "&offset=" + str(offset + limit)
    prev_url = "/?limit=" + str(limit) + "&offset=" + str(offset - limit)

    
    
    # Im sorting by id, and descending, this will show posts newest first, due to _id being incremented for each post
    return render_template("quotes.html", posts=output, total_quotes=total_quotes)

@app.route("/post_quote")
def post_quote():
        return render_template("post_quote.html", categories=mongo.db.categories.find())


# The function below will be called when submitting the form in post_quote
@app.route("/insert_quote", methods=["POST"])
def insert_quote():
    # target mongoDB posts, insert data from form into target
    quotes = mongo.db.posts
    quotes.insert_one(request.form.to_dict())
    # redirect to get quotes, which will render get_quotes.html
    return redirect(url_for("get_quotes"))


# this route will be called when a user want to edit a quote
@app.route('/edit_quote/<quote_id>')
def edit_quote(quote_id):
    # set a var to store the target post, targeted by _id
    the_quote = mongo.db.posts.find_one({"_id": ObjectId(quote_id)})
    # used to display all categories on the select element
    all_categories = mongo.db.categories.find()
    return render_template("edit_quote.html", quote=the_quote, categories=all_categories)


# this route will be called when submitting edit_quote form 
@app.route("/update_quote/<quote_id>", methods=["POST"])
def update_quote(quote_id):
    quotes = mongo.db.posts
    # use update to first target the document which has the same "_id", then update the fields with supplied values from the form
    quotes.update( {"_id": ObjectId(quote_id)},
    {
        "quote" : request.form.get("quote"),
        "said_by" : request.form.get("said_by"),
        "category_name" : request.form.get("category_name")
    })
    return redirect(url_for("get_quotes"))


# this route will be called when firing delete button on edit_quote.html
@app.route("/delete_quote/<quote_id>")
def delete_quote(quote_id):
    # remove post with matching id, then redirect to get_quotes
    mongo.db.posts.remove({"_id": ObjectId(quote_id)})
    return redirect(url_for("get_quotes"))

@app.route("/get_categories")
def get_categories():
    return render_template("get_categories.html", categories=mongo.db.categories.find())


# ROUTE FOR FILTERING QUOTES BY "CATEGORY"
@app.route("/filter_quotes/<category_name>")
def filter_quotes(category_name):
    quotes = mongo.db.posts
    res = quotes.find({"category_name": category_name})
    total_quotes = res.count()
    
    return render_template("filter_quotes.html", posts=res, total_quotes_count=total_quotes,  total_quotes=category_name + " | " + str(total_quotes) + " quotes", page_title="Filtering quotes by category")
    

# ROUTE FOR FILTERING QUOTES BY "SAID_BY"
@app.route("/quotes_by/<said_by>")
def quotes_by(said_by):
    quotes = mongo.db.posts
    res = quotes.find({"said_by": said_by})
    total_quotes = res.count()
    print(total_quotes)
    return render_template("quotes_by.html", posts=res, total_quotes=said_by + " | " + str(total_quotes) + " quotes", page_title="Filtering quotes by name")

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=(os.environ.get("PORT")),
    debug=True)