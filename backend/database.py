from sqlite3.dbapi2 import _SqliteData
import sqlalchemy as sql
import sqlalchemy.ext.declarative as declarative
import sqlalchemy.orm as orm

DATABASE_URL="sqllite.///.database.db"  

engine = _SqliteData.create_engine(DATABASE_URL, connectargs={"check_same_thread":False})

SessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind= engine)

Base = sql.orm.declarative_base()