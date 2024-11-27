from tinydb import Query
from typing import Dict, List, Optional
from database import students, attendance, grades
from datetime import datetime

class DatabaseManager:
    @staticmethod
    def create_student(data: Dict) -> int:
        data['created_at'] = datetime.now().isoformat()
        data['updated_at'] = datetime.now().isoformat()
        return students.insert(data)
    
    @staticmethod
    def get_all_students() -> List[Dict]:
        return students.all()
    
    @staticmethod
    def get_student(student_id: int) -> Optional[Dict]:
        Student = Query()
        return students.get(doc_id=student_id)
    
    @staticmethod
    def update_student(student_id: int, data: Dict) -> None:
        data['updated_at'] = datetime.now().isoformat()
        students.update(data, doc_ids=[student_id])
    
    @staticmethod
    def delete_student(student_id: int) -> None:
        students.remove(doc_ids=[student_id])
        # Cascade delete related records
        Attendance = Query()
        attendance.remove(Attendance.student_id == student_id)
        Grade = Query()
        grades.remove(Grade.student_id == student_id)
    
    @staticmethod
    def create_attendance(data: Dict) -> int:
        data['created_at'] = datetime.now().isoformat()
        return attendance.insert(data)
    
    @staticmethod
    def get_student_attendance(student_id: int) -> List[Dict]:
        Attendance = Query()
        return attendance.search(Attendance.student_id == student_id)
    
    @staticmethod
    def update_attendance(attendance_id: int, data: Dict) -> None:
        attendance.update(data, doc_ids=[attendance_id])
    
    @staticmethod
    def delete_attendance(attendance_id: int) -> None:
        attendance.remove(doc_ids=[attendance_id])
    
    @staticmethod
    def create_grade(data: Dict) -> int:
        data['created_at'] = datetime.now().isoformat()
        return grades.insert(data)
    
    @staticmethod
    def get_student_grades(student_id: int) -> List[Dict]:
        Grade = Query()
        return grades.search(Grade.student_id == student_id)
    
    @staticmethod
    def update_grade(grade_id: int, data: Dict) -> None:
        grades.update(data, doc_ids=[grade_id])
    
    @staticmethod
    def delete_grade(grade_id: int) -> None:
        grades.remove(doc_ids=[grade_id])