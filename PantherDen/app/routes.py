import json
import datetime

from app import app, session
from models import Teacher, Student, Schedule



# I put my id in: I want to see what students are in my class today
#/<teachid>/
class StudentsWithTeacherToday:

    def on_get(self, req, resp, teacherid):
        tid = int(teacherid)
        teacher = session.query(Teacher).get(tid)
        if teacher is None:
            return "404"
        roomid = teacher.roomid
        today = datetime.date.today()
        default = session.query(Student).filter_by(homeroomid=roomid)
        removedscheds = session.query(Schedule).filter_by(oldroomid=roomid, date=today)
        newscheds = session.query(Schedule).filter_by(roomid=roomid, date=today)
        resp["body"] = "hello"

swtt = StudentsWithTeacherToday()
app.add_route("/yolo/", swtt)
