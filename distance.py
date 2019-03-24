# distance.py
# Author: Kevin Chu
# Last Modified: 3/24/19


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

  a = r["a"]
  b = r["b"]

  dist = ((a[0] - b[0])**2 + (a[1] - b[1])**2)**(1/2)
  distance = {"distance": dist, "a": r["a"], "b": r["b"]}

  return jsonify(distance)


if __name__ == '__main__':
  app.run()
