from app import app, db
from app.models import User 

def test_No_User():
    u = User.query.filter_by(username = "Not_Existing_User"); 
    assert (u is None)




if __name__ == "__main__":
    print("Starting Tests")

    test_No_User()