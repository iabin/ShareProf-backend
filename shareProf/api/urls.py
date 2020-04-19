from django.urls import path, include
from shareProf.api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'log', views.model_views.LogViewSet)
router.register(r'ip', views.model_views.IpViewSet)
router.register('country', views.CountryViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls))
]
