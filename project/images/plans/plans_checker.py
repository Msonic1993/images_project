from images.database_repo.plans import PlansTab
from images.models import Plans, Sizes


class Plans:

    def check(self,request):
        user_plan = PlansTab().getOne(request)
        img_sizes = Sizes.objects.filter(plan=user_plan).values_list('size')
        return str(list(img_sizes))
