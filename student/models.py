from django.db import models


class Student(models.Model):
    ism=models.CharField(max_length=30)
    yosh=models.PositiveSmallIntegerField()
    kurs=models.PositiveSmallIntegerField()
    student_raqam=models.PositiveSmallIntegerField(unique=True)


class Muallif(models.Model):
    sarlavha=models.CharField(max_length=50)
    sana=models.DateField()
    batafsil_malumot=models.CharField(max_length=50, blank=True)
    bajarilgan=models.BooleanField()
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
