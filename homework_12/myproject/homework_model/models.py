from django.db import models
from django.db.models import TextField

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Student(Person):
    db_table = "Student"


class Teacher(Person):
    db_table = "Teacher"


class Homework(models.Model):
    db_table = "Homework"
    text = models.TextField()
    deadline = models.DateTimeField()
    created = models.DateTimeField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self) -> TextField:
        return self.text


class HomeworkResult(models.Model):
    db_table = "Homework_Result"
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    solution = models.TextField()
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    created = models.DateTimeField()

    def __str__(self) -> TextField:
        return self.solution
