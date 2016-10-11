import csv
import os
import string

from config.Domain import Student

def getStudentList(project_dir):
    students = []

    with open(os.path.join(project_dir, "csv", "students.csv")) as csv_file:
        student_reader = csv.DictReader(csv_file)


        for row in student_reader:
            students.append(Student(row["LastName"], row["FirstName"], row["EmailAddress"]))

    return students

def replacePlaceHolders(template_string, message_attributes):
    parsed_template_string = string.Formatter().parse(template_string)
    placeholders = [p[1] for p in parsed_template_string if p[1]]

    for key in placeholders:
        if key not in message_attributes:
            raise ValueError("Error: Key: " + key + " not found in message attributes. Could not replace.")
            return

    return template_string.format(**message_attributes)