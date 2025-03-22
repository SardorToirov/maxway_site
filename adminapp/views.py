from django.shortcuts import render, redirect
from home.models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import *
from . import services


def login_required_decorator(func):
    return login_required(func, login_url='login_page')


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect("login_page")


def login_page(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, password=password, username=username)
        if user is not None:
            login(request, user)
            return redirect("home_page")

    return render(request, 'login.html')


@login_required_decorator
def home_page(request):
    faculties = services.get_faculties()
    guruhs = services.get_guruh()
    subjects = services.get_subject()
    teachers = services.get_teacher()

    ctx = {
        'counts': {
            'faculties': len(faculties),
            'guruhs':len(guruhs),
            'subjects':len(subjects),
            'teachers':len(teachers),
        }
    }
    return render(request, 'indexs.html', ctx)


@login_required_decorator
def faculty_create(request):
    model = Categories()
    form = FacultyForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions',[])
        actions += [f"You edited faculty: {request.POST.get('name')}"]
        request.session["actions"] = actions

        faculty_count = request.session.get('faculty_count', 0)
        faculty_count += 1
        request.session["faculty_count"] = faculty_count

        return redirect('faculty_list')
    ctx = {
        "form": form
    }
    return render(request, 'faculty/form.html', ctx)


@login_required_decorator
def faculty_edit(request, pk):
    model = Categories.objects.get(pk=pk)
    form = FacultyForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        actions = request.session.get('actions',[])
        actions += [f"You edited faculty: {request.POST.get('name')}"]
        request.session["actions"] = actions

        faculty_count = request.session.get('faculty_count', 0)
        faculty_count += 1
        request.session["faculty_count"] = faculty_count

        return redirect('faculty_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'faculty/form.html', ctx)


@login_required_decorator
def faculty_delete(request, pk):
    model = Categories.objects.get(pk=pk)
    model.delete()
    return redirect('faculty_list')


@login_required_decorator
def faculty_list(request):
    faculties = services.get_faculties()
    print(faculties)
    ctx = {
        "faculties": faculties
    }
    return render(request, 'faculty/list.html', ctx)



@login_required_decorator
def guruh_created(request):
    model = Products()
    form = GuruhForm(request.POST or None,instance=model)
    if request.POST and form.is_valid():
        form.save()
        actions = request.session.get('actions', [])
        actions += [f"You created Group: {request.POST.get('name')}"]
        request.session["actions"] = actions

        group_count = request.session.get('group_count', 0)
        group_count += 1
        request.session["group_count"] = group_count

        return redirect('guruh_list')

    stx = {
        "form":form
    }
    return render(request,'Guruh/form.html',stx)


@login_required_decorator
def guruh_edit(request,pk):
    model = Products.objects.get(pk=pk)
    form = GuruhForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('guruh_list')

    stx = {
        "form": form,
        "model":model
    }
    return render(request, 'guruh/form.html', stx)


@login_required_decorator
def guruh_delete(request,pk):
    model = Products.objects.get(pk=pk)
    model.delete()
    return redirect('guruh_list')


@login_required_decorator
def guruh_list(request):
    guruhs = services.get_guruh()

    stx = {
        "guruhs": guruhs
    }
    return render(request,'guruh/list.html',stx)


@login_required_decorator
def subject_created(request):
    model = Orders()
    form = SubjectForm(request.POST or None,instance=model)
    if request.POST and form.is_valid():
        form.save()
        actions = request.session.get('actions', [])
        actions += [f"You created Subject: {request.POST.get('name')}"]
        request.session["actions"] = actions

        subject_count = request.session.get('subject_count', 0)
        subject_count += 1
        request.session["subject_count"] = subject_count

        return redirect('subject_list')

    stx = {
        "form":form
    }
    return render(request,'subject/form.html',stx)


@login_required_decorator
def subject_edit(request,pk):
    model = Orders.objects.get(pk=pk)
    form = SubjectForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('subject_list')

    stx = {
        "form": form,
        "model":model
    }
    return render(request, 'subject/form.html', stx)


@login_required_decorator
def subject_delete(request,pk):
    model = Orders.objects.get(pk=pk)
    model.delete()
    return redirect('subject_list')


@login_required_decorator
def subject_list(request):
    subjects = services.get_subject()

    stx = {
        "subjects": subjects
    }
    return render(request,'subject/list.html',stx)

@login_required_decorator
def teacher_create(request):
    model = Users()
    form = TeacherForm(request.POST or None,instance=model)
    if request.POST and form.is_valid():
        form.save()
        actions = request.session.get('actions', [])
        actions += [f"You created Teacher: {request.POST.get('first_name')}"]
        request.session["actions"] = actions

        teacher_count = request.session.get('teacher_count', 0)
        teacher_count += 1
        request.session["teacher_count"] = teacher_count

        return redirect('teacher_list')

    stx = {
        "form":form
    }
    return render(request,'teacher/form.html',stx)

@login_required_decorator
def teacher_edit(request,pk):
    model = Users.objects.get(pk=pk)
    form = TeacherForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('teacher_list')

    stx = {
        "form": form,
        "model":model
    }

    return render(request, 'teacher/form.html', stx)
@login_required_decorator
def teacher_delete(request,pk):
    model = Users.objects.get(pk=pk)
    model.delete()
    return redirect('teacher_list')

@login_required_decorator
def teacher_list(request):
    teachers = services.get_teacher()
    stx = {
        "teachers":teachers
    }
    return render(request,'teacher/list.html',stx)

@login_required_decorator
@login_required(login_url='login_page')
def student_create(request):
    model = Users()
    form = StudentForm(request.POST or None, request.FILES or None, instance=model)
    if request.method == "POST" and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You created Student: {request.POST.get('first_name')}"]
        request.session["actions"] = actions

        student_count = request.session.get('student_count', 0)
        student_count += 1
        request.session["student_count"] = student_count
        return redirect('student_list')
    ctx = {
        "form": form
    }
    return render(request, 'student/form.html', ctx)



@login_required_decorator
def profile(request):
    return render(request,'profile.html')

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login_page")
    template_name = "signup.html"