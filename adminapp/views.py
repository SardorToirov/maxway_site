from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import *
from home import services


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
    model = Category()
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
    model = Category.objects.get(pk=pk)
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
    model = Category.objects.get(pk=pk)
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
def guruh_create(request):
    model = Product()
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
    model = Product.objects.get(pk=pk)
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
    model = Product.objects.get(pk=pk)
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
def subject_create(request):
    model = Order()
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
    model = Order.objects.get(pk=pk)
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
    model = Order.objects.get(pk=pk)
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
    model = User()
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
    model = User.objects.get(pk=pk)
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
    model = User.objects.get(pk=pk)
    model.delete()
    return redirect('teacher_list')

@login_required_decorator
def teacher_list(request):
    teachers = services.get_teacher()
    stx = {
        "teachers":teachers
    }
    return render(request,'teacher/list.html',stx)


@login_required
def order_product_create(request):
    form = OrderProductForm(request.POST or None)
    if request.POST and form.is_valid():
        form.save()
        return redirect('order_product_list')

    ctx = {
        "form": form
    }
    return render(request, 'order_product/form.html', ctx)


@login_required
def order_product_edit(request, pk):
    model = OrderProduct.objects.get(pk=pk)
    form = OrderProductForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('order_product_list')

    ctx = {
        "form": form,
        "model": model
    }
    return render(request, 'order_product/form.html', ctx)


@login_required
def order_product_delete(request, pk):
    model = OrderProduct.objects.get(pk=pk)
    model.delete()
    return redirect('order_product_list')


@login_required
def order_product_list(request):
    order_products = services.get_order_products()
    ctx = {
        "order_products": order_products
    }
    return render(request, 'order_product/list.html', ctx)



@login_required_decorator
def profile(request):
    return render(request,'profile.html')

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login_page")
    template_name = "signup.html"