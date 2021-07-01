import os

from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse, Http404
from django.utils.timezone import now

from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, GenericViewSet

from images.database_repo.plans import PlansTab
from images.database_repo.storage import StorageTab
from images.plans.plans_checker import Plans
from images.serializers import StorageSerializer



class ImagesView(ViewSet):
    serializer_class = StorageSerializer

    def list(self, request):
        queryset = StorageTab().getAll(request)
        serializer = StorageSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self,request):
        filename = request.POST['fileName']
        queryset = StorageTab().getOne(request,filename)
        file_url = queryset.file.url
        if os.path.exists(settings.MEDIA_ROOT+file_url):
           sizes = Plans().check(request)
           data = {
           'images-url': reverse ('images', args = [file_url], request = request)
           }
           return Response (data)


        return  Response('File not found')


