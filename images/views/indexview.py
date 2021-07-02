from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from werkzeug import Response



def indexview(request):
    return HttpResponse('Hello. Please goto /api/login/')