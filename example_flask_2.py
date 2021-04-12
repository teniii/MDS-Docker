from flask import Flask, request
import json
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'
    
@app.route('/hello_iedi')
def hello_iedi():
    return 'Hello iedi'

@app.route("/double/<value>")    
def double_num(value):
    with open("/home/output/test.txt", "a") as f:
        f.write("{} ".format(value))
    print(os.listdir("/home"))
    return str(2*int(value))

@app.route("/get_dict")    
def get_dict():
    my_dict = {"a":1, "b":2}
    return json.dumps(my_dict)
    
    
@app.route("/post_stuff", methods=["GET", "POST"])
def save_new_soldier_info():
    if request.method == "POST":
        info = request.json
        print(info)
        return "stuff has been received"
    else:
        return "This route is for submitting data, please send a POST request with a json"


@app.route("/sum/<value1>/<value2>")    
def double_num(value1, value2):
    with open("/home/output/test.txt", "a") as f:
        f.write("{} + {} =  {}".format(value1, value2, int(value1) + int(value2)))
    print(os.listdir("/home"))
    return str(int(value1) + int(value2))

@app.route("/subtract/<value1>/<value2>")    
def double_num(value1, value2):
    with open("/home/output/test.txt", "a") as f:
        f.write("{} + {} =  {}".format(value1, value2, int(value1) - int(value2)))
    print(os.listdir("/home"))
    return str(int(value1) - int(value2))

@app.route("/multiply/<value1>/<value2>")    
def double_num(value):
    with open("/home/output/test.txt", "a") as f:
        f.write("{} + {} =  {}".format(value1, value2, int(value1) * int(value2)))
    print(os.listdir("/home"))
    return str(int(value1)*int(value2))

@app.route("/divide/<value1>/<value2>")    
def double_num(value):
    with open("/home/output/test.txt", "a") as f:
        f.write("{} + {} =  {}".format(value1, value2, float(value1) / float(value2)))
    print(os.listdir("/home"))
    return str(float(value1)/float(value2))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
