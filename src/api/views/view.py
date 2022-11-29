from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models.core import LivenessReport
from api.serializers.sirializer import LivenessReportSerializer

class LivenessReportAPIView(APIView):
    def get(self, request):
        lst = LivenessReport.objects.all().values()
        return Response(lst)

    def post(self, request, device_name):
        line_new = LivenessReport.objects.create(
            name=device_name,
            code=0
        )
        return Response({'post': model_to_dict(line_new)})