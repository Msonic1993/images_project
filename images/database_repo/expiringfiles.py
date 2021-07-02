from images.models import ExpiringFiles


class ExpiringFilesTab:

    def getAll(self,request):

        if request.user.is_superuser == False:
            data = ExpiringFiles.objects.filter(owner_id= request.user.id)
        else:
            data = ExpiringFiles.objects.filter()
        return data

    def getOne(self, request,filename):

        if request.user.is_superuser == False:
            data = ExpiringFiles.objects.get(fileName=filename)
        else:
            data = ExpiringFiles.objects.get(fileName=filename)
        return data.path


    def createOne(self,filename,path,availableTime,request):
       self.data =  ExpiringFiles.objects.create(fileName=filename,path=path,availableTime=availableTime,owner=request.user.id)
       return self.data

