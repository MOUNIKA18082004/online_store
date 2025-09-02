from flask import Flask, request
from flask_jwt_extended import jwt_required, JWTManager, create_access_token, get_jwt
from db import stores, registered_users as users
import uuid

app = Flask(__name__)
jwt = JWTManager(app)
app.config["JWT_SECRET_KEY"] = "123456789"



@app.get("/login")
def login():
    json_body = request.get_json()
    username = json_body["username"] # admin
    password = json_body["password"] # admin@123

    user = users.get(username, None) # {"username":"admin", "password":"admin@123"}

    if not user or user["password"] != password:
        return {"msg":"unauthorized user"}
    
    access_token = create_access_token(identity=username)
    return {"access_token":access_token}        


@app.get("/all_stores")
@jwt_required()
def all_stores():
    jwt_body = get_jwt()
    if jwt_body.get("sub") != "admin":
        return {"msg":"not an admin"}
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