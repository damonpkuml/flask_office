#!/usr/bin/env python
# coding:utf-8

"""
@File :hello.py
@Date :19-6-2

"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello,world!"


@app.route("/user/<username>")
def show_user_profile(username):
    return "User %s" % username


@app.route("/post/<int:post_id>")
def show_post(post_id):
    return "Post %d" % post_id


@app.route("/projects/")
def projects():
    return "The project page"


@app.route("/about")
def about():
    return "The about page"


@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("hello.html", name=name)
