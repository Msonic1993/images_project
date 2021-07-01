from django.contrib.auth import login
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.utils import json
from images.models import User

@api_view(["GET"])
@permission_classes([AllowAny])
def test(request):

    url = 'dupa'
    return HttpResponse(url)