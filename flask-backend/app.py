from Profile import Profile
from flask import Flask, jsonify
import random
from json_data import funny_data
from flask import url_for
from flask import abort
from flask import make_response
from flask import request
from flask_pymongo import PyMongo
import json
from bson import ObjectId
#from PyMongo import Connection



#from json_data import funny_quotes

app=Flask(__name__)


app.config['MONGO_DBNAME'] = 'restdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'
mongo = PyMongo(app)


@app.route("/api/addblogger",methods=["POST"])
def put_data():

    bloggers = mongo.db.bloggers
    #name1 = request.json['name1']
    #distance1 = request.json['distance1']
    # user_id = bloggers.insert({'name1': name1, 'distance1': dist1})
    # new_user = bloggers.find_one({'_id': user_id })
    #output = {'name' : new_user['name1'], 'distance' : new_user['distance1']}
    # print("request is ")
    # print( request.form.to_dict()
    account_dict = request.form.to_dict()

    bloggers.insert_one(account_dict)
    
    return jsonify({'result' :True})


# @app.route('/api/bloggers', methods=['GET'])
# def get_all_bloggers():
#   blogger = mongo.db.bloggers.find()
#   output = []
#   #for s in blogger.find():
#     #output.append({'name' : s['name1'], 'distance' : s['distance1']})
#   return jsonify({'result' : blogger})


# @app.route("/api/data",methods=["GET"])
# def json_data():
#     quotes =  funny_data()  #data.serialize()
#     nr_of_quotes = len(quotes)
#     selected_quote = quotes[0]
#     return jsonify(selected_quote)

@app.route("/api/bloggers/<string:name>",methods=["GET"])
def user_by_name(name):
    user = mongo.db.bloggers.find( { "Name": name } )
    if user:
        
        #print (user.dumps())
        return JSONEncoder().encode(user.next())
    else:
        abort(400)


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)




if __name__ == "__main__":
    app.run(debug=True)

