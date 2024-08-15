from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    # Table columns
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __repr__(self) -> str:
        return f"user({self.username}, {self.password})"
    
    
    # Function to create new user entities
    def create(name, passwd) -> bool:
        if (User.isUsernameTaken(name)): return False
        
        db.session.add(User(username=name, password=passwd))
        db.session.commit()
        return True

    # Function to check if username is taken
    def isUsernameTaken(name) -> bool:
        count = User.query.filter_by(username=name).count()
        return count == 1
    
    # Function to validate user credentials
    def validateCredentials(name, passwd) -> bool:
        count = User.query.filter_by(username=name, password=passwd).count()
        return count == 1