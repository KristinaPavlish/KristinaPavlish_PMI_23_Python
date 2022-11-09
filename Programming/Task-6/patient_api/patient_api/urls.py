from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('patient-api/api/', include('patient.urls')),
    path('admin/', admin.site.urls),
]

