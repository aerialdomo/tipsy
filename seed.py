"""
seed.py
"""
import model

db = model.connect_db()
user_id = model.new_user(db, "pinky@mlp.com", "party", "Pinky Pie")
task = model.new_task(db, "throw a party", user_id)
