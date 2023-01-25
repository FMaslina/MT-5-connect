from .models import LogRecord
from rest_framework.serializers import ModelSerializer


class LogRecordSerializer(ModelSerializer):
    class Meta:
        model = LogRecord
        fields = "__all__"
