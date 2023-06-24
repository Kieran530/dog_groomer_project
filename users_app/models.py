from django.db import models
import bcrypt
import re
from bcrypt import checkpw





class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 3:
            errors["first_name"] = "First name should be at least 3 characters"
        if len(postData['last_name']) < 3:
            errors["last_name"] = "Last name should be at least 3 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):            
            errors["email"] = "Invalid email address!"
        if len(postData['password']) < 6:
            errors["password"] = "Password should be at least 6 characters"
        if  (postData['password']) != (postData['confirm_password']):
            errors["confirm_password"] = "Passwords do not match"
        if not any(char.isdigit() for char in postData['password']):
            errors["password"] = "Password should contain at least one number"
        if not any(char.isupper() for char in postData['password']):
            errors["password"] = "Password should contain at least one uppercase letter"
        if not re.search(r"[!@#$%^&*]", postData['password']):
            errors["password"] = "Password should contain at least one special character"
        if User.objects.filter(email=postData['email']).exists():
            errors["email"] = "Email already exists"
        return errors
    def validate_login(self,postData):
        errors={}
        if not User.objects.filter(email=postData['email']).exists():
            errors["email"] = "Email does not exist"
        else:
            user = User.objects.get(email=postData['email'])
            if not checkpw(postData['password'].encode(), user.password.encode()):
                errors["password"] = "Password does not match"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=UserManager()



class Service(models.Model):
    CATEGORY_CHOICES = (
        ('wash', 'Wash'),
        ('left_add_on', 'Left Add-on'),
        ('right_add_on', 'Right Add-on'),
    )
    
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='wash')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def name_to_id(self):
        return self.name.replace(' ', '-').lower()

class Appointment(models.Model):
    pet_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    breed = models.CharField(max_length=255)
    coat_type= models.CharField(max_length=255)
    weight = models.IntegerField()
    dry_flakeyskin= models.BooleanField(default=False)
    sheds=models.BooleanField(default=False)
    ear_gunk=models.BooleanField(default=False)
    sensitive_ears=models.BooleanField(default=False)
    butt_dragger=models.BooleanField(default=False)
    fleas=models.BooleanField(default=False)
    anything_else=models.TextField(default="")
    date=models.DateTimeField(null=True)
    services = models.ManyToManyField(Service, related_name="services")
    user = models.ForeignKey(User, related_name="appointments",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    # many-to-many
    # reference for service table and the appointment table 
