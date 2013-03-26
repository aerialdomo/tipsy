"""
tipsy.py -- A flask-based todo list
"""
from flask import Flask, render_template, request, redirect
import model

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html", user_name="Rainbow Dash")

@app.route("/tasks")
def list_tasks():
	db = model.connect_db()
	tasks_from_db = model.get_tasks(db, None)
	return render_template("list_tasks.html", tasks=tasks_from_db)

@app.route("/new_task")
def new_task():
	return render_template("new_task.html",)

@app.route("/save_task", methods = ["POST"])
def save_task():
	task_title = request.form['task_title']
	db = model.connect_db()
	#user 1
	task_id = model.new_task(db, task_title, 1)
	return redirect("/tasks")

@app.route("/mark_complete", methods = ["POST"])
def mark_complete():
	task_id= request.form['click_complete']
	print "TASK ID!!!", task_id
	db = model.connect_db()
	model.complete_task(db, task_id)
	return redirect("/tasks")

@app.route("/edit_task")
def edit_task():
	return render_template("edit_task.html")

# @app.route("/log_in")
# def log_in():
# 	email = request.form['input_email']
# 	password = request.form['input_password']
# 	db = model.connect_db()
# 	model.authenticate(db, email, password)
# 	return render_template("log_in.html",)




if __name__ == "__main__":
	app.run(debug=True)
