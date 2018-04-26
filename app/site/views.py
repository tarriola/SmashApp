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

@mod.route('/<character_name>', methods=['GET'])
def showCharacter(character_name):
    character = Character.query.filter_by(name=character_name).first()
    print(character_name)
    return render_template('show.html', character = character)

@mod.route('/add', methods=['GET', 'POST'])
def addCharacter():
    if request.method == "POST":
        data = request.get_json()
        form = request.form
        print(form['name'] + form['info'])
        if data:
            charName = data['name']
            charInfo = data['info']
        elif form:
            charName = form['name']
            charInfo = form['info']

        # check if character exists in the database
        name = Character.query.filter_by(name=charName).first()
        if not name:
            character = Character(charName, charInfo)
            db.session.add(character)
            db.session.commit()

            return redirect(url_for('.homepage'))

    return render_template('add.html')


@mod.route('/delete/', methods=['GET','POST'])
def delete():
    print(request.method)
    if request.method == "POST":
        form = request.form

        if form:
            name = form['name']

            character = Character.query.filter_by(name=name).first()
            code = {'status' : 'Character doesn\'t exist'}
            if character:
                db.session.delete(character)
                db.session.commit()
                # code['status'] = 'Deleted Character'
                # print(code)
                return redirect(url_for('.homepage'))

    return render_template('delete.html')

@mod.route('/delete/<character_name>', methods=['DELETE'])
def deleteCharacter(character_name):
    character = Character.query.filter_by(name=character_name).first()
    code = {'status' : 'Character doesn\'t exist'}
    if character:
        db.session.delete(character)
        db.session.commit()
        code['status'] = 'Deleted Character'
        print(code)
        return redirect(url_for('.homepage'))
    return jsonify(code)

# @mod.route('/edit', methods=['POST'])
# def edit():

@mod.route('/edit', methods=['POST', 'PUT'])
def editCharacter():
    print(request.method)
    data = request.get_json()
    if request.method == "POST":
        name = request.form['name']
        character = Character.query.filter_by(name=name).first()
        character.info = request.form['info']
        db.session.commit()
    elif data:
        name = data['name']
        character = Character.query.filter_by(name=name).first()
        character.info = data['info']
        db.session.commit()

    return redirect(url_for('.homepage'))


# @mod.route('/edit/<character_name>', methods=['POST', 'PUT'])
# def editCharacter(character_name):
#     print(request.method)
#     character = Character.query.filter_by(name=character_name).first()
#     data = request.get_json()
#     if request.method == "POST":
#         character.info = request.form['info']
#         db.session.commit()
#     elif data:
#         character.info = data['info']
#         db.session.commit()
#     # code = {'status' : 'Character doesn\'t exist'}
#     # print(data['info'])
#     # if character:
#     #     code['status'] = 'Character Updated'
#     #     print(code)
#     #     return redirect(url_for('.homepage'))
#     # return jsonify(code)
#     return redirect(url_for('.homepage'))
