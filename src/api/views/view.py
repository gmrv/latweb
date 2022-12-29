from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models.core import LivenessReport


def has_command(device_name) -> bool:
    return True


def get_command(device_name) -> str:
    return "ls -la"


class LivenessReportAPIView(APIView):
    def get(self, request):
        lst = LivenessReport.objects.all().values()
        return Response(lst)

    def post(self, request, device_name):
        line_new = LivenessReport.objects.create(
            name=device_name,
            code=0
        )

        model_dict = model_to_dict(line_new)

        if has_command(device_name):
            model_dict["command"] = get_command(device_name)

        return Response({'post': model_dict})