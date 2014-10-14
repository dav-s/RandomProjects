import falcon
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import Student, Teacher, Schedule
from routes import *

class test:
    def on_get(self, req, resp):
        return "swag"

engine = sa.create_engine("sqlite:///pden.db")
Base = declarative_base()
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

app = falcon.API()
swtt = StudentsWithTeacherToday()
app.add_route("/{teacherid}/today/", swtt)

if __name__ == "__main__":
    from wsgiref import simple_server
    httpd = simple_server.make_server("127.0.0.1", 8000, app)
    httpd.serve_forever()