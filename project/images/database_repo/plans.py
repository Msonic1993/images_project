from images.models import Plans


class PlansTab:

    def getOne(self,request):
        data = Plans.objects.get(users=request.user.id)
        return data.id
