from rest_framework import serializers

from api.models.core import LivenessReport

class LivenessReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivenessReport
        fields = ('name', 'code')