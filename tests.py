from app import app, db
from app.models import User 

def test_No_User():
    print("Search User Database for 'Not_Existing_User'")
    u = User.query.filter_by(username = "Not_Existing_User").first(); 
    
    assert (u == None)

if __name__ == "__main__":
    print("Starting Tests")

    test_No_User()

    print("Tests Finished")