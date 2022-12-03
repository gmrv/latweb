from django.urls import path

from main.views.view import liveness_report

app='main'

urlpatterns = [
    path('livenessreport', liveness_report),
    path('livenessreport/<str:device_name>/<int:min_per_interval>', liveness_report),

]
