""" Specifies routing for the application"""
from flask import render_template, request, jsonify, redirect
from app import app
from app import database as db_helper

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
    db_helper.update(request.args.get('first'), request.args.get('last'), request.args.get('destCity'), request.args.get('email'), request.args.get('pass'))
    result = {'success': True, 'response': 'Done'}
    #return redirect(url_for('results'))
    return jsonify(result)
    

@app.route("/create", methods=['POST'])
def create():
    """ recieves post requests to add new task """
    db_helper.insert_new_user(request.args.get('first'), request.args.get('last'), request.args.get('destCity'), request.args.get('email'), request.args.get('pass'))
    print("here 2")
    result = {'success': True, 'response': 'Done'}
    #return redirect(url_for('results'))
    return jsonify(result)

@app.route("/search", methods=['POST'])
def search():
    res=db_helper.search_db(request.args.get('c'))
    result = {'success': True, 'response': 'Done'}
    print("SUCCESS?")
    return render_template("country.html", res=res)

@app.route("/home", methods=['GET', 'POST'])
def home():
    print('HERE')
    name = request.form['name']
    print(name)
    res = db_helper.search_db(name)
    print(res)
    return render_template("country.html", res=res)

@app.route("/")
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