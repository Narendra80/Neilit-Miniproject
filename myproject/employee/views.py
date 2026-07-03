from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Sum, Avg, Count, Q
from .models import Employee
from .forms import EmployeeForm, UserRegistrationForm

# ==========================================
# LOGIN & AUTHENTICATION SYSTEM
# ==========================================
def login_view(request):
    """User Login View"""
    if request.user.is_authenticated:
        return redirect('employee:dashboard')
        
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}! You are now logged in.")
            next_url = request.GET.get('next', 'employee:dashboard')
            return redirect(next_url)
        else:
            messages.error(request, "Invalid username or password. Please try again.")
    else:
        form = AuthenticationForm()
        
    return render(request, 'employee/login.html', {'form': form})

def logout_view(request):
    """User Logout View"""
    logout(request)
    messages.info(request, "You have been logged out successfully.")
    return redirect('employee:login')

def register_view(request):
    """New User Registration View"""
    if request.user.is_authenticated:
        return redirect('employee:dashboard')
        
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            messages.success(request, f"Account created successfully! Welcome to the portal, {user.username}.")
            return redirect('employee:dashboard')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserRegistrationForm()
        
    return render(request, 'employee/register.html', {'form': form})

# ==========================================
# ADMIN DASHBOARD
# ==========================================
@login_required
def dashboard(request):
    """Comprehensive Admin Analytics Dashboard"""
    total_employees = Employee.objects.count()
    total_payroll = Employee.objects.aggregate(total=Sum('salary'))['total'] or 0
    avg_salary = Employee.objects.aggregate(avg=Avg('salary'))['avg'] or 0
    
    active_count = Employee.objects.filter(status='Active').count()
    remote_count = Employee.objects.filter(status='Remote').count()
    leave_count = Employee.objects.filter(status='On Leave').count()
    
    # Department breakdown
    dept_stats = Employee.objects.values('department').annotate(
        count=Count('id'),
        avg_sal=Avg('salary')
    ).order_by('-count')
    
    recent_employees = Employee.objects.all()[:6]
    
    context = {
        'total_employees': total_employees,
        'total_payroll': total_payroll,
        'avg_salary': avg_salary,
        'active_count': active_count,
        'remote_count': remote_count,
        'leave_count': leave_count,
        'dept_stats': dept_stats,
        'recent_employees': recent_employees,
    }
    return render(request, 'employee/dashboard.html', context)

# ==========================================
# CRUD & SEARCH OPERATIONS
# ==========================================
@login_required
def employee_list(request):
    """Search & List Employees"""
    search_query = request.GET.get('search', '').strip()
    dept_filter = request.GET.get('dept', '')
    status_filter = request.GET.get('status', '')
    
    employees = Employee.objects.all()
    
    if search_query:
        employees = employees.filter(
            Q(name__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(role__icontains=search_query) |
            Q(department__icontains=search_query)
        )
        
    if dept_filter:
        employees = employees.filter(department=dept_filter)
        
    if status_filter:
        employees = employees.filter(status=status_filter)
        
    # Get distinct departments for filter options
    departments = Employee.objects.values_list('department', flat=True).distinct()
    
    context = {
        'employees': employees,
        'search_query': search_query,
        'dept_filter': dept_filter,
        'status_filter': status_filter,
        'departments': departments,
        'total_found': employees.count()
    }
    return render(request, 'employee/list.html', context)

@login_required
def employee_create(request):
    """Add New Employee"""
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            emp = form.save()
            messages.success(request, f"Employee {emp.name} added successfully!")
            return redirect('employee:list')
        else:
            messages.error(request, "Failed to add employee. Please check the form data.")
    else:
        form = EmployeeForm()
        
    return render(request, 'employee/form.html', {'form': form, 'action': 'Add New'})

@login_required
def employee_update(request, pk):
    """Update Existing Employee"""
    emp = get_object_or_404(Employee, pk=pk)
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=emp)
        if form.is_valid():
            form.save()
            messages.success(request, f"Employee {emp.name} updated successfully!")
            return redirect('employee:list')
        else:
            messages.error(request, "Failed to update employee. Please check the form data.")
    else:
        form = EmployeeForm(instance=emp)
        
    return render(request, 'employee/form.html', {'form': form, 'employee': emp, 'action': 'Update'})

@login_required
def employee_delete(request, pk):
    """Delete Employee Record"""
    emp = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        emp_name = emp.name
        emp.delete()
        messages.success(request, f"Employee {emp_name} has been removed from the directory.")
        return redirect('employee:list')
        
    return render(request, 'employee/delete_confirm.html', {'employee': emp})

# ==========================================
# DEMO & LEGACY VIEWS
# ==========================================
def home(request):
    """Redirect home to Admin Dashboard"""
    return redirect('employee:dashboard')

def simple_http_demo(request):
    """Simple HttpResponse Demo"""
    return HttpResponse("<h1>Welcome to Django Employee Portal</h1><p><a href='/employee/dashboard/'>Go to Dashboard</a></p>")

class HomeView(View):
    """Class-Based View Demo"""
    def get(self, request):
        return redirect('employee:dashboard')

def session_demo(request):
    """Session Management Demo"""
    if request.method == 'POST':
        visitor_name = request.POST.get('visitor_name', 'Guest')
        request.session['visitor_name'] = visitor_name
        messages.info(request, f"Session value saved as: {visitor_name}")
        return redirect('employee:session_demo')
    
    current_session_val = request.session.get('visitor_name', 'None set')
    return render(request, 'employee/session_demo.html', {'current_session_val': current_session_val})
