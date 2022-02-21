from flask import Flask
import requests


def hello(name):
    info = requests.get('http://localhost:5000/hello/'+name)
    return info.text

