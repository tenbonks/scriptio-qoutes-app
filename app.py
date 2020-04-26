import os
from flask import Flask, render_template, redirect, request, url_for, jsonify
from flask_pymongo import PyMongo
from flask_paginate import Pagination, get_page_parameter, get_page_args
from bson.objectid import ObjectId

app = Flask(__name__)

# set config variables for mongodb connection
app.config["MONGO_DBNAME"] = "scriptio"
#  MONGDB_URI is set within heroku config vars
app.config["MONGO_URI"] = os.environ.get("MONGODB_URI")

# mongo instance, that will use config vars above
mongo = PyMongo(app)

#  the three functions below are very similar, but they differ in what they query, the querys are sorted descending by _id.
# this one below is for all quotes, used in the homepage
def get_all_quotes_for_paginate(offset=0, per_page=10):
    thequotes = mongo.db.posts.find().sort("_id", -1)
    return thequotes[offset: offset + per_page]

# this function finds quotes by "said_by", this function is called when looking up all quotes said by one person
def get_quotes_said_by_for_paginate(offset=0, per_page=10, said_by=""):
    thequotes = mongo.db.posts.find({"said_by": said_by}).sort("_id", -1)
    return thequotes[offset: offset + per_page]

#  this function will find quotes by category, and will be called when filtering by category
def get_quotes_in_cat_for_paginate(offset=0, per_page=10, category_name=""):
    thequotes = mongo.db.posts.find({"category_name": category_name}).sort("_id", -1)
    return thequotes[offset: offset + per_page]


@app.route("/")
@app.route("/get_quotes")
def get_quotes():

    total_quotes = mongo.db.posts.find().count()

    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
                                        
    paginated_quotes = get_all_quotes_for_paginate(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total_quotes, record_name='quotes')

    return render_template("quotes.html", posts=paginated_quotes, total_quotes=total_quotes, pagination=pagination)

@app.route("/post_quote")
def post_quote():
        return render_template("post_quote.html", categories=mongo.db.categories.find())



@app.route("/insert_quote", methods=["POST"])
def insert_quote():
    
    quotes = mongo.db.posts
    quotes.insert_one(request.form.to_dict())
    
    return redirect(url_for("get_quotes"))


@app.route('/edit_quote/<quote_id>')
def edit_quote(quote_id):
    # target the single post, find it by the _id provided.
    the_quote = mongo.db.posts.find_one({"_id": ObjectId(quote_id)})
    # code below is for the select element
    all_categories = mongo.db.categories.find()
    return render_template("edit_quote.html", quote=the_quote, categories=all_categories)


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


@app.route("/delete_quote/<quote_id>")
def delete_quote(quote_id):
    mongo.db.posts.remove({"_id": ObjectId(quote_id)})
    return redirect(url_for("get_quotes"))

@app.route("/get_categories")
def get_categories():
    return render_template("get_categories.html", categories=mongo.db.categories.find())


@app.route("/filter_quotes/<category_name>")
def filter_quotes(category_name):
    total_quotes = mongo.db.posts.find({"category_name": category_name}).count()
    
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')

    paginated_quotes=get_quotes_in_cat_for_paginate(offset=offset, per_page=per_page, category_name=category_name)
    pagination = Pagination(page=page, per_page=per_page, total=total_quotes, record_name='quotes')
    
    return render_template("filter_quotes.html", posts=paginated_quotes, total_quotes_count=total_quotes,pagination=pagination,  category_name=category_name, page_title="Filtering quotes by category")
    

@app.route("/quotes_by/<said_by>")
def quotes_by(said_by):
    total_quotes = mongo.db.posts.find({"said_by": said_by}).count()

    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')

    paginated_quotes=get_quotes_said_by_for_paginate(offset=offset, per_page=per_page, said_by=said_by)

    pagination = Pagination(page=page, per_page=per_page, total=total_quotes, record_name='quotes')

    return render_template("quotes_by.html", posts=paginated_quotes, pagination=pagination, said_by=said_by, page_title="Filtering quotes by name")

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=(os.environ.get("PORT")),
    debug=False)