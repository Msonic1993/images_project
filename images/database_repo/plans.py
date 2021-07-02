from images.models import Plans


class PlansTab:

    def getOne(self,request):
        data = Plans.objects.get(users=request.user.id)
        return data.id

    def getCurrentPlan(self,request):
        data = Plans.objects.get(users=request.user.id)
        return str(data.name)

    def getOriginalImgOmit(self,request):
        data = Plans.objects.get(users=request.user.id)
        return data.originalImgOmit

    def getExpiringLink(self, request):
        data = Plans.objects.get(users=request.user.id)
        return data.expiringLink