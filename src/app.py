"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person


app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)


# create the jackson family object
jackson_family = FamilyStructure("Jackson")


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/members', methods=['GET'])
def handle_get_all_members():

    # this is how you can use the Family datastructure by calling its methods
    family_members = jackson_family.get_all_members()

    return jsonify(family_members), 200


@app.route('/member', methods=['POST'])
def handle_add_member():

    # this is how you can use the Family datastructure by calling its methods
    response_body = request.get_json() # captura los datos introducidos por el usuario
    new_member = jackson_family.add_member(response_body)
    
    return jsonify({
            "msg": "Familiar añadido",
            "member": new_member
        }), 200 # "Familiar añadido"


@app.route('/member/<int:id>', methods=['GET'])
def handle_get_single_member(id):
    # obtener el member que cumpla con el id indicado
    single_member = jackson_family.get_member(id)
    # retornar jsonify -> correcto
    return jsonify(single_member), 200


@app.route('/member/<int:id>', methods=['DELETE'])
def handle_delete_single_member(id):
    # eliminar el member que cumpla con el id indicado
    single_member = jackson_family.delete_member(id)
    # retornar jsonify -> correcto
    return jsonify({
        "done": True,
        "msg": "Familiar añadido",
        "member": single_member
    }), 200


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
