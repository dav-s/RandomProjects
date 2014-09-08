from app import app, db
from flask import render_template, request, redirect, flash
from models import Student
import re

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    rf = request.form

    if not rf.get("stid").isdigit:
        flash("The student ID is incorrect")
        return redirect("/")

    haspaid = None
    if rf.get("paid") == "Yes":
        haspaid=True
    if rf.get("paid") == "No":
        haspaid=False
    if haspaid is None:
        flash("Please choose yes or no!")
        return redirect("/")

    formvs = (int(rf.get("stid")), rf.get("fname"), rf.get("lname"), rf.get("cname"), rf.get("teacher"), haspaid)
    if not formsvalidated(*formvs):
        return redirect("/")
    if Student.query.get(formvs[0]):
        flash("Somebody already registered with that ID")
        return redirect("/")
    add_student = Student(*formvs)
    db.session.add(add_student)
    db.session.commit()
    return render_template("success.html", info=formvs)

@app.errorhandler(500)
def error500(e):
    return "whoops something went wrong"

@app.errorhandler(404)
def error404(e):
    return "what are you doing here?"

def formsvalidated(stid, fname, lname, cname, teacher, haspaid):
    sr = re.compile("^[0-9]{2,10}$")
    fr = re.compile("^[A-Za-z- ]{1,30}$")
    lr = re.compile("^[A-Za-z- ]{1,30}$")
    cr = re.compile("^[A-Za-z0-9-]{6,20}$")
    tc = re.compile("^(Westerduin|Christopher|Kenney)$")
    noerror = True
    if sr.match(str(stid)) is None:
        flash("ID does not meet criterion")
        noerror=False
    if fr.match(fname) is None:
        flash("First name does not meet criterion")
        noerror=False
    if lr.match(lname) is None:
        flash("Last name does not meet criterion")
        noerror=False
    if cr.match(cname) is None:
        flash("Computer name does not meet criterion")
        noerror=False
    if tc.match(teacher) is None:
        flash("Computer name does not meet criterion")
        noerror=False
    if haspaid is None:
        flash("Please choose a correct lab fee response")
        noerror=False
    return noerror