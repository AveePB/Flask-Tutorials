from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)
    date_created = db.Column(db.DateTime, default=datetime.now)

    # Function to fetch all tasks
    def get_all() -> list:
        return Task.query.all() 

    # Function to add task
    def create(content) -> bool:
        try:
            db.session.add(Task(content=content))
            db.session.commit()
        except:
            return False
        return True

    # Function to remove task
    def delete(id) -> None:
        task = Task.query.get({"id": id})

        if (task != None):
            db.session.delete(task)
            db.session.commit()