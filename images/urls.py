
from django.urls import path, include
from rest_framework import routers

from .views.links import ExpiringLinksView
from .views.login import userLogin
from .views.logout import userLogout
from .views.upload import FileUploadView
from .views.images import ImagesView
router =routers.DefaultRouter()
router.register('images', ImagesView, basename="images")
router.register(r'upload', FileUploadView, basename="upload")
router.register(r'generatelinks', ExpiringLinksView, basename="generatelinks")


urlpatterns = [
    path('', include(router.urls)),
    path('login/', userLogin, name="login"),
    path('logout/', userLogout, name="logout"),
]


