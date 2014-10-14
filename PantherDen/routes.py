import json
import datetime
from app import session as sess
from models import Teacher, Student, Schedule

# I put my id in: I want to see what students are in my class today
#/<teachid>/
class StudentsWithTeacherToday:

    def on_get(self, req, resp, teacherid):
        tid = int(teacherid)
        teacher = sess.query(Teacher).get(tid)
        if teacher is None:
            return "404"
        roomid = teacher.roomid
        today = datetime.date.today()
        default = sess.query(Student).filter_by(homeroomid=roomid)
        removedscheds = sess.query(Schedule).filter_by(oldroomid=roomid, date=today)
        newscheds = sess.query(Schedule).filter_by(roomid=roomid, date=today)
        return json.dumps({})