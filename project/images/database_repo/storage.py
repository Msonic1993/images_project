from images.models import Storage

class StorageTab:

    def getAll(self,request):

        if request.user.is_superuser == False:
            data = Storage.objects.filter(owner_id= request.user.id)
        else:
            data = Storage.objects.filter()
        return data

    def getOne(self, request,path):

        if request.user.is_superuser == False:
            data = Storage.objects.get(path=path)
        else:
            data = Storage.objects.get(path=path)
        return data
