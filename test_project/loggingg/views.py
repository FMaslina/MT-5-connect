from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import LogRecord
from .serializers import LogRecordSerializer
from rest_framework import generics, status, fields


class LogRecordViewSetCreate(generics.CreateAPIView):
    serializer_class = LogRecordSerializer
    queryset = LogRecord.objects.all()


class LogRecordViewSetGet(generics.RetrieveAPIView):
    serializer_class = LogRecordSerializer
    queryset = LogRecord.objects.all()


class LogRecordViewSetDelete(generics.DestroyAPIView):
    serializer_class = LogRecordSerializer
    queryset = LogRecord.objects.all()


class LogRecordViewSetList(generics.ListAPIView):
    serializer_class = LogRecordSerializer
    queryset = LogRecord.objects.all()


class LogRecordViewSetUpdate(generics.UpdateAPIView):
    serializer_class = LogRecordSerializer
    queryset = LogRecord.objects.all()


@api_view(['POST'])
@csrf_exempt
def ask(request):
    fields_1 = request.data
    print(request)
    request.data['comment'] = fields_1.get('ask')
    return Response({"m": fields_1.get('ask')}, status=status.HTTP_200_OK)