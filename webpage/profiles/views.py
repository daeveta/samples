from django.shortcuts import render, redirect
from .models import Students
from .forms import StudentsForm


def index(request):
    return render(request, 'index.html')


def teachers(request):
    return render(request, 'teachers.html')


def student_list(request):
    student = Students.objects.all()
    return render(request, 'student_list.html', {'student': student})


def students(request):
    if request.method == "POST":
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-list')

    form = StudentsForm()
    context = {
        'form': form,
    }

    return render(request, 'students.html', context)

#
# def student_id(request, id):
#     return render(request, 'student-list.html', {'coder': Students.odjects.get(pk=int(id))})