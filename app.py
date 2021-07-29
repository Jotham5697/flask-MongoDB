# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask_pymongo import PyMongo


# -- Initialization section --
app = Flask(__name__)

# events = [
#         {"event":"First Day of Classes", "date":"2019-08-21"},
#         {"event":"Winter Break", "date":"2019-12-20"},
#         {"event":"Finals Begin", "date":"2019-12-01"}
#     ]

# name of database
app.config['MONGO_DBNAME'] = 'upperline'

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://Admin:Pazzword5697@cluster0.e7n8a.mongodb.net/upperline?retryWrites=true&w=majority'

mongo = PyMongo(app)

# -- Routes section --
# INDEX

@app.route('/')
@app.route('/index')

def index():
    user = mongo.db.users
    return render_template('index.html', user = user)


# CONNECT TO DB, ADD DATA

@app.route('/add')

def add():
    # connect to the database
    user = mongo.db.users

    # insert new data
    user.insert({'name':'Jotham'})
    

    # return a message to the user
    return "Added User!"


    
@app.route("/event", methods = ["GET","POST"])
def event():
    if request.method == "GET":
        return "<h1>Try Agaian</h1>"
    else:
        user_name = request.form["first_name"]
        user_date = request.form["date"]
        events = mongo.db.events
        events.insert({"first_name" : user_name, "date" : user_date})
    
    # joy = mongo.db.users
    # users = joy.find({"name":"Jotham"})

    # return render_template("/event.html", users = users)

