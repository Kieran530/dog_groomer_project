from django.shortcuts import render, redirect
def index(request):
    

    return render(request,"index.html")

def book_appointment(request):

    return render(request,"appointment_form.html")