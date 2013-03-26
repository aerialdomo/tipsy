"""
model.py
"""
from datetime import *
import sqlite3

def connect_db():

    return sqlite3.connect("tipsy.db")

def new_user(db, email, password, name):          
    c = db.cursor()                                     
    query = """INSERT INTO Users VALUES (NULL, ?, ?, ?)"""                                                           
    result = c.execute(query, (email, password, name))           
    db.commit()
    print "Created new user: %s" % name
    return result.lastrowid

def authenticate(db, email, password):
    c = db.cursor()
    query = """SELECT * from Users WHERE email=? AND password=?"""
    c.execute(query, (email, password))
    result = c.fetchone()
    if result:
        fields = ["id", "email", "password", "username"]
        return dict(zip(fields, result))

    return None

def get_user(db, user_id):
    """Gets a user dictionary out of the database given an id"""
    c = db.cursor()
    query = """ SELECT name, id FROM Users WHERE id=?  """
    c.execute(query,(user_id,))
    result = c.fetchone()
    fields = ["name", "user_id"]
    print "User name: %s" % fields[0]
    return dict(zip(fields, result))


def new_task(db, title, user_id):
    """Given a title and a user_id, create a new task belonging to that user. 
    Return the id of the created task"""
    c =db.cursor()
    created_at = datetime.today()
    completed_at = ""
    query = """INSERT INTO Tasks VALUES (NULL, ?, ?, NULL, ?)"""
    result = c.execute(query, (title, created_at, user_id))
    db.commit()
    print "Added new task : %s" % title
    print "New task ID: ", result.lastrowid
    return result.lastrowid
   
def complete_task(db, task_id):
    """Mark the task with the given task_id as being complete."""
    c = db.cursor()
    completed_at = datetime.today()
    query = """UPDATE Tasks SET completed_at=? WHERE id =?"""
    c.execute(query, (completed_at, task_id))
    db.commit()
    print "Task %r marked as complete." % task_id

def edit_title(db, task_id, new_title):
    """Edit a task title""" 
    c = db.cursor()
    query = """UPDATE Tasks SET title = ? WHERE id=?"""
    c.execute(query, (new_title, task_id))
    db.commit()
    print "Task %r titled changed." % task_id

# If get_tasks is called with one parameter, user_id defaults to None
def get_tasks(db, user_id=None):
    """Get all the tasks matching the user_id,
     getting all the tasks in the system if the user_id is not provided. 
     Returns the results as a list of dictionaries."""
    c = db.cursor()
    if user_id == None:
        query = """SELECT * FROM Tasks"""
        c.execute(query)

    else:
        query = """SELECT * FROM Tasks WHERE user_id =?"""
        # execute method needs tuple parameters, so user_id needs a comma after it
        c.execute(query, (user_id,))
 
    result = c.fetchall()
    dict_list = []
    for row in result:
        fields = ["task_id", "title", "created_at", "completed_at", "user_id"]
        item = dict(zip(fields, row))
        dict_list.append(item)
    return dict_list

def get_task(db, task_id):
    """Gets a single task, given its id. Returns a dictionary of the task data."""
    c = db.cursor()
    query = """SELECT * FROM Tasks where id =?"""
    c.execute(query, (task_id,))
    result = c.fetchone()
    fields = ["title", "created_at", "completed_at", "user_id"]
    return dict(zip(fields, result))

def main():
    db = connect_db()
    #edit_title(db, 1, "Singing")

    # Testing code!!!
    #pony_id = new_user(db, "rainbow@mlp.com", "Sonic Rainboom!", "Rainbow Dash")
    #pony_task = new_task(db, "Make a sonic rainboom", pony_id)
    #get_id = get_user(db, pony_id)
    #complete_task(db, task_id)
    #list = get_task(db, task_id)

main()

