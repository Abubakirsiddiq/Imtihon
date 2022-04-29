from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

def student(request):
    if request.method == 'POST':
        Student.objects.create(
            ism=request.POST.get("ism"),
            yosh=request.POST.get("yosh"),
            kurs=request.POST.get("kurs"),
            student_raqam=request.POST.get("student_raqam")
        )
        return redirect("/student/")
    soz=request.Get.get("qidirish")
    if soz == None:

    return render(request, "Student.html", {"student":s})

def student_ochir(request, son):
    Student.objects.get(id=son).delete()
    return redirect("/student/")

def muallif(request):
    if request.method == 'POST':
        if request.POST.get("bajarilgan") == "False":
            natija = False
        else:
            natija = True
        Muallif.objects.create(
            sarlavha=request.POST.get("sarlavha"),
            sana=request.POST.get("sana"),
            batafsil_malumot=request.POST.get("batafsil_malumot"),
            bajarilgan=natija,
            student=student
        )
        return redirect("/student/")
    s=Muallif.objects.all()
    return render(request, "Student.html", {"student":s})
