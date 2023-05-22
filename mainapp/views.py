from rest_framework.viewsets import ReadOnlyModelViewSet

from .serializers import ImageModelSerializer
from .models import ImageModel


class ImageModelViewSet(ReadOnlyModelViewSet):
    queryset = ImageModel.objects.all()
    serializer_class = ImageModelSerializer
