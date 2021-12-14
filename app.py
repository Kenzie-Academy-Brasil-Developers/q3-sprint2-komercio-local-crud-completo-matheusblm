# Seu código aqui
from flask import Flask, jsonify, request

app = Flask(__name__)

produtos = [
    {"id": 1, "name": "sabonete", "price": 5.99},
    {"id": 2, "name": "perfume", "price": 39.90},
    {"id": 3, "name": "tapete", "price": 10.30},
    {"id": 4, "name": "tunica", "price": 19.29},
    {"id": 5, "name": "chuveiro", "price": 119.19},
    {"id": 6, "name": "arroz", "price": 30.10},
    {"id": 7, "name": "oleo de cozinha", "price": 11.15},
    {"id": 8, "name": "carne moida", "price": 39.90},
    {"id": 9, "name": "bola", "price": 25.99},
    {"id": 10, "name": "cantil", "price": 55.99},
    {"id": 11, "name": "copo", "price": 5.99},
    {"id": 12, "name": "panela", "price": 25.99},
    {"id": 13, "name": "prato", "price": 10.99},
    {"id": 14, "name": "açucar", "price": 7.99},
    {"id": 15, "name": "sal", "price": 5.99},
    {"id": 16, "name": "pipoca", "price": 3.14},
    {"id": 17, "name": "sabonete", "price": 5.99},
    {"id": 18, "name": "miojo", "price": 2.39},
    {"id": 19, "name": "alface", "price": 3.99},
    {"id": 20, "name": "tomate", "price": 9.99},
    {"id": 21, "name": "macarrao", "price": 6.40},
    {"id": 22, "name": "mesa", "price": 115.99},
    {"id": 23, "name": "cadeira gamer", "price": 445.99},
    {"id": 24, "name": "mouse gamer", "price": 215.99},
    {"id": 25, "name": "tv", "price": 995.99},
    {"id": 26, "name": "liquidificador", "price": 65.99},
    {"id": 27, "name": "furadeira", "price": 99.15},
    {"id": 28, "name": "ferro de passar", "price": 55.80},
    {"id": 29, "name": "coberta", "price": 55.99},
    {"id": 30, "name": "sofa", "price": 600.15}
]

@app.get("/products")
def list_products():
    return jsonify(produtos), 200

@app.get("/products/<product_id>")
def get(product_id: int):
    for item in produtos:
        if item.get("id") == int(product_id):
            return jsonify(item), 200
    return "Nao encontrado", 200

@app.post("/products")
def create():
    data = request.get_json()
    id = produtos[-1].get("id") + 1
    name = data.get("name")
    price = data.get("price")
    new_item = {"id": id, "name": name, "price": price}
    produtos.append(new_item)
    return jsonify(new_item), 201

@app.route("/products/<product_id>", methods=['PATCH', 'PUT'])
def update(product_id: int):
    data = request.get_json()
    for item in produtos:
        if item.get("id") == int(product_id):
            item = data
    return "", 204

@app.delete("/products/<product_id>")
def delete(product_id: int):
    for item in produtos:
        if item.get("id") == int(product_id):
            produtos.remove(item)
    return "" , 204