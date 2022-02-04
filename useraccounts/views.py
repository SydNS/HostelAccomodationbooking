from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth import login, authenticate, logout  # add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
import datetime


def Registering(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)

        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            messages.error(request, ' This ' + email + 'is already in use')
            return redirect("/login")

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            # return redirect("bookingapp:indexroute")
            return redirect("profilesetup")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="dashboard/hostel/auth-register-v3.html",
                  context={"register_form": form})


def loginuser(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("bookingapp:indexroute")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="dashboard/hostel/auth-login-v3.html", context={"login_form": form})
    # return render(request, , info)


def Logout(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login')


# profile registering
# @login_required
def ProfileSetting(request):
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    if request.method == 'POST':
        student_form = StudentForm(request.POST, request.FILES)

        if student_form.is_valid():
            try:
                student = student_form.save(commit=True)
                student.save()
                print(student.photo)
                registered = True
                return HttpResponseRedirect("/profiledetails")
            except:
                messages.error(request, "Sorry something went worng.")
        # else:
        #     return HttpResponseRedirect('<p>Hello</p>')

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    elif request.method == 'GET':
        student_form = StudentForm(initial={'name_user': request.user})
        # student_form.fields["name_user"]=request.user

    return render(request, 'dashboard/hostel/hostelstudentprofile.html', {
        'student_form': student_form,
        'registered': registered,
    })


def Profiledetails(request):
    currentuser = request.user
    if request.method == 'POST':
        student_form = StudentForm(request.POST, request.FILES)

        # fetch the object related to passed user in the GET request
        studentdetails_to_update = Student.objects.get(name_user=currentuser)

        # pass the object as instance in form
        studentdetails_to_update_form = StudentForm(request.POST, instance=studentdetails_to_update)

        if student_form.is_valid():
            try:
                student = studentdetails_to_update_form.save(commit=True)
                student.save()
                registered = True
                return HttpResponseRedirect("/profiledetails")
            except:
                pass
        # else:
        #     return HttpResponseRedirect('<p>Hello</p>')

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    elif request.method == 'GET':
        # studentdetails = Student.objects.get(name_user=request.user)

        # if not studentdetails:
        #
        try:
            studentdetails = Student.objects.get(name_user=request.user)
            student_form = StudentForm(initial={
                'name_user': studentdetails.name_user,
                'photo': studentdetails.photo,
                'gender': studentdetails.gender,
                'date_of_birth': studentdetails.date_of_birth,
                'reporting_date': studentdetails.reporting_date,
                'address': studentdetails.address,
                'parent_name': studentdetails.parent_name,
                'phonenumber': studentdetails.phonenumber,
                'city': studentdetails.city,
                'state': studentdetails.state,
                'studentIdnumber': studentdetails.studentIdnumber,
                'level_of_study': studentdetails.level_of_study

            })

            age = datetime.datetime.now()
            age = age.year
            age = age - studentdetails.date_of_birth.year

            return render(request, 'dashboard/hostel/userprofiledetails.html', {
                'studentdetails': studentdetails,
                'student_form': student_form,
                'age': age
            })

        except:
            studentdetails = {
                'name_user': "Enter Your Name Here",
                'gender': "Gender",
                'date_of_birth': "Enter Birthday",
                'reporting_date': "Reporting Date",
                'address': "Your Address",
                'parent_name': "Parent Names",
                'phonenumber': "Phone Contact",
                'city': "Home City",
                'state': "State/Region",
                'studentIdnumber': "Your ID.Numebr",
                'level_of_study': "Year Of Study"

            }
            student_form = StudentForm(initial={
                'name_user': "Enter Your Name ",
                'gender': "Gender",
                'date_of_birth': "Enter Birthday",
                'reporting_date': "Reporting Date",
                'address': "Your Address",
                'parent_name': "Parent Names",
                'phonenumber': "Phone Contact",
                'city': "Home City",
                'state': "State/Region",
                'studentIdnumber': "Your ID.Numebr",
                'level_of_study': "Year Of Study"

            })
            age = datetime.datetime.now()
            age = age.year
            age = age - 2003
            req_age = "Should be atleast" + str(age)
            return render(request, 'dashboard/hostel/userprofiledetails.html', {
                'studentdetails': studentdetails,
                'student_form': student_form,
                'age': req_age
            })


def Profiledetailofanotheruser(request, id):
    studentdetails = Student.objects.get(id=id)

    return render(request, 'dashboard/hostel/profiledetails.html', {
        'studentdetails': studentdetails,

    })


def Customersview(request):
    studentdetails = Student.objects.all()
    totalusers = studentdetails.count()

    return render(request, 'dashboard/hostel/studentslistwithimages.html', {
        'studentdetails': studentdetails,
        'totalusers': totalusers,

    })

def Customerdetailsview(request,id):
    studentdetails = Student.objects.get(id=id)

    return render(request, 'dashboard/hostel/userprofiledetails.html', {
        'studentdetails': studentdetails,

    })
