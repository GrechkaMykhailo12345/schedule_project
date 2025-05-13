from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return f"Назва предмету: {self.name}"

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    def __str__(self):
        return f"Ім'я вчителя: {self.name}"

class Class(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField(default=1)
    def __str__(self):
        return f"Назва класу: {self.name}"

class Student(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    class_group = models.ForeignKey(Class, on_delete=models.CASCADE)
    def __str__(self):
        return f"Ім'я студенту: {self.name}"

class Schedule(models.Model):
    day = models.CharField(max_length=100)
    hour = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_group = models.ForeignKey(Class, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    def __str__(self):
        return f"Розклад: {self.day}, {self.hour}"

class Grade(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.IntegerField()
    date = models.CharField(max_length=100)
    def __str__(self):
        return f"Оцінка: {self.grade}"