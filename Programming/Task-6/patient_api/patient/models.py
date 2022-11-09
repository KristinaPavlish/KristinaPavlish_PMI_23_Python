from django.db import models


# Create your models here.

class Patients(models.Model):
    app_label  = 'Patients'
    id = models.IntegerField()
    patient_name = models.CharField(max_length=200)
    date = models.DateTimeField()
    time = models.TimeField()
    duration = models.IntegerField()
    doctor_name = models.CharField(max_length=200)
    department = models.CharField(max_length=200)

    def __str__(self):
        return "\nid: " + self.id + "\nname: " + self.name+ "\ndate: " + self.date+ "\ntime: " + self.time\
               + "\nduration: " + self.duration + "\ndoctor_name: " + self.doctor_name + "\ndepartment: " + self.department


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=model.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)