import pytest
import os

from app.models import User, Ingredients, recipeIng, recipes, Pantry

def test_No_User(client, db):
    
    u = User.query.filter_by(username = "Not_Existing_User").first()
    
    assert (u == None)

def test_Existing_User(client, db):

    user = User(username = "Test_Dude1", email = "test2@email.com")
    db.session.add(user)
    db.session.commit()
    u = User.query.filter_by(email = "test2@email.com").first() 

    assert u.username == user.username

def test_ingredient_search(db):
    item = Ingredients(name = "Salt", category = "Spice")
    db.session.add(item)
    db.session.commit()
    
    item_id = Ingredients.get_id(item.category, item.name)

    item_name = Ingredients.get_ingredient_name(item_id)
    assert item.name == item_name

def test_invalid_ingredient_search(db):
    item = Ingredients(name = "Salt", category = "Spice")
    db.session.add(item)
    db.session.commit()
    
    item_id = Ingredients.get_id(item.category, item.name)

    item_name = Ingredients.get_ingredient_name(item_id)
    assert item.name == item_name

    item_name = Ingredients.get_ingredient_name("Invalid Name")
    assert item_name is None

def test_login_page(client):
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Email' in response.data  
    assert b'Password' in response.data

def test_home_page(client):
    response = client.get('/home')
    assert response.status_code == 200

def test_registration(client, db):
    new_user = User(username = "new_user", email = "new_user@email.com")
    password = "test_password"
    response = client.post('/register', data = dict(form ="", username = new_user.username, 
        email = new_user.email, password= password, confirm_password = password), follow_redirects = True )

    u = User.query.filter_by(email = "new_user@email.com").first()
    assert response.status_code == 200 
    assert u.username == new_user.username
    assert u.email == new_user.email 

def test_logging_in(client, db): 
    new_user = User(username = "new_user", email = "new_user@email.com")
    password = "test_password"
    response = client.post('/register', data = dict(form ="", username = new_user.username, 
        email = new_user.email, password= password, confirm_password = password), follow_redirects = True )

    u = User.query.filter_by(email = "new_user@email.com").first()
    assert response.status_code == 200 
    assert u.username == new_user.username
    assert u.email == new_user.email

    response = client.post('/login', data = dict(email = new_user.email, password=password), follow_redirects = True)

    assert response.status_code == 200

    resposne = client.get('/ingredients')
    assert response.status_code == 200


    
    