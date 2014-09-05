from app import db

class Student(db.Model):
    stid = db.Column(db.Integer, primary_key=True, unique=True)
    fname = db.Column(db.String(30))
    lname = db.Column(db.String(30))
    cname = db.Column(db.String(20))

    def __init__(self, stid, fname, lname, cname):
        self.stid = stid
        self.fname = fname
        self.lname = lname
        self.cname = cname

    def __repr__(self):
        return "<Student %r>" % self.id