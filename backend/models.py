import datetime
import sqlalchemy.orm as orm
import sqlalchemy as sql
import passlib.hash as _hash
import database as _database

class User(_database.Base):
    __tablename__="users"
    id = sql.Column(sql.Integer, primary_key=True, index= True)
    email = sql.Column(sql.String, unique=True, index= True)
    hashed_password = sql.Column(sql.String)

    def verify_password(self, password:str):
        return _hash.bcrypt.verify(password, self.hashed_password)