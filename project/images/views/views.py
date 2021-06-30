import os

from django.conf.urls.static import static
from django.http import HttpResponse, Http404

from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, GenericViewSet
from images.database_repo.storage import StorageTab
from images.serializers import StorageSerializer
from project import settings
from project.settings import MEDIA_ROOT


class ImagesView(ViewSet):
    serializer_class = StorageSerializer

    def list(self, request):
        queryset = StorageTab().getAll(request)
        serializer = StorageSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self,request):
        path = request.POST['path']
        queryset = StorageTab().getOne(request,path)
        file_url = queryset.file.url()
        print(file_url)
        if os.path.exists(file_url):
            with open(file_url, 'rb') as f:
                return HttpResponse(f.read(), content_type="image/png" )


        raise Http404

