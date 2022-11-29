from django.urls import path
from .views.view import LivenessReportAPIView

app='api'
urlpatterns = [
    path('v1/livenessreport', LivenessReportAPIView.as_view()),
    path('v1/livenessreport/<str:device_name>', LivenessReportAPIView.as_view()),
]