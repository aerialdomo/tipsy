"""
model.py
"""
import datetime
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
    if result:
        fields = ["name", "user_id"]
        print "User name: %s" % fields[0]
        return dict(zip(fields, result))


def new_task(db, title, user_id):
    """Given a title and a user_id, create a new task belonging to that user. 
    Return the id of the created task"""
    c =db.cursor()
    created_at = "now"
    completed_at = 0
    query = """INSERT INTO Tasks VALUES (NULL, ?, ?, ?, ?)"""
    result = c.execute(query, (title, user_id, created_at, completed_at))
    db.commit()
    print "Added new task : %s" % title
    print "New task ID: ", result.lastrowid
    return result.lastrowid
   
def complete_task(db, task_id):
    """Mark the task with the given task_id as being complete."""
    c = db.cursor()
    completed_at = "00/00/00"
    query = """UPDATE Tasks SET completed_at = ? WHERE id =?"""
    c.execute(query, (completed_at, task_id))
    print "Task %r marked as complete." % task_id

def get_tasks(db, user_id=None):
    """Get all the tasks matching the user_id, getting all the tasks in the system if the user_id is not provided. Returns the results as a list of dictionaries."""
    pass

def get_task(db, task_id):
    """Gets a single task, given its id. Returns a dictionary of the task data."""

def main():
    db = connect_db()
    pony_id = 51
    #task_id = 21
    pony_task = new_task(db, "Play with animals", pony_id )
    get_id = get_user(db, pony_id)
    #complete_task(db, task_id)

main()

