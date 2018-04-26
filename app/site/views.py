from flask import Flask, Blueprint, render_template, request, redirect, url_for, session, jsonify, json

# Import the database object from man app module
from app import db

# Import module forms
from app.site.forms import AddForm

# Import module models (Character)
from app.site.models import Character

# Define the blueprint
mod = Blueprint(' ',__name__,
                        template_folder='templates')

@mod.route('/')
def homepage():
    characters = Character.query.all()
    return render_template('home.html', characters = characters)

@mod.route('/add', methods=['GET', 'POST'])
def addCharacter():
    if request.method == "POST":
        data = request.get_json()
        charName = data['name']
        charInfo = data['info']
        name = Character.query.filter_by(name=charName).first()
        if not name:
            character = Character(charName, charInfo)
            db.session.add(character)
            db.session.commit()

            return redirect(url_for('.homepage'))


    return render_template('add.html')

@mod.route('/delete/<character_name>', methods=['DELETE'])
def deleteCharacter(character_name):
    character = Character.query.filter_by(name=character_name).first()
    code = {200 : 'Character does not exist'}
    if character:
        db.session.delete(character)
        db.session.commit()
        code[200] = 'Deleted Character'
    return jsonify(code)

@mod.route('/edit/<character_name>', methods=['PUT'])
def editCharacter(character_name):
    character = Character.query.filter_by(name=character_name).first()
    data = request.get_json()
    print(data['info'])
    if character:
        return 'Character Exists'
    return 'Character does not exist'
