from flask import Flask,jsonify,request
app=Flask(__name__)
tasks=[
    {
        "Contact":1,
        "Name":"Raju",
        "id":"1",
        "done":False
    },{
        "Contact":2,
        "Name":"",
        "id":"2",
        "done":False
    }
]
@app.route("/")
@app.route("/get-data")
@app.route("/send-data",methods=["POST"])
def send_task():
    if not request.json:
        task={
            "id":tasks[-1]["id"]+1,
        "title":request.json["title"],
        "description":request.json["description"],
        "done":False
        }
        tasks.append(task)
        return jsonify({
            "status":"success"
        })
def get_task():
    return jsonify({
        "data":tasks
    })
def hello_world():
    return "helloworld"

if(__name__=="__main__"):
    app.run(debug=True)