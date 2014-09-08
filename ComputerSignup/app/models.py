from app import db

class Student(db.Model):
    stid = db.Column(db.Integer, primary_key=True, unique=True)
    fname = db.Column(db.String(30))
    lname = db.Column(db.String(30))
    cname = db.Column(db.String(20))
    teacher = db.Column(db.String(12))
    paid = db.Column(db.Boolean)

    def __init__(self, stid, fname, lname, cname, teacher, paid):
        self.stid = stid
        self.fname = fname
        self.lname = lname
        self.cname = cname
        self.teacher = teacher
        self.paid = paid

    def __repr__(self):
        return "<Student %r>" % self.id