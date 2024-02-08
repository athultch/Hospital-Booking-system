from django.shortcuts import render
from .models import Departments, Doctors
from .forms import BookingForm

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')  # Redirect to confirmation page after successful form submission
    else:
        form = BookingForm()
    
    doctors = Doctors.objects.all()  # Queryset for all doctors
    dict_form = {'form': form, 'doctors': doctors}  # Include doctors in the context
    return render(request, "booking.html", dict_form)

def doctors(request):
    dict_docs = {
        'doctors': Doctors.objects.all()
    }
    return render(request, "doctors.html", dict_docs)

def contact(request):
    return render(request, "contact.html")

def department(request):
    dict_dept = {
        'dept': Departments.objects.all() 
    }
    return render(request, "department.html", dict_dept)
