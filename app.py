from flask import Flask, request
from db import stores

app = Flask(__name__)

@app.get("/all_stores")
def all_stores():
    return stores

@app.post("/add_stores")
def add_stores():
    json_body = request.get_json()
    stores["name"] = json_body["name"]
    return stores

@app.put("/update_store")
def update_store():
    json_body = request.get_json()
    


if __name__ == "__main__":
    app.run(debug=True)