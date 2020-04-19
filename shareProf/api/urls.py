from django.urls import path, include
from shareProf.api.views import model_views
from shareProf.api.views import auth_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'log', model_views.LogViewSet)
router.register(r'ip', model_views.IpViewSet)
router.register(r'users', auth_views.UserViewSet)
router.register(r'groups', auth_views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls))
]
