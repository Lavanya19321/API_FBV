from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from app.models import *
from app.serializer import *
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def school_jsondata(request):
    SOD=school.objects.all()
    JSOD=schoolmodelserializer(SOD,many=True)
    jsondata=JSOD.data
    return Response(jsondata)