from django.db import models

# Create your models here.
class Course(models.Model):
    cname=models.CharField(max_length=100,primary_key=True)
    cprice=models.IntegerField(default=30000)

    def __str__(self):
        return self.cname

class Student(models.Model):
    cname=models.ForeignKey(Course,on_delete=models.CASCADE)
    sname=models.CharField(max_length=100)
    sid=models.IntegerField()

    def __str__(self):
        return self.sname