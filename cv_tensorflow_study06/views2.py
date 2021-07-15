from flask import render_template, request

def index():
    return render_template("index.html")
    # if request.method == "POST":
    #     first_name = request.from['first']
    #     last_name = request.from['last']
    #     email_id = request.from['email']

    # data = {
    #     "first" : first_name,
    #     "last" : last_name,
    #     "email" : email_id
    # }

    