import os
import sys
import django

# Setup Django Environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from student.models import Student
from employee.models import Employee
from django.db import connections

def test_database_connections():
    print("=" * 60)
    print("[*] DJANGO DBSQL LITE (SQLite3) CONNECTION & ORM DEMO")
    print("=" * 60)

    # Test SQLite (default) Connection
    print("\n[1] Testing SQLite Database ('default')...")
    try:
        conn_sqlite = connections['default']
        conn_sqlite.ensure_connection()
        print("[+] SQLite connection successful!")
        
        # Count records in SQLite
        student_count_sqlite = Student.objects.count()
        employee_count_sqlite = Employee.objects.count()
        print(f"    -> SQLite Records: {student_count_sqlite} Students | {employee_count_sqlite} Employees")

        # Create a demo student in SQLite
        demo_student, created = Student.objects.get_or_create(
            rollnumber="SQLITE01",
            defaults={"name": "Alice (SQLite User)", "age": 20, "course": "Django & DBSQL Lite"}
        )
        if created:
            print(f"    -> Added demo student to SQLite: {demo_student}")
        else:
            print(f"    -> Demo student already exists in SQLite: {demo_student}")

    except Exception as e:
        print(f"[-] SQLite connection failed: {e}")

    print("\n" + "=" * 60)
    print("[*] Demo complete! Using SQLite3 engine smoothly.")
    print("=" * 60)

if __name__ == "__main__":
    test_database_connections()
