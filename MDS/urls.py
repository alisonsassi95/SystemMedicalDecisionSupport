from django.contrib import admin
from django.urls import path, include
from patient import views as viewsPatient
from validation import views as viewsValidation

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', viewsValidation.home, name='home'),
    #path('patient/', viewsPatient.patient, name='patient'),
    #path('records/', viewsPatient.db_record, name='records'),
    #path('validation/<int:validateNumb>', views.validation, name='validation'),
]
