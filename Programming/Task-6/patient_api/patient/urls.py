from django.urls import path

from . import views

app_name = 'patient-api'
urlpatterns = [
    path('patients', views.get_patients, name='index'),
    path('patient/<int:patient_id>', views.get_patient, name='detail'),
    path('patient', views.create_patient, name='create_patient'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
