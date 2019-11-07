from app import app, db
from app.models import User 

def test_No_User():
    print("Non-Existing User Test")
    u = User.query.filter_by(username = "Not_Existing_User").first(); 
    
    assert (u == None)

def test_Existing_User():
    print("Existing User Test"); 
    u = User.query.filter_by(email = "test@email.com").first(); 

    assert (u.username == "Test_Dude1"); 

if __name__ == "__main__":
    print("\n___Starting Tests___\n")

    test_No_User()
    test_Existing_User(); 

    print("\n___Tests Finished___\n")