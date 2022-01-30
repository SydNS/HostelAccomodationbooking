from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth import login, authenticate, logout  # add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
import datetime


def Registering(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
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
                registered = True
                return HttpResponseRedirect("/profiledetails")
            except:
                pass
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
    if request.method == 'POST':
        student_form = StudentForm(request.POST, request.FILES)

        if student_form.is_valid():
            try:
                student = student_form.save(commit=True)
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
        student_form = StudentForm(initial={
            'name_user': request.user,
            'gender': request.gender,
            'date_of_birth': request.date_of_birth,
            'reporting_date': request.reporting_date,
            'address': request.address,
            'phonenumber': request.phonenumber,
            'city': request.city,
            'state': request.state,
            'studentIdnumber': request.studentIdnumber,
            'level_of_study': request.level_of_study

        })

    studentdetails = Student.objects.get(name_user=request.user)
    age = datetime.datetime.now()
    age = age.year
    age = age - studentdetails.date_of_birth.year

    return render(request, 'dashboard/hostel/userprofiledetails.html', {
        'studentdetails': studentdetails,
        'student_form': student_form,
        'age': age
    })
