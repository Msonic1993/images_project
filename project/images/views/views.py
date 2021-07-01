import os
from PIL import Image
from django.conf import settings
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

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
        current_user_plan = PlansTab().getCurrentPlan(request)
        originalImgOmit = PlansTab().getOriginalImgOmit(request)
        expiringLinkFlag = PlansTab().getExpiringLink(request)
        if os.path.exists(settings.MEDIA_ROOT+file_url):
           sizes = Plans().check(request)
           data_list = []
           for i in sizes:
                im1 = Image.open(settings.MEDIA_ROOT+"\\media\\"+filename)
                im_small = im1.resize((i[0], i[0]), Image.ANTIALIAS)
                im_small.save(settings.MEDIA_ROOT+"\\media\\"+str(i[0])+filename)
                data = {'URLS':request.get_host()+"/media/"+str(i[0])+filename}
                data_list.append(data)
           if originalImgOmit == 0:
                data_list.append(request.get_host()+file_url)
           if expiringLinkFlag == 1:
               data_list.append(request.get_host() + file_url)
               # data = get_some_data_or_whatever()
           return Response(str(current_user_plan) + str(data_list))

        return  Response('File not found')

