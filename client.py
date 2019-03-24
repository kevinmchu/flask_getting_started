# client.py
# Author: Kevin Chu
# Last Modified: 3/24/19

import requests


def get_name():
    r = requests.get("http://127.0.0.1:5000/name")
    print(r.json())
    
    return


def get_hello_name():
    r = requests.get("http://127.0.0.1:5000/hello/Kevin")
    print(r.json())

    return


def calculate_distance():
    coordinates = {"a": [2, 4], "b": [5, 6]}

    r = requests.post("http://127.0.0.1:5000/distance", json=coordinates)
    print("'r' = {}".format(r))
    print("'r.json() = {}".format(r.json()))

    return


if __name__ == "__main__":
    get_name()
    get_hello_name()
    calculate_distance()
