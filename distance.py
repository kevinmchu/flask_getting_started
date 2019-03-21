from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/name", methods=["GET"])
def name():
  """
  Returns the name as a json to the caller
  """
  name = {"name": "Kevin"}
  return jsonify(name)
  
@app.route("/hello/<name>", methods=["GET"])
def hello_name(name): # the name variable being passed in here is the string that the client puts in the <name> part of the url
  hello = {"message": "Hello there, {}".format(name)}
  return jsonify(hello)

@app.route("/distance", methods=["POST"])
def distance():
  r = request.get_json()
  coordinates = {"a": [2, 4], "b": [5, 6]}
  dist = sum((r["a"] - r["b"])**(1/2))
  distance = {"distance": dist, "a": [2, 4], "b": [5, 6]}

  return jsonify(distance)
