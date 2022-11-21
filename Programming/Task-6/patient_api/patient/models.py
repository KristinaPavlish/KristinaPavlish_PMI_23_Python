from django.core.validators import RegexValidator
from django.db import models


class Patients(models.Model):
    app_label = 'patient_api'
    patient_id = models.IntegerField()
    name = models.CharField(max_length=200, verbose_name='name', validators=[
        RegexValidator(regex='^[a-zA-Z ]+$', message='Incorrect name', code='invalid_name')])
    date = models.DateTimeField()
    time = models.TimeField()
    duration = models.IntegerField()
    doctor_name = models.CharField(max_length=200, verbose_name='doctor_name', validators=[
        RegexValidator(regex='^[a-zA-Z ]+$', message='Incorrect doctor name', code='invalid_doctor_name')])
    department = models.CharField(max_length=200, verbose_name='department', validators=[
        RegexValidator(regex='^[a-zA-Z ]+$', message='Incorrect department', code='invalid_department')])

    def __str__(self):
        return "\nid: " + str(self.patient_id) + "\nname: " + self.name + "\ndate: " + str(
            self.date) + "\ntime: " + str(self.time) + "\nduration: " + str(
            self.duration) + "\ndoctor_name: " + self.doctor_name + "\ndepartment: " + self.department

    class Meta:
        app_label = 'patient_api'
