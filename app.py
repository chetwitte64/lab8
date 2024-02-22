from flask import Flask, request, jsonify
from service import ToDoService
from service import Schema
import json

app = Flask(__name__)
@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = "*"
    response.headers['Access-Control-Allow-Headers'] =  "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods']=  "POST, GET, PUT, DELETE, OPTIONS"
    return response

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/GetTickets", methods=["GET"])
def get_all_tickets():
    return jsonify(ToDoService().list())

@app.route("/GetTickets/<limit>", methods=["GET"])
def get_select_tickets(limit):
    return jsonify(ToDoService().select_list(limit))

@app.route("/GetTicket/<id>", methods=["GET"])
def get_ticket(id):
    return jsonify(ToDoService().select_ticket(id))

@app.route("/CreateTicket", methods=["POST"])
def create_ticket():
    return jsonify(ToDoService().create(request.get_json()))

@app.route("/MarkComplete/<id>", methods=["PUT"])
def mark_complete(id):
    return jsonify(ToDoService().update(id))

@app.route("/DeleteTicket/<id>", methods=["DELETE"])
def delete_ticket(id):
    return jsonify(ToDoService().delete(id))

if __name__ == "__main__":
    Schema()
    app.run(debug=True, host='127.0.0.1', port=5000)
