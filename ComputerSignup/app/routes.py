from app import app, db
from flask import render_template, request, redirect, flash, url_for
from models import Student
import re

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    rf = request.form
    formvs = (rf.get("stid"), rf.get("fname"), rf.get("lname"), rf.get("cname"))
    if not formsvalidated(*formvs):
        return redirect("/")
    id = int(rf.get("stid"))
    if Student.query.get(id):
        flash("That student ID already exists")
        return redirect("/")
    add_student = Student(id, formvs[1], formvs[2], formvs[3])
    db.session.add(add_student)
    db.session.commit()
    return render_template("success.html", info=formvs)

@app.errorhandler(500)
def error500(e):
    return "whoops something went wrong"

@app.errorhandler(404)
def error404(e):
    return "what are you doing here?"

def formsvalidated(stid, fname, lname, cname):
    sr = re.compile("^[0-9]{2,10}$")
    fr = re.compile("^[A-Za-z- ]{1,30}$")
    lr = re.compile("^[A-Za-z- ]{1,30}$")
    cr = re.compile("^[A-Za-z0-9-]{6,20}$")
    noerror = True
    if not sr.match(stid):
        flash("ID does not meet criterion")
        noerror=False
    if not fr.match(fname):
        flash("First name does not meet criterion")
        noerror=False
    if not lr.match(lname):
        flash("Last name does not meet criterion")
        noerror=False
    if not cr.match(cname):
        flash("Computer name does not meet criterion")
        noerror=False
    return noerror