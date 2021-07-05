from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('rev/', views.SoundView, name='rev'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
