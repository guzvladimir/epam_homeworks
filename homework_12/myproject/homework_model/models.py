from django.db import models
from django.db.models import TextField

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    class Meta:
        abstract = True


class Student(Person):
    db_table = "students"


class Teacher(Person):
    db_table = "teachers"


class Homework(models.Model):
    db_table = "homeworks"
    text = models.TextField()
    deadline = models.DateTimeField()
    created = models.DateTimeField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.text


class HomeworkResult(models.Model):
    db_table = "homework_results"
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    solution = models.TextField()
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    created = models.DateTimeField()

    def __str__(self) -> str:
        return self.solution
