import os
import sys

# Setup Django Environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

try:
    import django
    django.setup()
    from django.contrib.auth import get_user_model
    from employee.models import Employee
except Exception as e:
    print(f"[-] Django setup failed: {e}")
    sys.exit(1)

def seed_database():
    User = get_user_model()
    username = os.environ.get('ADMIN_USERNAME', 'admin')
    email = os.environ.get('ADMIN_EMAIL', 'admin@prohr.com')
    password = os.environ.get('ADMIN_PASSWORD', 'admin123')

    print("=" * 60)
    print("[*] PROHR DATABASE SEEDING & SUPERUSER SETUP (SQLite3)")
    print("=" * 60)

    # 1. Create Admin User
    try:
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            print(f"[+] Superuser '{username}' created successfully!")
            print(f"    -> Login Username: {username}")
            print(f"    -> Login Password: {password}")
        else:
            print(f"[*] Superuser '{username}' already exists.")
    except Exception as e:
        print(f"[-] Could not create superuser: {e}")

    # 2. Seed Sample Employee Profiles
    sample_employees = [
        {
            "name": "Sarah Jenkins",
            "email": "sarah.jenkins@prohr.com",
            "role": "VP of Engineering",
            "department": "Engineering",
            "salary": 145000.00,
            "phone": "+1 (555) 234-5678",
            "status": "Active"
        },
        {
            "name": "Marcus Chen",
            "email": "marcus.chen@prohr.com",
            "role": "Senior Cloud Architect",
            "department": "IT",
            "salary": 128000.00,
            "phone": "+1 (555) 345-6789",
            "status": "Remote"
        },
        {
            "name": "Elena Rodriguez",
            "email": "elena.rodriguez@prohr.com",
            "role": "People Operations Lead",
            "department": "HR",
            "salary": 92000.00,
            "phone": "+1 (555) 456-7890",
            "status": "Active"
        },
        {
            "name": "David Kim",
            "email": "david.kim@prohr.com",
            "role": "Financial Controller",
            "department": "Finance",
            "salary": 115000.00,
            "phone": "+1 (555) 567-8901",
            "status": "Active"
        },
        {
            "name": "Aisha Patel",
            "email": "aisha.patel@prohr.com",
            "role": "Growth Marketing Manager",
            "department": "Marketing",
            "salary": 98000.00,
            "phone": "+1 (555) 678-9012",
            "status": "On Leave"
        }
    ]

    if Employee.objects.count() == 0:
        print("\n[*] Seeding sample employee records...")
        for data in sample_employees:
            Employee.objects.create(**data)
            print(f"    [+] Created profile for: {data['name']} ({data['role']})")
    else:
        print(f"\n[*] Database already populated with {Employee.objects.count()} employees.")

    print("=" * 60)
    print("[*] Database seeding complete!")
    print("=" * 60)

if __name__ == '__main__':
    seed_database()
