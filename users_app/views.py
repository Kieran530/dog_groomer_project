from django.shortcuts import render, redirect
from .models import User
from .models import Service
from .models import Appointment
from datetime import datetime
from django.db.models import Sum
from django.contrib import messages
import bcrypt
from bcrypt import checkpw

def index(request):
    return render(request,"index.html")

def login_reg(request):
    form_data = request.session.get('form_data', {
    'first_name': '',
    'last_name': '',
    'email': '',
})
    return render(request, "login&reg.html", {'form_data': form_data})      
#add validations here
#add password encryption
def login(request):
    email = request.POST.get("email")
    password = request.POST.get("password")
    error_count=0
    try:
        user = User.objects.get(email=email)
        if checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            # Password is correct, log in the user and redirect to the desired page
            request.session["user_id"] = user.id
            return redirect("index")
        else:
            # Password is incorrect, display error message
            messages.error(request, "Incorrect password")
            return redirect("login&reg")
    except User.DoesNotExist:
        # Email does not exist, display error message
        
        messages.error(request, "Email is not registered")
        #if there are no errors, check if finalize_url is in session and redirect to finalize if it is
        
        return redirect("login&reg")
       

def logout(request):
    request.session.clear()
    return redirect("index")


def register(request):

    errors=User.objects.basic_validator(request.POST)
    if len(errors)>0:
        # Save values to session
        request.session['form_data'] = {
                'first_name': request.POST.get('first_name', ''),
                'last_name': request.POST.get('last_name', ''),
                'email': request.POST.get('email', ''),
            }


        for key,value in errors.items():
            messages.error(request,value)
        return redirect("login&reg")
    else:
        password=request.POST["password"]
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        email=request.POST["email"]
        password=pw_hash

        add_new_user=User.objects.create(first_name=first_name,last_name=last_name,email=email,password=password)
        request.session["user_id"]=add_new_user.id

        # Clear session data
        del request.session['form_data']
        #if finalize_url is in session, redriect to finalize
        if "finalize_url" in request.session:
            return redirect(request.session["finalize_url"])
        else:
            return redirect("index")    

def about(request):
    return render(request,"about.html")

def book_appointment(request):
    apppointment_in_progress=request.session.get("appointment_in_progress",{
        'pet_name':"",
        'breed': '',
        'weight': '', 
        'coat_type': '',
    })


    return render(request,"appointment_form.html",{"appointment_in_progress":apppointment_in_progress})

def create_appointment(request):
    
    request.session["appointment_in_progress"]=request.POST
    current_appointment=request.session["appointment_in_progress"]
    print(current_appointment)
    
    def check_appointment_form(some_dict):
        reset_counter=0
        if some_dict["pet_name"]=="":
            messages.error(request,"Please enter a pet name")
            reset_counter+=1
        if some_dict["breed"]=="":
            messages.error(request,"Please enter a breed")
            reset_counter+=1
        if some_dict["weight"]=="":
            messages.error(request,"Please enter a weight")
            reset_counter+=1
        if some_dict["coat_type"]=="":
            messages.error(request,"Please enter a coat type")
            reset_counter+=1
        return reset_counter
    

    errors_count=check_appointment_form(current_appointment)
    if errors_count>0:
        request.session["appointment_in_progress"]=current_appointment
        return redirect("book_appointment")
    request.session["appointment_in_progress"] = current_appointment 

    return redirect("select_service")


def select_service(request):
    if request.method == "POST":
        selected_services = request.POST.getlist('services[]')
        request.session["selected_services"] = selected_services

        if len(selected_services) == 0:
            messages.error(request, "Please select at least one service")
            return redirect("select_service")


        print(request.session["selected_services"])
        return redirect("finalize")
    #retrieve selected options and store in session 
    
    print(request.session["appointment_in_progress"])
    services=Service.objects.all()
    
    wash_services=services.filter(category="wash")
    left_add_on_services=services.filter(category="left_add_on")
    right_add_on_services=services.filter(category="right_add_on")    

    context={
        "wash_services":wash_services,
        "left_add_on_services":left_add_on_services,
        "right_add_on_services":right_add_on_services,
    }
    return render(request,"select_service.html",context)





