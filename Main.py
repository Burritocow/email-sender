import os


from config.Properties import Properties
from config.Domain import Email
from service.Services import getStudentList
from service.Services import replacePlaceHolders



yaml_props = Properties()

project_dir = os.path.dirname(__file__)

template_string = open(os.path.join(project_dir, "templates", yaml_props.template), "r").read()

students = getStudentList(project_dir)

emails = []

for student in students:
    student_dict = {'first_name': student.first_name, 'adj' : "totally gnar"}

    email = Email(yaml_props.email_properties)
    email.to_address = student.email_address
    email.content = replacePlaceHolders(template_string, student_dict)
    emails.append(email)


for email1 in emails:
    print("Subject: " + email1.subject)
    print("To: " + email1.to_address)
    print("From: " + email1.from_address)
    print("Reply To: " + email1.reply_to_address)
    print(email1.content + "\n\n")






