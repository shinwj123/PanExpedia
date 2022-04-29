""" Specifies routing for the application"""
#from flask import render_template, request, jsonify, redirect
from app import app
from app import database as db_helper
from flask import Flask, render_template, render_template_string, request, session, redirect, url_for, jsonify

app.secret_key = 'BAD_SECRET_KEY'


@app.route("/delete/", methods=['POST'])
def delete():
    """ recieved post requests for entry delete """
    try:
        db_helper.remove_user_by_email(request.args.get('e'))
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/edit/<int:task_id>", methods=['POST'])
def bad(task_id):
    """ recieved post requests for entry updates """

    data = request.get_json()

    try:
        if "status" in data:
            db_helper.update_status_entry(task_id, data["status"])
            result = {'success': True, 'response': 'Status Updated'}
        elif "description" in data:
            db_helper.update_task_entry(task_id, data["description"])
            result = {'success': True, 'response': 'Task Updated'}
        else:
            result = {'success': True, 'response': 'Nothing Updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)

@app.route("/update", methods=['POST'])
def update():
    """ recieves post requests to add new task """
    print("HERE")
    db_helper.update(request.args.get('first'), request.args.get('last'), request.args.get('destCity'), session["email"], request.args.get('pass'))
    result = {'success': True, 'response': 'Done'}
    return redirect('/')
    

@app.route("/create", methods=['GET', 'POST'])
def create():
    print("hereerereEREWR")
    """ recieves post requests to add new task """
    session['email'] = request.args.get('email')
    print(request.args.get('first'))
    task = db_helper.insert_new_user(request.args.get('first'), request.args.get('last'), request.args.get('destCity'), request.args.get('email'), request.args.get('pass'))
    print("here 2")
    result = {'success': True, 'response': 'Done'}
    return redirect('/')
    #return jsonify(result)

@app.route("/search", methods=['POST'])
def search():
    res=db_helper.search_db(request.args.get('c'))
    result = {'success': True, 'response': 'Done'}
    print("SUCCESS?")
    return render_template("country.html", res=res)

@app.route("/country", methods=['GET', 'POST'])
def home():
    print('HERE')
    name = request.form['name']
    print(name)
    country_res, airport_res, covid_res, rate = db_helper.search_country(name)
    return render_template("country.html", country_res=country_res, airport_res=airport_res, covid_res=covid_res, rate=rate)

@app.route("/", methods=['GET', 'POST'])
def homepage():
    """ returns rendered homepage """
    items = db_helper.fetch_todo()
    #res = db_helper.search_db(request.args.get('c'))
    return render_template("index.html", items=items)

@app.route("/covidRate", methods=['GET', 'POST'])
def covidRate():
    print('HERE')
    #name = request.form['Rate in Country'] # getting info that is stored in name
    #print(name)
    res = db_helper.getCovidRate()
    print(res)
    return render_template("covidrate.html", res_=res)

@app.route("/vaxRate", methods=['GET', 'POST'])
def vaccinationRate():
    print('HERE')
    #name = request.form['Rate in Country'] # getting info that is stored in name
    #print(name)
    res = db_helper.getVaxRate()
    print(res)
    return render_template("vaccinationrate.html", res_=res)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        # Save the form data to the session object
        session['email'] = request.form['email_address']
        valid = db_helper.login(request.form['email_address'], request.form['password'])
        if (valid):
            return redirect('/')
        else:
            print("INVALID")
            return render_template("login.html", message=True)
    else:
        return render_template("login.html", message=False)

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")

@app.route("/userprofile", methods=['GET', 'POST'])
def userprofile():
    return render_template("userprofile.html")



        