from flask import Flask, request
from db import stores
import uuid

app = Flask(__name__)

@app.get("/all_stores")
def all_stores():
    return stores

@app.post("/add_stores")
def add_stores():
    json_body = request.get_json()
    store_id = uuid.uuid4().hex
    store_name = {"id" : store_id, "name" : json_body["name"]}
    stores[store_id] = store_name
    return stores

@app.put("/update_store/<id>")
def update_store(id):
    json_body = request.get_json()
    stores[id]["name"] = json_body["name"]
    return stores[id]

@app.delete("/delete_store/<id>")
def delete_store(id):
    if id in stores:
        stores.pop(id)
        return ("deleted")
    else:
        return ("store not found")

if __name__ == "__main__":
    app.run(debug=True)