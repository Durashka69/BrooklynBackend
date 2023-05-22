from rest_framework.routers import DefaultRouter

from .views import ImageModelViewSet


router = DefaultRouter()

router.register('api/images', ImageModelViewSet, basename='api/images')

urlpatterns = []
urlpatterns += router.urls
