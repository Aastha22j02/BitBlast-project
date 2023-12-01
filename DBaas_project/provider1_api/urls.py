# from django.contrib import admin
# from django.urls import path, include
# from provider_app.views import ProviderViewSet
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'provider', ProviderViewSet, basename='provider')

# urlpatterns = [
#     path("", include(router.urls)),
    
# ]
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from provider1_api.views import ProviderViewSet

router = DefaultRouter()
router.register(r'providers', ProviderViewSet, basename='provider')

urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^providers/by-name/(?P<provider_name>[-\w]+)/$', ProviderViewSet.as_view({'get': 'get_provider_by_name'}), name='get-provider-by-name'),
    re_path(r'^providers/by-user/(?P<user_id>\d+)/$', ProviderViewSet.as_view({'get': 'get_provider_by_user_id'}), name='get-provider-by-user-id'),
]

