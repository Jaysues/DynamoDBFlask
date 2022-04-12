from flask import Flask, jsonify, render_template, request
import aws_controller
import json


app = Flask(__name__)


@app.route('/')
def index():
    data = aws_controller.get_items()
    return render_template('index.html', data=data)


@app.route('/new-booking', methods=["POST"])
def new_booking():
    userName = request.form.get("userName")
    officeLabel = request.form.get("officeLabel")
    createdAt = request.form.get("createdAt")
    numDesks = request.form.get("numDesks")
    aws_controller.put_item(userName, officeLabel, createdAt, numDesks)
    data = aws_controller.get_items()
    return render_template('index.html', data=data)
    

if __name__ == '__main__':
    app.run()