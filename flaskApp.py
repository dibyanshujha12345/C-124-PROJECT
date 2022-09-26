from flask import Flask,jsonify,request
app=Flask(__name__)

{"data":[
    {
        "Contact":"6295036487",
        "Name":"xyz",
        "done":False,
        "id":1

    },

    {
        "Contact":"6294046234",
        "Name":"mummiiieeee",
        "done":False,
        "id":2
    }
]}

@app.route("/")
def hello_world():
    return "hello_world"

@app.route("/add-data",methods=["POST"])
def add_task():
    # return "hello_world"
      if not request.json:

        return jsonify({
        "status":"error",
        "message":"please provide the data"
        },400)

      Contacts = {
        'id': tasks['id'] + 1, 
        'title': request.json['title'],
        'description': request.json.get('description',""), 
        'done': False 
        } 
      tasks.append(task)
      return jsonify({ 
        "status":"success", 
        "message": "Task added succesfully!"
       })  


@app.route("/get-data")
def get_task(): 
    return jsonify({ 
        "data" : tasks 
        })

if(__name__=="__main__"):
    app.run(debug=True)

