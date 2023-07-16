from app import app
from model.user_model import user_model
from flask import request, send_file
import os
from datetime import datetime
obj = user_model()

@app.route("/user/getall")
def user_getall_controller():
    return obj.user_getall_model()

@app.route("/user/addone", methods=['POST'])
def user_addone_controller():
    return obj.user_addone_model(request.form)

@app.route("/user/update/<int:id>", methods=['PUT'])
def user_update_controller(id):
    return obj.user_update_model(request.form,id)

@app.route("/user/delete/<int:id>", methods=['DELETE'])
def user_delete_controller(id):
    return obj.user_delete_model(id)

@app.route("/user/patch/<int:id>", methods=['PATCH'])
def user_patch_controller(id):
    return obj.user_patch_model(request.form, id)

@app.route("/user/getall/limit/<int:limit>/page/<int:page>", methods=['GET'])
def user_pagination_controller(limit, page):
    return obj.user_pagination_model(limit, page)

@app.route("/user/<uid>/avatar/upload", methods=["PATCH"])
def upload_avatar(uid):
    file = request.files['avatar']
    new_filename =  str(datetime.now().timestamp()).replace(".", "") # Generating unique name for the file
    split_filename = file.filename.split(".") # Spliting ORIGINAL filename to seperate extenstion
    ext_pos = len(split_filename)-1 # Canlculating last index of the list got by splitting the filname
    ext = split_filename[ext_pos] # Using last index to get the file extension
    db_path = f"uploads/{new_filename}.{ext}"
    file.save(f"uploads/{new_filename}.{ext}")
    return obj.upload_avatar_model(uid, db_path)

@app.route("/user/avatar/<uid>", methods=["GET"])
def get_avatar(uid):
    data = obj.get_avatar_path_model(uid)
    root_dir = os.path.dirname(app.instance_path)
    return send_file(f"{root_dir}{data['payload'][0]['avatar']}")