def finalize_appointment(request):
    if request.method == 'POST':
        if 'user_id' not in request.session:
            
            #save the Finalize URL to session
            request.session["finalize_url"] = "finalize"
            messages.error(request, "Please log in or register to book an appointment")
            return redirect("login&reg")
        else:

            appointment_datetime_str = request.POST.get("appointment_datetime")

        if not appointment_datetime_str:
            messages.error(request, "Please select an appointment date and time")
            return redirect("finalize")

        appointment_datetime = request.POST['appointment_datetime']


        service_ids = [int(id) for id in request.session["selected_services"]]
        services = Service.objects.filter(id__in=service_ids)
        
        appointment_datetime = datetime.strptime(appointment_datetime_str, "%Y-%m-%dT%H:%M")

        appointment = Appointment.objects.create(
            pet_name=request.session["appointment_in_progress"]["pet_name"],
            gender=request.session["appointment_in_progress"]["gender"],
            breed=request.session["appointment_in_progress"]["breed"],
            coat_type=request.session["appointment_in_progress"]["coat_type"],
            weight=request.session["appointment_in_progress"]["weight"],
            dry_flakeyskin=request.session["appointment_in_progress"].get("dry_flakeyskin",False),
            sheds=request.session["appointment_in_progress"].get("sheds",False),
            ear_gunk=request.session["appointment_in_progress"].get("ear_gunk",False),
            sensitive_ears=request.session["appointment_in_progress"].get("sensitive_ears",False),
            butt_dragger=request.session["appointment_in_progress"].get("butt_dragger",False),
            fleas=request.session["appointment_in_progress"].get("fleas",False),
            anything_else=request.session["appointment_in_progress"].get("anything_else",""),
            date=appointment_datetime,
            user=User.objects.get(id=request.session["user_id"])                    )
        
        appointment.services.set(services)
        
        return redirect("complete")
    

    current_services=Service.objects.filter(id__in=request.session["selected_services"])
    total_price = current_services.aggregate(total=Sum('price'))['total']
    return render(request,"finalize.html",{"current_services":current_services,"total_price":total_price})

def complete_appointment(request):

    appointments = Appointment.objects.filter(user_id=request.session["user_id"])
    current_appointment = appointments.last()


    total_price = current_appointment.services.aggregate(total=Sum('price'))['total']
    #clear session of the appointment in progress and the finalize url
    del request.session["appointment_in_progress"]
    if "finalize_url" in request.session:
        del request.session["finalize_url"]
    # del request.session["finalize_url"]
    return render(request,"complete.html",{"current_appointment":current_appointment,"total_price":total_price})








def services(request):
    return render(request,"services.html")



def view_appointments(request):
    user_id= request.session.get("user_id")
    if user_id is None or user_id != 10:
        print("not admin")
        return redirect("index")
    else:
        appointments=Appointment.objects.all().order_by("-date")
        return render(request,"view_appointments.html",{"appointments":appointments})


def view__single_appointment(request,appointment_id):
    user_id= request.session.get("user_id")
    if user_id is None or user_id != 10:
        print("not admin")
        return redirect("index")
    else:
        appointment=Appointment.objects.get(id=appointment_id)
        total_price = appointment.services.aggregate(total=Sum('price'))['total']
        return render(request,"view_single_appointment.html",{"appointment":appointment,"total_price":total_price})

# def edit_appointment(request,appointment_id):
#     appointment=Appointment.objects.get(id=appointment_id)
#     return render(request,"edit_appointment.html",{"appointment":appointment})

# def update_appointment(request,appointment_id):
#     return redirect("view_appointment",appointment_id=appointment_id)

def delete_appointment(request,appointment_id):
    appointment=Appointment.objects.get(id=appointment_id)
    appointment.delete()
    return redirect("appointments")
