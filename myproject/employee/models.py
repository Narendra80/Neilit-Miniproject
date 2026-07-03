from django.db import models

# Django Models and ORM for Employee Management System
class Employee(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('On Leave', 'On Leave'),
        ('Remote', 'Remote'),
    ]

    objects = models.Manager()
    name = models.CharField(max_length=100, verbose_name="Full Name")
    email = models.EmailField(unique=True, verbose_name="Email Address")
    role = models.CharField(max_length=100, default="Software Engineer", verbose_name="Job Role")
    department = models.CharField(max_length=50, default="General", verbose_name="Department")
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=50000.00, verbose_name="Salary")
    phone = models.CharField(max_length=20, default="+1 555-0100", verbose_name="Phone Number")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active', verbose_name="Status")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.role} - {self.department})"

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
