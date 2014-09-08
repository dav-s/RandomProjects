import csv
from app import models
from config import CSV_FILENAME

with open(CSV_FILENAME, 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(["Student ID", "First Name", "Last Name", "Computer Name", "Teacher", "Has Paid"])
    for s in models.Student.query.order_by(models.Student.teacher):
        writer.writerow([s.stid, s.fname, s.lname, s.cname, s.teacher, "Yes" if s.paid else "No"])
