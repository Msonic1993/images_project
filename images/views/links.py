import os
from django.conf import settings
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from images.database_repo.expiringfiles import ExpiringFilesTab
from images.database_repo.plans import PlansTab
from images.database_repo.storage import StorageTab
from images.serializers import StorageSerializer


class ExpiringLinksView(ViewSet):
    # parser_classes = [JSONParser]
    serializer_class = StorageSerializer


    def list(self, request):
        queryset = StorageTab().getAll(request)
        serializer = StorageSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self,request):
        filename = request.POST['fileName']
        availableTime = request.POST['numberOfSeconds']
        queryset = StorageTab().getOne(request, filename)
        file_url = queryset.file.url
        current_user_plan = PlansTab().getCurrentPlan(request)
        expiringLinkFlag = PlansTab().getExpiringLink(request)
        if os.path.exists(settings.MEDIA_ROOT + file_url):
           data_list = []
           if expiringLinkFlag == 1:
               ExpiringFilesTab().createOne(filename,file_url,availableTime,request)
               data_list.append(request.get_host() + file_url)
           return Response('Your plan is '+str(current_user_plan) +'. Your images links '+ str(data_list))

        return  Response('File not found')