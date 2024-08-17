from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

db = SQLAlchemy()

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.String(255))
    upload_date = db.Column(db.DateTime, default=datetime.now)

    def save(file, description) -> bool:
        try:
            db.session.add(File(name=file.filename, description=description))
            db.session.commit()

            file.save(os.path.join('uploads', file.filename))
        except:
            return False
        return True
    
    def delete(file_id) -> None:
        file = File.query.get(file_id)
        
        if (file != None):
            db.session.delete(file)
            db.session.commit()
            
            os.remove(os.path.join('uploads', file.name))