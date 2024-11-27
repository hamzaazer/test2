from tinydb import TinyDB
from tinydb.queries import Query
from datetime import datetime
import os

# Initialize database
db = TinyDB('student_management.json')

# Create collections
students = db.table('students')
attendance = db.table('attendance')
grades = db.table('grades')

def init_db():
    """Initialize database tables if they don't exist"""
    if not os.path.exists('student_management.json'):
        students.insert({'_init': True})
        attendance.insert({'_init': True})
        grades.insert({'_init': True})
        
        # Remove initialization documents
        students.remove(Query()._init.exists())
        attendance.remove(Query()._init.exists())
        grades.remove(Query()._init.exists())