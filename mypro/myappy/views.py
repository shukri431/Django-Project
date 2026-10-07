from django.shortcuts import render,HttpResponse, redirect
from .models import Student
from .forms import studentModelForm
# Create your views here.

def home(request):
    context={
        'name': 'jama',
        'age': 30,
        'fruits': ['mango', 'orange']
    }
    return render(request, 'home.html', context)
def base(request):
    return render(request, 'base.html')
def contact (request):
    form = studentModelForm()
    if request.method == "POST":
         form =studentModelForm(request.POST)
         if form.is_valid():
            #  Student.objects.create(
            #      firstname = form.cleaned_data['firstName'],
            #      lastName = form.cleaned_data['lastname'],
            #      email = form.cleaned_data['email'],
            #      age = form.cleaned_data['age']
            #  )
            #  return HttpResponse("success")
            form.save()
            return redirect ("table")
        #  else:
        #      form = studentModelForm()
    return render(request, 'student_add.html',{"form": form})

def table(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def update(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == "POST":
        form = studentModelForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("table")
    else:
        form = studentModelForm(instance=student)
    return render(request, 'update.html', {'form': form})

def delete(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect("table")
    return render(request, 'student_delete.html', {'student': student})


      