from app import app, db
from app.models import User 
import pytest

def test_No_User():
    u = User.query.filter_by(username = "Not_Existing_User").first(); 
    
    assert (u == None)

def test_Existing_User():
    u = User.query.filter_by(email = "test@email.com").first(); 

    assert (u.username == "Test_Dude1"); 

def test_creating_User():
    u = User(email= "python_test@email.com", username = "python_test_user", password = "abcd"); 
    
    